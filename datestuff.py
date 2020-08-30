import os
import datetime
import time

def displayValsFromEpoch( UnixTimeValue ) :
    dt =datetime.datetime.fromtimestamp(UnixTimeValue)
    print "Convert UNIXTIMESTAMP to PYTHON DATETIME and Display ALL THE VALUES" 
    print dt.strftime('%Y-%m-%d %H:%M:%S'),"Converted to a python datetime object" 
    print " Now every part of that datetime value is accessible"
    print "  Year", dt.year
    print "  Month", dt.month
    print "  Day", dt.day
    print "  Hour", dt.hour
    print "  Minute", dt.minute
    print "  Second", dt.second
    print 
    return dt
    
FileModTime = os.path.getmtime("datestuff.py") #I'm just using this actual file
print "FileModTime",FileModTime, "As a UNIX Timestamp value"

File_dt = displayValsFromEpoch ( FileModTime )

FileModEpochYear = datetime.datetime(File_dt.year, 1, 1)
print "FileModEpochYear (datetime)", FileModEpochYear
print "     which is basically a datetime object set at the beginning of THAT year"
print "SO - now convert that BACK to a UNIXTIME so we can add that HoursFromEpoch value" 

UnixFileModEpochYear = time.mktime(FileModEpochYear.timetuple()) #This is just the way to convert from datetime BACK to UnixTime
print "Epoch Year as a Unixtime:", UnixFileModEpochYear
print "FileModTime - UnixFileModEpochYear=",FileModTime-UnixFileModEpochYear, "Seconds from Jan 1", FileModEpochYear.year

HoursFromJan1AsEpoch = 6219.86763916665
print "Your Example: HoursFromJan1AsEpoch", HoursFromJan1AsEpoch
SecondsFromJan1AsEpoch = HoursFromJan1AsEpoch * 60 * 60
print "SecondsFromJan1AsEpoch", SecondsFromJan1AsEpoch


ResultingEpoch =  UnixFileModEpochYear + SecondsFromJan1AsEpoch

print "ResultingEpoch ", ResultingEpoch

print "Display All the Vals from ResultingEpoch"
displayValsFromEpoch( ResultingEpoch )

