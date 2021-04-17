#!/usr/bin/python

#  Copyright (c) Lightstreamer Srl.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
import logging
import threading
import time
import traceback
import os
import datetime
import math 

# Modules aliasing and function utilities to support a
# very coarse version differentiation between Python 2 and Python 3.
PY3 = sys.version_info[0] == 3
PY2 = sys.version_info[0] == 2

if PY3:
    from urllib.request import urlopen as _urlopen
    from urllib.parse import (urlparse as parse_url, urljoin, urlencode)

    def _url_encode(params):
        return urlencode(params).encode("utf-8")

    def _iteritems(d):
        return iter(d.items())

    def wait_for_input():
        input("{0:-^80}\n".format("HIT CR TO UNSUBSCRIBE AND DISCONNECT FROM \
LIGHTSTREAMER"))

else:
    from urllib import (urlopen as _urlopen, urlencode)
    from urlparse import urlparse as parse_url
    from urlparse import urljoin

    def _url_encode(params):
        return urlencode(params)

    def _iteritems(d):
        return d.iteritems()

    def wait_for_input():
        raw_input("{0:-^80}\n".format("HIT CR TO UNSUBSCRIBE AND DISCONNECT FROM \
LIGHTSTREAMER"))

CONNECTION_URL_PATH = "lightstreamer/create_session.txt"
BIND_URL_PATH = "lightstreamer/bind_session.txt"
CONTROL_URL_PATH = "lightstreamer/control.txt"
# Request parameter to create and activate a new Table.
OP_ADD = "add"
# Request parameter to delete a previously created Table.
OP_DELETE = "delete"
# Request parameter to force closure of an existing session.
OP_DESTROY = "destroy"
# List of possible server responses
PROBE_CMD = "PROBE"
END_CMD = "END"
LOOP_CMD = "LOOP"
ERROR_CMD = "ERROR"
SYNC_ERROR_CMD = "SYNC ERROR"
OK_CMD = "OK"

log = logging.getLogger("iss-live")
#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))


class Subscription(object):
    """Represents a Subscription to be submitted to a Lightstreamer Server."""

    def __init__(self, mode, items, fields, adapter=""):
        self.item_names = items
        self._items_map = {}
        self.field_names = fields
        self.adapter = adapter
        self.mode = mode
        self.snapshot = "true"
        self._listeners = []

    def _decode(self, value, last):
        """Decode the field value according to
        Lightstreamer Text Protocol specifications.
        """
        if value == "$":
            return u''
        elif value == "#":
            return None
        elif not value:
            return last
        elif value[0] in "#$":
            value = value[1:]

        return value

    def addlistener(self, listener):
        self._listeners.append(listener)

    def notifyupdate(self, item_line):
        """Invoked by LSClient each time Lightstreamer Server pushes
        a new item event.
        """
        # Tokenize the item line as sent by Lightstreamer
        toks = item_line.rstrip('\r\n').split('|')
        undecoded_item = dict(list(zip(self.field_names, toks[1:])))

        # Retrieve the previous item stored into the map, if present.
        # Otherwise create a new empty dict.
        item_pos = int(toks[0])
        curr_item = self._items_map.get(item_pos, {})
        # Update the map with new values, merging with the
        # previous ones if any.
        self._items_map[item_pos] = dict([
            (k, self._decode(v, curr_item.get(k))) for k, v
            in list(undecoded_item.items())
        ])
        # Make an item info as a new event to be passed to listeners
        item_info = {
            'pos': item_pos,
            'name': self.item_names[item_pos - 1],
            'values': self._items_map[item_pos]
        }

        # Update each registered listener with new event
        for on_item_update in self._listeners:
            on_item_update(item_info)
            
class LSClient(object):
    """Manages the communication with Lightstreamer Server"""

    def __init__(self, base_url, adapter_set="", user="", password=""):
        self._base_url = parse_url(base_url)
        self._adapter_set = adapter_set
        self._user = user
        self._password = password
        self._session = {}
        self._subscriptions = {}
        self._current_subscription_key = 0
        self._stream_connection = None
        self._stream_connection_thread = None
        self._bind_counter = 0

    def _encode_params(self, params):
        """Encode the parameter for HTTP POST submissions, but
        only for non empty values..."""
        return _url_encode(
            dict([(k, v) for (k, v) in _iteritems(params) if v])
        )

    def _call(self, base_url, url, params):
        """Open a network connection and performs HTTP Post
        with provided params.
        """
        # Combines the "base_url" with the
        # required "url" to be used for the specific request.
        url = urljoin(base_url.geturl(), url)
        body = self._encode_params(params)
        log.debug("Making a request to <%s> with body <%s>", url, body)
        return _urlopen(url, data=body)

    def _set_control_link_url(self, custom_address=None):
        """Set the address to use for the Control Connection
        in such cases where Lightstreamer is behind a Load Balancer.
        """
        if custom_address is None:
            self._control_url = self._base_url
        else:
            parsed_custom_address = parse_url("//" + custom_address)
            self._control_url = parsed_custom_address._replace(
                scheme=self._base_url[0]
            )

    def _control(self, params):
        """Create a Control Connection to send control commands
        that manage the content of Stream Connection.
        """
        params["LS_session"] = self._session["SessionId"]
        response = self._call(self._control_url, CONTROL_URL_PATH, params)
        decoded_response = response.readline().decode("utf-8").rstrip()
        log.debug("Server response: <%s>", decoded_response)
        return decoded_response

    def _read_from_stream(self):
        """Read a single line of content of the Stream Connection."""
        line = self._stream_connection.readline().decode("utf-8").rstrip()
        return line

    def connect(self):
        """Establish a connection to Lightstreamer Server to create a new
        session.
        """
        log.debug("Opening a new session to <%s>", self._base_url.geturl())
        self._stream_connection = self._call(
            self._base_url,
            CONNECTION_URL_PATH,
            {
             "LS_op2": 'create',
             "LS_cid": 'mgQkwtwdysogQz2BJ4Ji kOj2Bg',
             "LS_adapter_set": self._adapter_set,
             "LS_user": self._user,
             "LS_password": self._password}
        )
        stream_line = self._read_from_stream()
        self._handle_stream(stream_line)

    def bind(self):
        """Replace a completely consumed connection in listening for an active
        Session.
        """
        log.debug("Binding to <%s>", self._control_url.geturl())
        self._stream_connection = self._call(
            self._control_url,
            BIND_URL_PATH,
            {
             "LS_session": self._session["SessionId"]
             }
        )

        self._bind_counter += 1
        stream_line = self._read_from_stream()
        self._handle_stream(stream_line)
        log.info("Bound to <%s>", self._control_url.geturl())

    def _handle_stream(self, stream_line):
        if stream_line == OK_CMD:
            log.info("Successfully connected to <%s>", self._base_url.geturl())
            log.debug("Starting to handling real-time stream")
            # Parsing session inkion
            while 1:
                next_stream_line = self._read_from_stream()
                if next_stream_line:
                    session_key, session_value = next_stream_line.split(":", 1)
                    self._session[session_key] = session_value
                else:
                    break

            # Setup of the control link url
            self._set_control_link_url(self._session.get("ControlAddress"))

            # Start a new thread to handle real time updates sent
            # by Lightstreamer Server on the stream connection.
            self._stream_connection_thread = threading.Thread(
                name="StreamThread-{0}".format(self._bind_counter),
                target=self._receive
            )
            self._stream_connection_thread.setDaemon(True)
            self._stream_connection_thread.start()
            log.info("Started handling of real-time stream")
        else:
            lines = self._stream_connection.readlines()
            lines.insert(0, stream_line)

            log.error("\nServer response error: \n%s", "".join([str(line) for line in lines]))
            raise IOError()

    def _join(self):
        """Await the natural StreamThread termination."""
        if self._stream_connection_thread:
            log.debug("Waiting for thread to terminate")
            self._stream_connection_thread.join()
            self._stream_connection_thread = None
            log.debug("Thread terminated")

    def disconnect(self):
        """Request to close the session previously opened with the connect()
        invocation.
        """
        if self._stream_connection is not None:
            log.debug("Closing session to <%s>", self._base_url.geturl())
            server_response = self._control({"LS_op": OP_DESTROY})
            # There is no need to explicitly close the connection, since it is
            # handled by thread completion.
            self._join()
            log.info("Closed session to <%s>", self._base_url.geturl())
        else:
            log.warning("No connection to Lightstreamer")

    def subscribe(self, subscription):
        """"Perform a subscription request to Lightstreamer Server."""
        # Register the Subscription with a new subscription key
        self._current_subscription_key += 1
        self._subscriptions[self._current_subscription_key] = subscription

        # Send the control request to perform the subscription
        log.debug("Making a new subscription request")
        # that LS_snapshot is the key to getting the last/current value of the telemetry
        # I had to pick apart the actual Javascript client source to get this 
        # line 487 here: https://github.com/Lightstreamer/Lightstreamer-lib-client-javascript/blob/33378e564926146ac96cf185da1c5e4ee6545043/source/Subscription.js#L1153
        # LS_requested_max_frequency is another one to add possibly to keep data updates down for very active items (e.g. ,"TIME_000001")
        server_response = self._control({
            "LS_Table": self._current_subscription_key,
            "LS_op": OP_ADD,
            "LS_data_adapter": subscription.adapter,
            "LS_mode": subscription.mode,
            "LS_snapshot": 'true',
            "LS_requested_max_frequency" : 0.033,
            "LS_schema": " ".join(subscription.field_names),
            "LS_id": " ".join(subscription.item_names),
        })
        if server_response == OK_CMD:
            log.info("Successfully subscribed ")
        else:
            log.warning("Subscription error")
        return self._current_subscription_key

    def unsubscribe(self, subcription_key):
        """Unregister the Subscription associated to the
        specified subscription_key.
        """
        log.debug("Making an unsubscription request")
        if subcription_key in self._subscriptions:
            server_response = self._control({
                "LS_Table": subcription_key,
                "LS_op": OP_DELETE
            })

            if server_response == OK_CMD:
                del self._subscriptions[subcription_key]
                log.info("Successfully unsubscribed")
            else:
                log.warning("Unsubscription error")
        else:
            log.warning("No subscription key %s found!", subcription_key)

    def _forward_update_message(self, update_message):
        """Forwards the real time update to the relative
        Subscription instance for further dispatching to its listeners.
        """
        log.debug("Received update message: <%s>", update_message)
        try:
            tok = update_message.split(',', 1)
            table, item = int(tok[0]), tok[1]
            if table in self._subscriptions:
                self._subscriptions[table].notifyupdate(item)
            else:
                log.warning("No subscription found!")
        except Exception:
            print(traceback.format_exc())

    def _receive(self):
        rebind = False
        receive = True
        while receive:
            log.debug("Waiting for a new message")
            try:
                message = self._read_from_stream()
                log.debug("Received message: <%s>", message)
                if not message.strip():
                    message = None
            except Exception:
                log.error("Communication error")
                print(traceback.format_exc())
                message = None

            if message is None:
                receive = False
                log.warning("No new message received")
            elif message == PROBE_CMD:
                # Skipping the PROBE message, keep on receiving messages.
                log.debug("PROBE message")
            elif message.startswith(ERROR_CMD):
                # Terminate the receiving loop on ERROR message
                receive = False
                log.error("ERROR")
            elif message.startswith(LOOP_CMD):
                # Terminate the the receiving loop on LOOP message.
                # A complete implementation should proceed with
                # a rebind of the session.
                log.debug("LOOP")
                receive = False
                rebind = True
            elif message.startswith(SYNC_ERROR_CMD):
                # Terminate the receiving loop on SYNC ERROR message.
                # A complete implementation should create a new session
                # and re-subscribe to all the old items and relative fields.
                log.error("SYNC ERROR")
                receive = False
            elif message.startswith(END_CMD):
                # Terminate the receiving loop on END message.
                # The session has been forcibly closed on the server side.
                # A complete implementation should handle the
                # "cause_code" if present.
                log.info("Connection closed by the server")
                receive = False
            elif message.startswith("Preamble"):
                # Skipping Preamble message, keep on receiving messages.
                log.debug("Preamble")
            else:
                self._forward_update_message(message)

        if not rebind:
            log.debug("No rebind to <%s>, clearing internal session data",
                      self._base_url.geturl())
            # Clear internal data structures for session
            # and subscriptions management.
            self._stream_connection = None
            self._session.clear()
            self._subscriptions.clear()
            self._current_subscription_key = 0
        else:
            log.debug("Binding to this active session")
            self.bind()

def TS_to_GMT( tsu ) :
    ts_str = tsu.encode('ascii', 'ignore')
    ts = float( ts_str )  
    ts_day = int(ts/24)
    ts_hour = int(((ts/24)-ts_day)*24)
    ts_minute = int((((ts/24)-ts_day)*24-ts_hour)*60)
    ts_seconds = int(((((((ts/24)-ts_day)*24-ts_hour)*60) - ts_minute)*60))
    return ("GMT " + str(ts_day) + "/" + str(ts_hour) + ":" + str(ts_minute) + ":" + str(ts_seconds))
    
logging.basicConfig(stream=sys.stdout, format='%(asctime)s %(levelname)-7s ' +
                    '%(threadName)-15s %(message)s', level=logging.INFO)

# Establishing a new connection to Lightstreamer Server
print("Starting connection")
# lightstreamer_client = LSClient("http://localhost:8080", "DEMO")
lightstreamer_client = LSClient("http://push.lightstreamer.com","ISSLIVE")
try:
    lightstreamer_client.connect()
except Exception as e:
    print("Unable to connect to Lightstreamer Server")
    print(traceback.format_exc())
    sys.exit(1)

print "ARE WE CONNECTED?"


# Import globals for the PUI's and specialPUIs

from PUI import *

'''
subscription = Subscription(
    mode="MERGE",
    items=["AIRLOCK000001","AIRLOCK000002","AIRLOCK000003","AIRLOCK000004","AIRLOCK000005","AIRLOCK000006",
"AIRLOCK000007","AIRLOCK000008","AIRLOCK000009","AIRLOCK000010","AIRLOCK000011","AIRLOCK000012",
"AIRLOCK000013","AIRLOCK000014","AIRLOCK000015","AIRLOCK000016","AIRLOCK000017","AIRLOCK000018",
"AIRLOCK000019","AIRLOCK000020","AIRLOCK000021","AIRLOCK000022","AIRLOCK000023","AIRLOCK000024",
"AIRLOCK000025","AIRLOCK000026","AIRLOCK000027","AIRLOCK000028","AIRLOCK000029","AIRLOCK000030",
"AIRLOCK000031","AIRLOCK000032","AIRLOCK000033","AIRLOCK000034","AIRLOCK000035","AIRLOCK000036",
"AIRLOCK000037","AIRLOCK000038","AIRLOCK000039","AIRLOCK000040","AIRLOCK000041","AIRLOCK000042",
"AIRLOCK000043","AIRLOCK000044","AIRLOCK000045","AIRLOCK000046","AIRLOCK000047","AIRLOCK000048",
"AIRLOCK000049","AIRLOCK000050","AIRLOCK000051","AIRLOCK000052","AIRLOCK000053","AIRLOCK000054",
"AIRLOCK000055","AIRLOCK000056","AIRLOCK000057","NODE2000001","NODE2000002","NODE2000003",
"NODE2000006","NODE2000007","NODE3000001","NODE3000002","NODE3000003","NODE3000004",
"NODE3000005","NODE3000006","NODE3000007","NODE3000008","NODE3000009","NODE3000010",
"NODE3000011","NODE3000012","NODE3000013","NODE3000017","NODE3000018","NODE3000019",
"USLAB000053","USLAB000054","USLAB000055","USLAB000056","USLAB000057","USLAB000058",
"USLAB000059","USLAB000060","USLAB000061","USLAB000062","USLAB000063","USLAB000064",
"USLAB000065","AIRLOCK000058","NODE1000001","NODE1000002","NODE2000004","NODE2000005",
"NODE3000014","NODE3000015","NODE3000016","NODE3000020","P1000006","P1000008",
"P1000009","P3000001","P3000002","P4000003","P4000006","P6000003","P6000006",
"S0000010","S0000011","S0000012","S0000013","S1000006","S1000007","S1000008",
"S3000001","S3000002","S4000003","S4000006","S6000003","S6000006","USLAB000066",
"USLAB000067","USLAB000068","USLAB000069","USLAB000070","USLAB000071","USLAB000072",
"USLAB000073","USLAB000074","USLAB000075","USLAB000076","USLAB000077","USLAB000078",
"USLAB000079","USLAB000080","P1000001","P1000002","P1000003","P4000001",
"P4000002","P4000004","P4000005","P4000007","P4000008","P6000001",
"P6000002","P6000004","P6000005","P6000007","P6000008","S1000001",
"S1000002","S1000003","S4000001","S4000002","S4000004","S4000005",
"S4000007","S4000008","S6000001","S6000002","S6000004","S6000005",
"S6000007","S6000008","P1000004","P1000005","P1000007","S1000004",
"S1000009","USLAB000088","USLAB000089","USLAB000090","USLAB000091","USLAB000092",
"USLAB000093","USLAB000094","USLAB000095","USLAB000096","USLAB000097","USLAB000098",
"USLAB000099","USLAB000100","USLAB000101","Z1000013","Z1000014","Z1000015",
"S0000001","S0000002","S0000003","S0000004","S0000005","S0000006",
"S0000007","S0000008","S0000009","USLAB000081","RUSSEG000001","RUSSEG000002",
"RUSSEG000003","RUSSEG000004","RUSSEG000005","RUSSEG000006","RUSSEG000007","RUSSEG000008",
"RUSSEG000009","RUSSEG000010","RUSSEG000011","RUSSEG000012","RUSSEG000013","RUSSEG000014",
"RUSSEG000015","RUSSEG000016","RUSSEG000017","RUSSEG000018","RUSSEG000019","RUSSEG000020",
"RUSSEG000021","RUSSEG000022","RUSSEG000023","RUSSEG000024","S1000005","USLAB000001",
"USLAB000002","USLAB000003","USLAB000004","USLAB000005","USLAB000006","USLAB000007",
"USLAB000008","USLAB000009","USLAB000011","USLAB000013","USLAB000014","USLAB000015",
"USLAB000016","USLAB000017","USLAB000018","USLAB000019","USLAB000020","USLAB000021",
"USLAB000022","USLAB000023","USLAB000024","USLAB000025","USLAB000026","USLAB000027",
"USLAB000028","USLAB000029","USLAB000030","USLAB000031","USLAB000038","USLAB000039",
"USLAB000040","USLAB000041","USLAB000042","USLAB000043","USLAB000044","USLAB000045",
"USLAB000046","USLAB000047","USLAB000048","USLAB000049","USLAB000050","USLAB000051",
"USLAB000052","Z1000001","Z1000002","Z1000003","Z1000004","Z1000005",
"Z1000006","Z1000007","Z1000008","Z1000009","Z1000010","Z1000011",
"Z1000012","USLAB000010","USLAB000012","RUSSEG000025","USLAB000032","USLAB000033",
"USLAB000034","USLAB000035","USLAB000036","USLAB000037","USLAB000082","USLAB000083",
"USLAB000084","USLAB000085","USLAB000087","USLAB000086","USLAB000102","TIME_000001",
"TIME_000002","CSAMT000001","CSAMT000002","CSASSRMS001","CSASSRMS002","CSASSRMS003",
"CSASSRMS004","CSASSRMS005","CSASSRMS006","CSASSRMS007","CSASSRMS008","CSASSRMS009",
"CSASSRMS010","CSASSRMS011","CSASPDM0001","CSASPDM0002","CSASPDM0003","CSASPDM0004",
"CSASPDM0005","CSASPDM0006","CSASPDM0007","CSASPDM0008","CSASPDM0009","CSASPDM0010",
"CSASPDM0011","CSASPDM0012","CSASPDM0013","CSASPDM0014","CSASPDM0015","CSASPDM0016",
"CSASPDM0017","CSASPDM0018","CSASPDM0019","CSASPDM0020","CSASPDM0021","CSASPDM0022",
"CSAMBS00001","CSAMBS00002","CSAMBA00003","CSAMBA00004"],
    fields=["Value","TimeStamp","Status.Class","Status.Indicator","Status.Color","CalibratedData"],
    adapter="")    
'''

# Making a new Subscription in MERGE mode
# "USLAB000040" Solar Beta Angle
# "USLAB000088" Ku-Band Video Downlink Channel 1 Activity
# "USLAB000089" Ku-Band Video Downlink Channel 1 Activity
# "USLAB000090" Ku-Band Video Downlink Channel 1 Activity
# "USLAB000091" Ku-Band Video Downlink Channel 1 Activity
# USLAB000095 Video Source Routed to Downlink 1
# USLAB000096 Video Source Routed to Downlink 2
# USLAB000097 Video Source Routed to Downlink 3
# USLAB000098 Video Source Routed to Downlink 4

#Normally MERGE mode vs DISTINCT
#"LS_requested_max_frequency" : 1,
#items=["USLAB000040","USLAB000086","USLAB000081","USLAB000012","USLAB000088","USLAB000089","USLAB000090","USLAB000091",
#"USLAB000095","USLAB000096","USLAB000097","USLAB000098"],
#items=["USLAB000040","USLAB000086","USLAB000081","USLAB000012","USLAB000095","USLAB000096","USLAB000097","USLAB000098"],

#STB_POWER = "S4000001","S4000002","S4000007"
#PRT_POWER = "P6000004","P6000005","P6000008"
# "S0000003","S0000004","S0000008","S0000009","P6000004","P6000005","P6000008","S4000001","S4000002","S4000007"
# "USLAB000018","USLAB000019","USLAB000020","USLAB000021"

Qvals = ["USLAB000018","USLAB000019","USLAB000020","USLAB000021"]
yaw = None
pitch = None
roll = None 
LVLH = {}

def initLVLH() :
    global LVLH
    LVLH = {}

def gotAllLVLH(item_name, item_value) :
    global LVLH
    if item_name in Qvals :
       LVLH[item_name] = float(item_value.encode('ascii', 'ignore'))
    
       gotall = True
       for i in Qvals :
           if not LVLH.has_key(i) :
              gotall = False
              break 
    
    return gotall

def setRPY() :
    global yaw,pitch,roll, LVLH
    Q0 = LVLH["USLAB000018"]
    Q1 = LVLH["USLAB000019"]
    Q2 = LVLH["USLAB000020"]
    Q3 = LVLH["USLAB000021"]
    
    c12 = 2 * (Q1 * Q2 + Q0 * Q3)
    c11 = Q0 * Q0 + Q1 * Q1 - Q2 * Q2 - Q3 * Q3
    c13 = 2 * (Q1 * Q3 - Q0 * Q2)
    c23 = 2 * (Q2 * Q3 + Q0 * Q1)
    c33 = Q0 * Q0 - Q1 * Q1 - Q2 * Q2 + Q3 * Q3
    c22 = Q0 * Q0 - Q1 * Q1 + Q2 * Q2 - Q3 * Q3
    c21 = 2 * (Q1 * Q2 - Q0 * Q3)
    mag_c13 = abs(c13) #all c's should be in radians
    
    yaw = 0.0
    pitch = 0.0
    roll = 0.0
    
    if (mag_c13 < 1):       
       yaw = math.atan2(c12, c11)
       pitch = math.atan2(-c13, math.sqrt(1.0 - (c13 * c13)))
       roll = math.atan2(c23, c33)

    elif (mag_c13 == 1): 
         yaw = math.atan2(-c21, c22)
         pitch = math.asin(-c13)
         roll = 0.0
    			
    #convert to degrees
    yaw = yaw * 180 / math.pi
    pitch = pitch * 180 / math.pi
    roll = roll * 180 / math.pi 
        
    initLVLH()   

initLVLH()

subscription = Subscription(
    mode="MERGE",
    items=["USLAB000086","USLAB000081","USLAB000012","USLAB000016","USLAB000018","USLAB000019","USLAB000020","USLAB000021"],
    fields=["Value","TimeStamp"],
    adapter="") 

FileModEpochYear = datetime.datetime(2020, 12, 31)
UnixFileModEpochYear = time.mktime(FileModEpochYear.timetuple())
print "UnixFileModEpochYear",UnixFileModEpochYear

def unixtimestamp_to_dt(uts) :
    dt =datetime.datetime.fromtimestamp(uts)
    #print dt.strftime('%Y-%m-%d %H:%M:%S')
    return dt    
# A simple function acting as a Subscription listener

csv_file = "ls-yaw_pitch-roll.csv"

def on_item_update(item_update):

    
    #print item_update
    item_name = item_update["name"]
    item_value = item_update["values"]["Value"] 
    print "name", item_name, PUI_NAMES[item_name]
    
    if item_name in Qvals :
       if gotAllLVLH(item_name,item_value) :
          setRPY()
          
          #print "  values:",TS_to_GMT(item_update["values"]["TimeStamp"])
          tsu = item_update["values"]["TimeStamp"]
          ts_str = tsu.encode('ascii', 'ignore')
          #print ts_str
          ts = float( ts_str )  
          HoursFromJan1AsEpoch = ts 
          SecondsFromJan1AsEpoch = HoursFromJan1AsEpoch * 60 * 60
          ResultingEpoch =  UnixFileModEpochYear + SecondsFromJan1AsEpoch
          dt =unixtimestamp_to_dt(ResultingEpoch)
          csv_txt = dt.strftime('%Y-%m-%d %H:%M:%S') +","+ str(yaw) +"," + str(pitch) +"," + str(roll) + "\n"
          print csv_txt 
          with open(csv_file, "a") as myfile:
                    myfile.write(csv_txt)
    
    #print item_update.getItemName(), item_update.getItemValue("Value")
    #print("{Public_PUI:<19}: Category{Category:>6} - Description {Description:<8}"
    #      .format(**item_update["values"]))


statuses = {0:"Overridden",1:"Missing",2:"Dead",3:"Off-Scale High",4:"Off-Scale Low",5:"Out of Limit High",6:"Out of Limit Low",7:"Out of Calibration",8:"Overscaling",9:"Static",10:"SSME Controller",11:"SSME EIU",12:"Flight Critical MDM",13:"Payload MDM",14:"OI MDM",15:"OI DSC",16:"Lower Limit",17:"Upper Limit",18:"Event Limit",19:"Selmon Aggregate Measure",20:"Truncated",21:"User-Defined",22:"User-Defined",23:"User-Defined",24:"Default"}

# Subscription('MERGE', 'TIME_000001', ['TimeStamp','Status']);
'''
subStatus = Subscription(
    mode="MERGE",
    items=["TIME_000001"],
    fields=["TimeStamp","Status.Class"],
    adapter="") 
'''

def on_sub_update(item_update):
    #print item_update
    today = datetime.datetime.now()
    dayOfYear = (today - datetime.datetime(today.year, 1, 1)).days + 1
    timestampnow = dayOfYear*24 + today.hour + today.minute/60 + today.second/3600 
    item_name = item_update["name"]
    status = item_update["values"]["Status.Class"]
    #print "** STATUS:",status
    AOStimestamp = float( item_update["values"]["TimeStamp"] )
    difference = timestampnow - AOStimestamp
    if status == "24" :
       #print ">>> Signal Acquired"
       x = 1 #dummy
    else :
         print ">>> Signal Lost",status,statuses[status]
    if (difference > 0.00153680542553047) :
       print ">>> Stale Signal",status,statuses[status]  
    


# Adding the "on_item_update" function to Subscription
subscription.addlistener(on_item_update)

# not sure if this is a good idea subscribing twice
#subStatus.addlistener(on_sub_update)

# Registering the Subscription
#substatus_key = lightstreamer_client.subscribe(subStatus)
sub_key = lightstreamer_client.subscribe(subscription)


wait_for_input()

# Unsubscribing from Lightstreamer by using the subscription key
lightstreamer_client.unsubscribe(sub_key)
#lightstreamer_client.unsubscribe(substatus_key)

# Disconnecting
lightstreamer_client.disconnect()
