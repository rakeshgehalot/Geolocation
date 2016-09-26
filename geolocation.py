#!/usr/bin/env python 
from urllib2 import urlopen
from contextlib import closing
import json
import random

# Automatically geolocate the connecting IP
url = 'http://freegeoip.net/json/'
try:
    with closing(urlopen(url)) as response:
        location = json.loads(response.read())
        loc =location['city'].encode('utf-8') + ' ' + location['region_name'].encode('utf-8')+ ' ' + location['ip'].encode('utf-8') + ' ' + location['country_name'].encode('utf-8')+ ' '+loc2  = location['longitude'], location['latitude']
				loc3 = loc , loc2
        print "location: ", loc3    
except:
    print("Location could not be determined automatically")
