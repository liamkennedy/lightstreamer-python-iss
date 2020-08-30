# lightstreamer-python-iss
 Example of a python lightstreamer client to get live telemetry from the ISS
 
This work is a mashup of looking through various resources related to the lightstreamer framework and how that has been used to get live telemetry from the ISS.  
 
Most of the hard graft was done by the folks who built this https://github.com/ISS-Mimic/Mimic
 
In particular I found MOST VALUABLE the work they did to provide definitions for all the public telemetry - and especially some of the full text expansions of some of the data to make more "reading friendly" names for the results (see the Excel spreadsheet)

Most of the working examples with lightstreamer were implemeted through javascript - but what I wanted to do was handle this via a native python code base.  

I then ripped apart this https://github.com/Lightstreamer/Lightstreamer-example-StockList-client-python to help me create my own version pulling live telemetry I was interested in from the more than 300 data points published.  
 
 
