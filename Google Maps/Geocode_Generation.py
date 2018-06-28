# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:29:51 2018

@author: uoa-student2
"""

import pandas
import googlemaps
import time

start_time = time.time() 

def is_valid(string):
    if '' in string:
        return True
    else:
        return False

gmaps = googlemaps.Client(key='AIzaSyDZ4NjYxnFmUstA3Wpj6bjGLG7e9kfn1Bs')

file = pandas.read_excel('../../../Resources/FG/RES geodata for Aachen/'
                         'eeg_anlagen_aachen.xlsx', sheet_name=0,  header=0)
file_nd = file.get_values()
strasse = file_nd[:, 4]
for i in range (0, len(strasse) - 1):
    if is_valid(strasse[i]):
        strasse[i] = strasse[i].replace('', '')
hausnummer = file_nd[:, 5]
ort = file_nd[:, 2]
plz = file_nd[:, 3]

geocode_result = []
lat = []
lng = []

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
for i in range (0, len(file) - 1):
    geocode_result.append(gmaps.geocode(strasse[i] + ' ' + str(hausnummer[i]) + ', ' + ort[i] + ' ' + str(plz[i])))
    lat.append(geocode_result[i][0]['geometry']['location']['lat'])
    lng.append(geocode_result[i][0]['geometry']['location']['lng'])

file['Strasse'] = strasse
file['Latitude'] = lat
file['Longitude'] = lng

#filepath = 'Generation_Geocode.xlsx'
#file.to_excel(filepath, index=False)
    
elapsed_time = time.time() - start_time
print("Elapsed {} seconds.".format(elapsed_time))