# Include file with PUI global definitions   

specialPUIs = ["USLAB000095","USLAB000096","USLAB000097","USLAB000098","USLAB000012",'USLAB000086']

# This really needs to be in a data file
#This is the full text expansion from the PUI to the "friendly name"
# Original comes from a spreadsheet provided in the mimic project on github 
PUI_NAMES = { \
'AIRLOCK000001':'Supplies power through the Umbilical Interface Assembly (UIA) to the spacesuits (EMU 1), Voltage', \
'AIRLOCK000002':'Supplies power through the Umbilical Interface Assembly (UIA) to the spacesuits (EMU 1), Current', \
'AIRLOCK000003':'Supplies power through the Umbilical Interface Assembly (UIA) to the spacesuits (EMU 2), Voltage', \
'AIRLOCK000004':'Supplies power through the Umbilical Interface Assembly (UIA) to the spacesuits (EMU 2), Current', \
'AIRLOCK000005':'In-flight Refill Unit (IRU), Voltage', \
'AIRLOCK000006':'In-flight Refill Unit (IRU), Current', \
'AIRLOCK000007':'Supplies power to the spacesuits (EVA Mobility Unit, EMU 1), Voltage', \
'AIRLOCK000008':'Supplies power to the spacesuits (EVA Mobility Unit, EMU 1), Current', \
'AIRLOCK000009':'Supplies power to the spacesuits (EVA Mobility Unit, EMU 2), Voltage', \
'AIRLOCK000010':'Supplies power to the spacesuits (EVA Mobility Unit, EMU 2), Current', \
'AIRLOCK000011':'Battery Charger Assembly (BCA) 1 Voltage', \
'AIRLOCK000012':'Battery Charger Assembly (BCA) 1 Current', \
'AIRLOCK000013':'Battery Charger Assembly (BCA) 2 Voltage', \
'AIRLOCK000014':'Battery Charger Assembly (BCA) 2 Current', \
'AIRLOCK000015':'Battery Charger Assembly (BCA) 3 Voltage', \
'AIRLOCK000016':'Battery Charger Assembly (BCA) 3 Current', \
'AIRLOCK000017':'Battery Charger Assembly (BCA) 4 Voltage', \
'AIRLOCK000018':'Battery Charger Assembly (BCA) 4 Current', \
'AIRLOCK000019':'Battery Charger Assembly (BCA) 1 Status', \
'AIRLOCK000020':'Battery Charger Assembly (BCA) 2 Status', \
'AIRLOCK000021':'Battery Charger Assembly (BCA) 3 Status', \
'AIRLOCK000022':'Battery Charger Assembly (BCA) 4 Status', \
'AIRLOCK000023':'Battery Charger Assembly (BCA) 1 Channel 1 Status', \
'AIRLOCK000024':'Battery Charger Assembly (BCA) 1 Channel 2 Status', \
'AIRLOCK000025':'Battery Charger Assembly (BCA) 1 Channel 3 Status', \
'AIRLOCK000026':'Battery Charger Assembly (BCA) 1 Channel 4 Status', \
'AIRLOCK000027':'Battery Charger Assembly (BCA) 1 Channel 5 Status', \
'AIRLOCK000028':'Battery Charger Assembly (BCA) 1 Channel 6 Status', \
'AIRLOCK000029':'Battery Charger Assembly (BCA) 2 Channel 1 Status', \
'AIRLOCK000030':'Battery Charger Assembly (BCA) 2 Channel 2 Status', \
'AIRLOCK000031':'Battery Charger Assembly (BCA) 2 Channel 3 Status', \
'AIRLOCK000032':'Battery Charger Assembly (BCA) 2 Channel 4 Status', \
'AIRLOCK000033':'Battery Charger Assembly (BCA) 2 Channel 5 Status', \
'AIRLOCK000034':'Battery Charger Assembly (BCA) 2 Channel 6 Status', \
'AIRLOCK000035':'Battery Charger Assembly (BCA) 3 Channel 1 Status', \
'AIRLOCK000036':'Battery Charger Assembly (BCA) 3 Channel 2 Status', \
'AIRLOCK000037':'Battery Charger Assembly (BCA) 3 Channel 3 Status', \
'AIRLOCK000038':'Battery Charger Assembly (BCA) 3 Channel 4 Status', \
'AIRLOCK000039':'Battery Charger Assembly (BCA) 3 Channel 5 Status', \
'AIRLOCK000040':'Battery Charger Assembly (BCA) 3 Channel 6 Status', \
'AIRLOCK000041':'Battery Charger Assembly (BCA) 4 Channel 1 Status', \
'AIRLOCK000042':'Battery Charger Assembly (BCA) 4 Channel 2 Status', \
'AIRLOCK000043':'Battery Charger Assembly (BCA) 4 Channel 3 Status', \
'AIRLOCK000044':'Battery Charger Assembly (BCA) 4 Channel 4 Status', \
'AIRLOCK000045':'Battery Charger Assembly (BCA) 4 Channel 5 Status', \
'AIRLOCK000046':'Battery Charger Assembly (BCA) 4 Channel 6 Status', \
'AIRLOCK000047':'Pumps atmosphere from Airlock into Node one during depress, voltage status.', \
'AIRLOCK000048':'Pumps atmosphere from Airlock into Node one during depress, switch status.', \
'AIRLOCK000049':'Crewlock Pressure', \
'AIRLOCK000050':'Hi P O2 Supply valve position', \
'AIRLOCK000051':'Lo P O2 Supply Valve position', \
'AIRLOCK000052':'N2 Supply Valve position', \
'AIRLOCK000053':'Airlock Air Conditioner State', \
'AIRLOCK000054':'Airlock Pressure', \
'AIRLOCK000055':'Airlock Hi P O2 Tank Pressure', \
'AIRLOCK000056':'Airlock Lo P O2 Tank Pressure', \
'AIRLOCK000057':'Airlock N2 Tank Pressure', \
'AIRLOCK000058':'Airlock Multiplexer/Demultiplexer (MDM) on-off status', \
'NODE1000001':'Node 1 Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'NODE1000002':'Node 1 Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'NODE2000001':'Coolant water quantity (Node 2), MT', \
'NODE2000002':'Coolant water quantity (Node 2), LT', \
'NODE2000003':'Node 2 Air Conditioner State', \
'NODE2000004':'Node 2 Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'NODE2000005':'Node 2 Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'NODE2000006':'Air Cooling Fluid Temp (Node 2)', \
'NODE2000007':'Avionics Cooling Fluid Temp (Node 2)', \
'NODE3000001':'Node 3 ppO2', \
'NODE3000002':'Node 3 ppN2', \
'NODE3000003':'Node 3 ppCO2', \
'NODE3000004':'Urine Processor State', \
'NODE3000005':'Urine Tank Qty', \
'NODE3000006':'Water Processor State', \
'NODE3000007':'Water Processor Step', \
'NODE3000008':'Waste Water Tank Qty', \
'NODE3000009':'Clean Water Tank Qty', \
'NODE3000010':'Oxygen Generator State', \
'NODE3000011':'O2 Production rate', \
'NODE3000012':'Avionics Cooling Fluid Temp (Node 3)', \
'NODE3000013':'Air Cooling Fluid Temp (Node 3)', \
'NODE3000014':'Hub Control Zone (HCZ) Multiplexer/Demultiplexer 2 (MDM) on-off status', \
'NODE3000015':'Node 3 Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'NODE3000016':'Hub Control Zone (HCZ) Multiplexer/Demultiplexer 1 (MDM) on-off status', \
'NODE3000017':'Coolant water quantity (Node 3)', \
'NODE3000018':'Node 3 Air Conditioner State', \
'NODE3000019':'Coolant water quantity (Node 3)', \
'NODE3000020':'Node 3 Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'P1000001':'Loop B Pump Flowrate (kg/hr)', \
'P1000002':'Loop B PM Out Press (kPa)', \
'P1000003':'Loop B PM Out Temp (deg C)', \
'P1000004':'S-Band Radio Frequency Group (RFG 2) Azimuth Gimbal Position', \
'P1000005':'S-Band Radio Frequency Group (RFG 2) Elevation Gimbal Position', \
'P1000006':'P1 Truss Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'P1000007':'S-Band Radio Frequency Group (RFG 2), on-off status', \
'P1000008':'Port Thermal Radiator (STR) Multiplexer/Demultiplexer (MDM) on-off status', \
'P1000009':'P1 Truss Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'P3000001':'P3 Truss Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'P3000002':'P3 Truss Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'P4000001':'Photovolatic Control Unit (PVCU) - Solar Array - 2A - Drive Voltage', \
'P4000002':'Photovolatic Control Unit (PVCU) - Solar Array - 2A - Drive Current', \
'P4000003':'Photovolatic Control Unit (PVCU) - Solar Array - 2A Multiplexer/Demultiplexer (MDM) 120 Volt On-Off Status', \
'P4000004':'Photovolatic Control Unit (PVCU) - Solar Array - 4A - Drive Voltage', \
'P4000005':'Photovolatic Control Unit (PVCU) - Solar Array - 4A - Drive Current', \
'P4000006':'Photovolatic Control Unit (PVCU) - Solar Array - 4A Multiplexer/Demultiplexer (MDM) 120 Volt On-Off Status', \
'P4000007':'Photovolatic Control Unit (PVCU) - Solar Array - 2A - Beta Gimble Assembly (BGA) Position (degrees)', \
'P4000008':'Photovolatic Control Unit (PVCU) - Solar Array - 4A - Beta Gimble Assembly (BGA) Position (degrees)', \
'P6000001':'Photovolatic Control Unit (PVCU) - Solar Array - 4B - Drive Voltage', \
'P6000002':'Photovolatic Control Unit (PVCU) - Solar Array - 4B - Drive Current', \
'P6000003':'Photovolatic Control Unit (PVCU) - Solar Array - 4B Multiplexer/Demultiplexer (MDM) 120 Volt On-Off Status', \
'P6000004':'Photovolatic Control Unit (PVCU) - Solar Array - 2B - Drive Voltage', \
'P6000005':'Photovolatic Control Unit (PVCU) - Solar Array - 2B - Drive Current', \
'P6000006':'Photovolatic Control Unit (PVCU) - Solar Array - 2B Multiplexer/Demultiplexer (MDM) 120 Volt On-Off Status', \
'P6000007':'Photovolatic Control Unit (PVCU) - Solar Array - 4B - Beta Gimble Assembly (BGA) Position (degrees)', \
'P6000008':'Photovolatic Control Unit (PVCU) - Solar Array - 2B - Beta Gimble Assembly (BGA) Position (degrees)', \
'RUSSEG000001':'Russian Segment Station Mode - Service Module (SM)', \
'RUSSEG000002':'First Kurs Equipment Kit Operating', \
'RUSSEG000003':'Second Kurs Equipment Kit Operating', \
'RUSSEG000004':'Service Module Kurs P1, P2 Failure - Russian Segment', \
'RUSSEG000005':'Distance from Service Module (SM) Kurs (Range)', \
'RUSSEG000006':'Rate from Service Module (SM) Kurs (Range Rate)', \
'RUSSEG000007':'Service Module (SM) Kurs-P Test Mode - Russian Segment', \
'RUSSEG000008':'Service Module (SM) Kurs-P "Capture" Signal Availability', \
'RUSSEG000009':'Service Module (SM) Kurs-P Target Acquisition Signal - Russian Segment', \
'RUSSEG000010':'Service Module (SM) Kurs-P Functional Mode Signal - Russian Segment', \
'RUSSEG000011':'Service Module (SM) Kurs-P Standby Mode - Russian Segment', \
'RUSSEG000012':'Service Module Docking Flag', \
'RUSSEG000013':'Service Module (SM) Forward Docking Port Engaged', \
'RUSSEG000014':'Service Module (SM) Aft Docking Port Engaged', \
'RUSSEG000015':'Service Module (SM) Nadir (Down-looking) Docking Port Engaged - Along Y-Axis', \
'RUSSEG000016':'Functional Cargo Block (FGB) Nadir (Down-looking) Docking Port Engaged - Along Y-Axis', \
'RUSSEG000017':'Service Module (SM) Nadir (Down-looking) Universal Docking Module (UDM) Docking Port Engaged - Along Y-Axis', \
'RUSSEG000018':'Mini Research Module (MRM) 1 Docking Port Engaged - Russian Segment', \
'RUSSEG000019':'Mini Research Module (MRM) 2 Docking Port Engaged - Russian Segment', \
'RUSSEG000020':'Service Module - Docked Vehicle Hooks Closed - Russian Segment', \
'RUSSEG000021':'Service Module - Russian Guidance, Navigation, and Control - Active Attitude Mode - Russian Segment', \
'RUSSEG000022':'Service Module - Russian Guidance, Navigation, and Control - Motion Control - Russian Segment', \
'RUSSEG000023':'Service Module - Russian Guidance, Navigation, and Control - Prepared to Free Drift Mode Transition - Russian Segment', \
'RUSSEG000024':'Service Module - Russian Guidance, Navigation, and Control - Thruster Operation Mode Terminated - Russian Segment', \
'RUSSEG000025':'Service Module - Russian Guidance, Navigation, and Control - Current Dynamic Mode - Russian Segment', \
'S0000001':'Starboard Thermal Radiator Rotating Joint (TRRJ) Position (degrees)', \
'S0000002':'Port Thermal Radiator Rotating Joint (TRRJ) Position (degrees)', \
'S0000003':'Solar Alpha Rotary Joint (SARJ) Starboard Joint Angle Position (degrees)', \
'S0000004':'Solar Alpha Rotary Joint (SARJ) Port Joint Angle Position (degrees)', \
'S0000005':'Solar Alpha Rotary Joint (SARJ) Port Joint Angle Commanded Position (degrees)', \
'S0000006':'External Thermal Control System (ETCS) - Thermal Radiator Rotating Joint (TRRJ) - Loop B - Software mode', \
'S0000007':'External Thermal Control System (ETCS) - Thermal Radiator Rotating Joint (TRRJ) - Loop A - Software mode', \
'S0000008':'External Primary Solar Alpha Rotary Joint (SARJ) Port Mode', \
'S0000009':'External Primary Solar Alpha Rotary Joint (SARJ) Starboard Mode', \
'S0000010':'External Control Zone Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'S0000011':'S0 Truss Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'S0000012':'External Control Zone Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'S0000013':'S0 Truss Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'S1000001':'Loop A Pump Flowrate (kg/hr)', \
'S1000002':'Loop A PM Out Press (kPa)', \
'S1000003':'Loop A PM Out Temp (deg C)', \
'S1000004':'S-Band Radio Frequency Group (RFG 1) Azimuth Gimbal Position', \
'S1000005':'S-Band Radio Frequency Group (RFG 1) Elevation Gimbal Position', \
'S1000006':'Starboard Thermal Radiator (STR) Multiplexer/Demultiplexer (MDM) on-off status', \
'S1000007':'S1 Truss Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'S1000008':'S1 Truss Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'S1000009':'S-Band Radio Frequency Group (RFG 1), on-off status', \
'S3000001':'S3 Truss Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'S3000002':'S3 Truss Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'S4000001':'Photovolatic Control Unit (PVCU) - Solar Array - 1A - Drive Voltage', \
'S4000002':'Photovolatic Control Unit (PVCU) - Solar Array - 1A - Drive Current', \
'S4000003':'Photovolatic Control Unit (PVCU) - Solar Array - 1A Multiplexer/Demultiplexer (MDM) 120 Volt On-Off Status', \
'S4000004':'Photovolatic Control Unit (PVCU) - Solar Array - 3B - Drive Voltage', \
'S4000005':'Photovolatic Control Unit (PVCU) - Solar Array - 3B - Drive Current', \
'S4000006':'Photovolatic Control Unit (PVCU) - Solar Array - 3A Multiplexer/Demultiplexer (MDM) 120 Volt On-Off Status', \
'S4000007':'Photovolatic Control Unit (PVCU) - Solar Array - 1A - Beta Gimble Assembly (BGA) Position (degrees)', \
'S4000008':'Photovolatic Control Unit (PVCU) - Solar Array - 3A - Beta Gimble Assembly (BGA) Position (degrees)', \
'S6000001':'Photovolatic Control Unit (PVCU) - Solar Array - 3B - Drive Voltage', \
'S6000002':'Photovolatic Control Unit (PVCU) - Solar Array - 3B - Drive Current', \
'S6000003':'Photovolatic Control Unit (PVCU) - Solar Array - 3B Multiplexer/Demultiplexer (MDM) 120 Volt On-Off Status', \
'S6000004':'Photovolatic Control Unit (PVCU) - Solar Array - 1B - Drive Voltage', \
'S6000005':'Photovolatic Control Unit (PVCU) - Solar Array - 1B - Drive Current', \
'S6000006':'Photovolatic Control Unit (PVCU) - Solar Array - 1B Multiplexer/Demultiplexer (MDM) 120 Volt On-Off Status', \
'S6000007':'Photovolatic Control Unit (PVCU) - Solar Array - 3B - Beta Gimble Assembly (BGA) Position (degrees)', \
'S6000008':'Photovolatic Control Unit (PVCU) - Solar Array - 1B - Beta Gimble Assembly (BGA) Position (degrees)', \
'TIME_000001':'Greenwich Mean Time (GMT)', \
'TIME_000002':'Year', \
'USLAB000001':'Control Moment Gyroscope (CMG)-1 On-Line', \
'USLAB000002':'Control Moment Gyroscope (CMG)-2 On-Line', \
'USLAB000003':'Control Moment Gyroscope (CMG)-3 On-Line', \
'USLAB000004':'Control Moment Gyroscope (CMG)-4 On-Line', \
'USLAB000005':'Number of Control Moment Gyroscope (CMG)s Online', \
'USLAB000006':'Control Moment Gyroscope (CMG) Control Torque - Roll (N-m)', \
'USLAB000007':'Control Moment Gyroscope (CMG) Control Torque - Pitch (N-m)', \
'USLAB000008':'Control Moment Gyroscope (CMG) Control Torque - Yaw (N-m)', \
'USLAB000009':'Active Control Moment Gyroscope (CMG) Momentum (Nms)', \
'USLAB000010':'Control Moment Gyroscope (CMG) Momentum Percentage (%)', \
'USLAB000011':'Desaturation Request (Enabled/Inhibited)', \
'USLAB000012':'US Guidance, Navigation and Control (GNC) Mode', \
'USLAB000013':'US Attitude Source', \
'USLAB000014':'US Rate Source', \
'USLAB000015':'US State Vector Source', \
'USLAB000016':'Attitude Controller Type', \
'USLAB000017':'Attitude Control Reference Frame', \
'USLAB000018':'US Current Local Vertical Local Horizontal (LVLH) Attitude Quaternion Component 0', \
'USLAB000019':'US Current Local Vertical Local Horizontal (LVLH) Attitude Quaternion Component 1', \
'USLAB000020':'US Current Local Vertical Local Horizontal (LVLH) Attitude Quaternion Component 2', \
'USLAB000021':'US Current Local Vertical Local Horizontal (LVLH) Attitude Quaternion Component 3', \
'USLAB000022':'US Attitude Roll Error (deg)', \
'USLAB000023':'US Attitude Pitch Error (deg)', \
'USLAB000024':'US Attitude Yaw Error (deg)', \
'USLAB000025':'US Inertial Attitude Rate X (deg/s)', \
'USLAB000026':'US Inertial Attitude Rate Y (deg/s)', \
'USLAB000027':'US Inertial Attitude Rate Z (deg/s)', \
'USLAB000028':'US Commanded Attitude Quaternion Component 0', \
'USLAB000029':'US Commanded Attitude Quaternion Component 1', \
'USLAB000030':'US Commanded Attitude Quaternion Component 2', \
'USLAB000031':'US Commanded Attitude Quaternion Component 3', \
'USLAB000032':'US Guidance, Navigation and Control (GNC) J2000 Propagated State Vector - X (km)', \
'USLAB000033':'US Guidance, Navigation and Control (GNC) J2000 Propagated State Vector - Y (km)', \
'USLAB000034':'US Guidance, Navigation and Control (GNC) J2000 Propagated State Vector - Z (km)', \
'USLAB000035':'US Guidance, Navigation and Control (GNC) J2000 Propagated State Vector - X (m/s)', \
'USLAB000036':'US Guidance, Navigation and Control (GNC) J2000 Propagated State Vector - Y (m/s)', \
'USLAB000037':'US Guidance, Navigation and Control (GNC) J2000 Propagated State Vector - Z (m/s)', \
'USLAB000038':'Active Control Moment Gyroscope (CMG) Momentum Capacity (Nms)', \
'USLAB000039':'ISS Total Mass (kg)', \
'USLAB000040':'Solar Beta Angle (degrees)', \
'USLAB000041':'Loss of CMG Attitude Control (LOAC) Caution Message In Alarm', \
'USLAB000042':'Loss of ISS Attitude Control (LOAC) Caution Message In Alarm', \
'USLAB000043':'Global Positioning System (GPS-1) Ops Status', \
'USLAB000044':'Global Positioning System (GPS-2) Ops Status', \
'USLAB000045':'Spin Motor Spin Bearing Temperature - Control Moment Gyroscope (CMG) 1 (deg C)', \
'USLAB000046':'Spin Motor Spin Bearing Temperature - Control Moment Gyroscope (CMG) 2 (deg C)', \
'USLAB000047':'Spin Motor Spin Bearing Temperature - Control Moment Gyroscope (CMG) 3 (deg C)', \
'USLAB000048':'Spin Motor Spin Bearing Temperature - Control Moment Gyroscope (CMG) 4 (deg C)', \
'USLAB000049':'Hall Resolver Spin Bearing Temperature - Control Moment Gyroscope (CMG) 1 (deg C)', \
'USLAB000050':'Hall Resolver Spin Bearing Temperature - Control Moment Gyroscope (CMG) 2 (deg C)', \
'USLAB000051':'Hall Resolver Spin Bearing Temperature - Control Moment Gyroscope (CMG) 3 (deg C)', \
'USLAB000052':'Hall Resolver Spin Bearing Temperature - Control Moment Gyroscope (CMG) 4 (deg C)', \
'USLAB000053':'Lab ppO2', \
'USLAB000054':'Lab ppN2', \
'USLAB000055':'Lab ppCO2', \
'USLAB000056':'Coolant water quantity, LT (Lab)', \
'USLAB000057':'Coolant water quantity, MT (Lab)', \
'USLAB000058':'Cabin pressure', \
'USLAB000059':'Cabin temperature', \
'USLAB000060':'Avionics Cooling Fluid Temp (Lab)', \
'USLAB000061':'Air Cooling Fluid Temp (Lab)', \
'USLAB000062':'Vacuum Resource System Valve Position', \
'USLAB000063':'Vacuum Exhaust System Valve Position', \
'USLAB000064':'Lab Port Air Conditioner State', \
'USLAB000065':'Lab Starboard Air Conditioner State', \
'USLAB000066':'Command and Control (C&C) Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'USLAB000067':'Command and Control (C&C) Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'USLAB000068':'Command and Control (C&C) Multiplexer/Demultiplexer (MDM) 3 on-off status', \
'USLAB000069':'Internal Control Zone Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'USLAB000070':'Internal Control Zone Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'USLAB000071':'Payload (PL) Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'USLAB000072':'Payload (PL) Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'USLAB000073':'Guidance, Navigation and Control (GNC) Multiplexer/Demultiplexer 1 on-off status', \
'USLAB000074':'Guidance, Navigation and Control (GNC) Multiplexer/Demultiplexer 2 on-off status', \
'USLAB000075':'Power Mangement Controller Unit (PMCU) 1 Multiplexer/Demultiplexer 1 on-off status', \
'USLAB000076':'Power Mangement Controller Unit (PMCU) 2 Multiplexer/Demultiplexer 1 on-off status', \
'USLAB000077':'US Lab Multiplexer/Demultiplexer (MDM) 1 on-off status', \
'USLAB000078':'US Lab Multiplexer/Demultiplexer (MDM) 2 on-off status', \
'USLAB000079':'US Lab Multiplexer/Demultiplexer (MDM) 3 on-off status', \
'USLAB000080':'Permanent Multipurpose Module - System Power voltage status', \
'USLAB000081':'Attitude Maneuver In Progress status', \
'USLAB000082':'Standard Command Counter - Count of standard commands received by the ISS Command and Control Computer', \
'USLAB000083':'Data Load Command Counter - Count of data load commands received by the ISS Command and Control Computer', \
'USLAB000084':'ISS Command and Control Multiplexer/Demultiplexer Onboard Time (course)', \
'USLAB000085':'ISS Command and Control Multiplexer/Demultiplexer Onboard Time (fine)', \
'USLAB000086':'ISS Station Mode', \
'USLAB000087':'# Laptops active and connected to the Primary Command and Control (C&C) Multiplexer/Demultiplexer (MDM)', \
'USLAB000088':'Ku-Band Video Downlink Channel 1 Activity', \
'USLAB000089':'Ku-Band Video Downlink Channel 2 Activity', \
'USLAB000090':'Ku-Band Video Downlink Channel 3 Activity', \
'USLAB000091':'Ku-Band Video Downlink Channel 4 Activity', \
'USLAB000092':'Active String of S-Band', \
'USLAB000093':'Internal Audio Controller (IAC) - IAC-1 Active/Backup Indication', \
'USLAB000094':'Internal Audio Controller (IAC) - IAC-2 Active/Backup Indication', \
'USLAB000095':'Video Source Routed to Downlink 1', \
'USLAB000096':'Video Source Routed to Downlink 2', \
'USLAB000097':'Video Source Routed to Downlink 3', \
'USLAB000098':'Video Source Routed to Downlink 4', \
'USLAB000099':'Space-To-Space Radio (UHF) 1 Power', \
'USLAB000100':'Space-To-Space Radio (UHF) 2 Power', \
'USLAB000101':'Space-To-Space Radio Frame Sync Lock', \
'USLAB000102':'State vector time tag', \
'USLAB000ALT':'US Altitude (km)', \
'Z1000001':'Control Moment Gyroscope (CMG)-1 Vibration (g)', \
'Z1000002':'Control Moment Gyroscope (CMG)-2 Vibration (g)', \
'Z1000003':'Control Moment Gyroscope (CMG)-3 Vibration (g)', \
'Z1000004':'Control Moment Gyroscope (CMG)-4 Vibration (g)', \
'Z1000005':'Control Moment Gyroscope (CMG)-1 Spin Motor Current (amps)', \
'Z1000006':'Control Moment Gyroscope (CMG)-2 Spin Motor Current (amps)', \
'Z1000007':'Control Moment Gyroscope (CMG)-3 Spin Motor Current (amps)', \
'Z1000008':'Control Moment Gyroscope (CMG)-4 Spin Motor Current (amps)', \
'Z1000009':'Control Moment Gyroscope (CMG) 1 Wheel Speed (rpm)', \
'Z1000010':'Control Moment Gyroscope (CMG) 2 Wheel Speed (rpm)', \
'Z1000011':'Control Moment Gyroscope (CMG) 3 Wheel Speed (rpm)', \
'Z1000012':'Control Moment Gyroscope (CMG) 4 Wheel Speed (rpm)', \
'Z1000013':'Ku-Band Transmit', \
'Z1000014':'Ku-Band SGANT Elevation Position', \
'Z1000015':'Ku-Band SGANT Cross-Elevation Position', \
'CSAMT000001':'MSS MT Position Float', \
'CSAMT000001':'MSS MT Utility Port ID (which Worksite MT is connected to, WS1 though WS8)', \
'CSASSRMS001':'MSS EDCD SSRMS Base Location', \
'CSASSRMS002':'MSS EDCD SSRMS Base Location', \
'CSASSRMS003':'MSS EDCD SSRMS Operating Base (Which LEE is Base)', \
'CSASSRMS004':'SSRMS SR Measured Joint Position', \
'CSASSRMS005':'SSRMS SY Measured Joint Position', \
'CSASSRMS006':'SSRMS SP Measured Joint Position', \
'CSASSRMS007':'SSRMS EP Measured Joint Position', \
'CSASSRMS008':'SSRMS WP Measured Joint Position', \
'CSASSRMS009':'SSRMS WY Measured Joint Position', \
'CSASSRMS010':'SSRMS WR Measured Joint Position', \
'CSASSRMS011':'MSS OCS Payload Status SSRMS Tip LEE', \
'CSASPDM0001':'MSS OCS Base Location SPDM', \
'CSASPDM0002':'MSS OCS Base Location SPDM', \
'CSASPDM0003':'MSS OCS SPDM 1 SR Measured Joint Position', \
'CSASPDM0004':'MSS OCS SPDM 1 SY Measured Joint Position', \
'CSASPDM0005':'MSS OCS SPDM 1 SP Measured Joint Position', \
'CSASPDM0006':'MSS OCS SPDM 1 EP Measured Joint Position', \
'CSASPDM0007':'MSS OCS SPDM 1 WP Measured Joint Position', \
'CSASPDM0008':'MSS OCS SPDM 1 WY Measured Joint Position', \
'CSASPDM0009':'MSS OCS SPDM 1 WR Measured Joint Position', \
'CSASPDM0010':'MSS Payload Status OCS SPDM Arm 1 OTCM', \
'CSASPDM0011':'MSS OCS SPDM 2 SR Measured Joint Position', \
'CSASPDM0012':'MSS OCS SPDM 2 SY Measured Joint Position', \
'CSASPDM0013':'MSS OCS SPDM 2 SP Measured Joint Position', \
'CSASPDM0014':'MSS OCS SPDM 2 EP Measured Joint Position', \
'CSASPDM0015':'MSS OCS SPDM 2 WP Measured Joint Position', \
'CSASPDM0016':'MSS OCS SPDM 2 WY Measured Joint Position', \
'CSASPDM0017':'MSS OCS SPDM 2 WR Measured Joint Position', \
'CSASPDM0018':'MSS Payload Status OCS SPDM Arm 2 OTCM?', \
'CSASPDM0019':'MSS Payload Status OCS SPDM Arm 2 OTCM', \
'CSASPDM0020':'MSS OCS SPDM Body Roll Joint Position', \
'CSASPDM0021':'MSS Payload Status OCS SPDM Body?', \
'CSASPDM0022':'MSS Payload Status OCS SPDM Body', \
'CSAMBS00001':'MSS OCS Payload Status MBS MCAS?', \
'CSAMBS00002':'MSS OCS Payload Status MBS MCAS', \
'CSAMBA00003':'MSS OCS Payload Status MBS POA?', \
'CSAMBA00004':'MSS OCS Payload Status MBS POA' \
}

#These are PUI's which map to a lookup list of full text names based upon the item_value
USLAB000095 = {0:" -",1:"WETA 113 (S3)",2:"S1 Upper Outboard (UPOB)",3:"SCU1 Mux",4:"S1 Lower Outboard (LOOB)",5:"JEM Channel 1",6:"JEM Channel 2",7:"S1 Upper Inboard (UPIB)",8:"S1 Lower Inboard (LOIB)",9:"Columbus 1",10:"Columbus 2",11:"P1 Upper Inboard (UPIB)",12:"SCU2 Mux",13:"Node 3 Starboard",14:"P1 Lower Inboard (LOIB)",15:"SCU1 Test",16:"WETA 112 (Node2)",17:"ORB1",18:"ORB2",19:"P1 Lower Outboard (LOOB)",20:"SCU2 Test",21:"P3 Aft",22:"Payload Rack",23:"VTR1",24:"VTR2",25:"Node 2 Nadir",26:"WETA 115 (Node1)",28:"Lab Starboard",31:"MBS POA Payload 3",32:"MBS POA",33:"SPDM S1",34:"SPDM S2",35:"MBS CLPA",36:"SPDM LEE",37:"MBS Mast",40:"SSRMS Base LEE",43:"SSRMS Base Elbow",48:"SSRMS Tip Elbow",50:"MSS Payload 3",51:"SSRMS Tip LEE",52:"Lab AVU1",53:"Lab AVU2",54:"Cup AVU1",55:"Cup AVU2",56:"SPDM OTCM 1",57:"SPDM Body 1",58:"SPDM OTCM 2",59:"SPDM Body 2",60:"SSRMS Payload 1",61:"SSRMS Payload 2",62:"SSRMS Payload 3",63:"MSS Payload 1",64:"MSS Payload 2",65:"Lab Rack 1D3",66:"Lab Rack 1P2",67:"Lab Rack 1P4",68:"Lab Camera",69:"Lab Rack 1O5",70:"Lab Rack 1O4",71:"Lab Rack 1O3",72:"Lab Rack 1O2",73:"Lab Rack 1O1",74:"Lab Rack 1S1",75:"Lab Rack 1S2",76:"Lab Rack 1S3",77:"Airlock Camera",78:"Lab Rack 1S4",79:"Node 1 Camera",80:"Node 3 Camera"}
USLAB000096 = {0:" -",1:"WETA 113 (S3)",2:"S1 Upper Outboard (UPOB)",3:"SCU1 Mux",4:"S1 Lower Outboard (LOOB)",5:"JEM Channel 1",6:"JEM Channel 2",7:"S1 Upper Inboard (UPIB)",8:"S1 Lower Inboard (LOIB)",9:"Columbus 1",10:"Columbus 2",11:"P1 Upper Inboard (UPIB)",12:"SCU2 Mux",13:"Node 3 Starboard",14:"P1 Lower Inboard (LOIB)",15:"SCU1 Test",16:"WETA 112 (Node2)",17:"ORB1",18:"ORB2",19:"P1 Lower Outboard (LOOB)",20:"SCU2 Test",21:"P3 Aft",22:"Payload Rack",23:"VTR1",24:"VTR2",25:"Node 2 Nadir",26:"WETA 115 (Node1)",28:"Lab Starboard",31:"MBS POA Payload 3",32:"MBS POA",33:"SPDM S1",34:"SPDM S2",35:"MBS CLPA",36:"SPDM LEE",37:"MBS Mast",40:"SSRMS Base LEE",43:"SSRMS Base Elbow",48:"SSRMS Tip Elbow",50:"MSS Payload 3",51:"SSRMS Tip LEE",52:"Lab AVU1",53:"Lab AVU2",54:"Cup AVU1",55:"Cup AVU2",56:"SPDM OTCM 1",57:"SPDM Body 1",58:"SPDM OTCM 2",59:"SPDM Body 2",60:"SSRMS Payload 1",61:"SSRMS Payload 2",62:"SSRMS Payload 3",63:"MSS Payload 1",64:"MSS Payload 2",65:"Lab Rack 1D3",66:"Lab Rack 1P2",67:"Lab Rack 1P4",68:"Lab Camera",69:"Lab Rack 1O5",70:"Lab Rack 1O4",71:"Lab Rack 1O3",72:"Lab Rack 1O2",73:"Lab Rack 1O1",74:"Lab Rack 1S1",75:"Lab Rack 1S2",76:"Lab Rack 1S3",77:"Airlock Camera",78:"Lab Rack 1S4",79:"Node 1 Camera",80:"Node 3 Camera"}
USLAB000097 = {0:" -",1:"WETA 113 (S3)",2:"S1 Upper Outboard (UPOB)",3:"SCU1 Mux",4:"S1 Lower Outboard (LOOB)",5:"JEM Channel 1",6:"JEM Channel 2",7:"S1 Upper Inboard (UPIB)",8:"S1 Lower Inboard (LOIB)",9:"Columbus 1",10:"Columbus 2",11:"P1 Upper Inboard (UPIB)",12:"SCU2 Mux",13:"Node 3 Starboard",14:"P1 Lower Inboard (LOIB)",15:"SCU1 Test",16:"WETA 112 (Node2)",17:"ORB1",18:"ORB2",19:"P1 Lower Outboard (LOOB)",20:"SCU2 Test",21:"P3 Aft",22:"Payload Rack",23:"VTR1",24:"VTR2",25:"Node 2 Nadir",26:"WETA 115 (Node1)",28:"Lab Starboard",31:"MBS POA Payload 3",32:"MBS POA",33:"SPDM S1",34:"SPDM S2",35:"MBS CLPA",36:"SPDM LEE",37:"MBS Mast",40:"SSRMS Base LEE",43:"SSRMS Base Elbow",48:"SSRMS Tip Elbow",50:"MSS Payload 3",51:"SSRMS Tip LEE",52:"Lab AVU1",53:"Lab AVU2",54:"Cup AVU1",55:"Cup AVU2",56:"SPDM OTCM 1",57:"SPDM Body 1",58:"SPDM OTCM 2",59:"SPDM Body 2",60:"SSRMS Payload 1",61:"SSRMS Payload 2",62:"SSRMS Payload 3",63:"MSS Payload 1",64:"MSS Payload 2",65:"Lab Rack 1D3",66:"Lab Rack 1P2",67:"Lab Rack 1P4",68:"Lab Camera",69:"Lab Rack 1O5",70:"Lab Rack 1O4",71:"Lab Rack 1O3",72:"Lab Rack 1O2",73:"Lab Rack 1O1",74:"Lab Rack 1S1",75:"Lab Rack 1S2",76:"Lab Rack 1S3",77:"Airlock Camera",78:"Lab Rack 1S4",79:"Node 1 Camera",80:"Node 3 Camera"}
USLAB000098 = {0:" -",1:"WETA 113 (S3)",2:"S1 Upper Outboard (UPOB)",3:"SCU1 Mux",4:"S1 Lower Outboard (LOOB)",5:"JEM Channel 1",6:"JEM Channel 2",7:"S1 Upper Inboard (UPIB)",8:"S1 Lower Inboard (LOIB)",9:"Columbus 1",10:"Columbus 2",11:"P1 Upper Inboard (UPIB)",12:"SCU2 Mux",13:"Node 3 Starboard",14:"P1 Lower Inboard (LOIB)",15:"SCU1 Test",16:"WETA 112 (Node2)",17:"ORB1",18:"ORB2",19:"P1 Lower Outboard (LOOB)",20:"SCU2 Test",21:"P3 Aft",22:"Payload Rack",23:"VTR1",24:"VTR2",25:"Node 2 Nadir",26:"WETA 115 (Node1)",28:"Lab Starboard",31:"MBS POA Payload 3",32:"MBS POA",33:"SPDM S1",34:"SPDM S2",35:"MBS CLPA",36:"SPDM LEE",37:"MBS Mast",40:"SSRMS Base LEE",43:"SSRMS Base Elbow",48:"SSRMS Tip Elbow",50:"MSS Payload 3",51:"SSRMS Tip LEE",52:"Lab AVU1",53:"Lab AVU2",54:"Cup AVU1",55:"Cup AVU2",56:"SPDM OTCM 1",57:"SPDM Body 1",58:"SPDM OTCM 2",59:"SPDM Body 2",60:"SSRMS Payload 1",61:"SSRMS Payload 2",62:"SSRMS Payload 3",63:"MSS Payload 1",64:"MSS Payload 2",65:"Lab Rack 1D3",66:"Lab Rack 1P2",67:"Lab Rack 1P4",68:"Lab Camera",69:"Lab Rack 1O5",70:"Lab Rack 1O4",71:"Lab Rack 1O3",72:"Lab Rack 1O2",73:"Lab Rack 1O1",74:"Lab Rack 1S1",75:"Lab Rack 1S2",76:"Lab Rack 1S3",77:"Airlock Camera",78:"Lab Rack 1S4",79:"Node 1 Camera",80:"Node 3 Camera"} 
USLAB000012 = {0:"Default",1:"WAIT",2:"RESERVED",3:"STANDBY",4:"CMG ATTITUDE CONTROL",5:"CMG/THRUSTER ASSIST ATTITUDE CONTROL",6:"USER DATA GENERATION",7:"FREEDRIFT"}
USLAB000086 = {1:"Standard",2:"Microgravity",4:"Reboost",8:"Proximity_Ops",16:"External_Ops",32:"Survival",64:"ASCR",127:"all_modes"}

if __name__ == '__main__':  

   #This is an example of how to USE this PUI.py code
   # from PUI import *
   
   #Simulating the evaluation of the "specialPUIs" key/value pair 
   item_name = "USLAB000095"
   item_value = u"1"
   if item_name in specialPUIs:
      # all the the PUI's listed in the specialPUI's list have a related Key/Value dict which maps their item_value to a plain text expansion" 
      print "SpecialPUI:", item_name, PUI_NAMES[item_name]
      print "   ", item_value, eval(item_name)[int(item_value.encode('ascii', 'ignore'))]
   else : 
        print "nothing"
   print 
   # This is just an axample of the full PUI name expansion to a friendly name from the given PUI code
   print "AIRLOCK000010",PUI_NAMES['AIRLOCK000010']
     
       