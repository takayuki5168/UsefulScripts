#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import urllib.parse
import urllib.request

WEATHER_URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city=%s"
CITY_CODES = {"TOKYO" : "130010"}

def main(day=0, city="TOKYO"):
    try:
        city_code = CITY_CODES[city]
        url = WEATHER_URL % city_code
        html = urllib.request.urlopen(url)
        weather_json = json.loads(html.read().decode('utf-8'))
        
        date = weather_json['forecasts'][day]['date']
        weather = weather_json['forecasts'][day]['telop']
        if weather_json['forecasts'][day]['temperature']['max'] != None:
            max_temperature = weather_json['forecasts'][day]['temperature']['max']['celsius'] + "℃"       
        else:
            max_temperature = "Unknown"            
        if weather_json['forecasts'][day]['temperature']['min'] != None:
            min_temperature = weather_json['forecasts'][day]['temperature']['min']['celsius'] + "℃"
        else:
            min_temperature = "Unknown"            

        print("天気     : {}".format(weather))
        print("最低気温 : {}".format(min_temperature))
        print("最高気温 : {}".format(max_temperature))
        
    except Exception as e:
        print ("Exception Error: ", e)
        sys.exit(1)

if __name__ == '__main__':
    main(0) # 0:today, 1:tommorow
