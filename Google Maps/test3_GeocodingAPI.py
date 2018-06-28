# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 09:31:38 2018

@author: uoa-student2
"""

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDZ4NjYxnFmUstA3Wpj6bjGLG7e9kfn1Bs')


now = datetime.now()
directions_result = gmaps.directions("Aachen, Germany",
                                     "Maastricht, Nederlands",
                                     mode="driving",
                                     avoid="ferries",
                                     departure_time=now
                                    )

print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])
print(str(directions_result[0]['legs'][0]['start_location']['lat']) + ', ' + str(directions_result[0]['legs'][0]['start_location']['lng']))
print(directions_result[0]['legs'][0]['end_location']['lat'])

