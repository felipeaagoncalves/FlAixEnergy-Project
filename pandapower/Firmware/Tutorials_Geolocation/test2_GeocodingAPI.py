# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 09:39:11 2018

@author: uoa-student2
"""
###############################################################################
#import pandas
#from googlemaps import GoogleMaps
#import xml.etree.ElementTree as et
###############################################################################

###############################################################################
#gmaps = GoogleMaps()
#pars = et.XMLParser(encoding='utf-8')
#tree = et.parse('data.xml',parser=pars)
#root = tree.getroot()
#adress = "ringelblum 7 beer sheva"
#lat , lng = gmaps.address_to_latlng(adress)
#print(lat, lng) 
###############################################################################

###############################################################################
#file = pandas.read_csv('my_file.csv', header=0, sep=';')
###############################################################################

###############################################################################
#geo_s ='https://maps.googleapis.com/maps/api/geocode/json'
#
#param = {'address': address, 'key': 'AIzaSyDZ4NjYxnFmUstA3Wpj6bjGLG7e9kfn1Bs'}
#
#response = requests.get(geo_s, params=param)
#
#json_dict = response.json()
#
#try:
#    lat = json_dict['results'][0]['geometry']['location']['lat']
#    lng = json_dict['results'][0]['geometry']['location']['lng']
#    return {'lat': lat, 'lng': lng}
###############################################################################

locations = ["Utica", "Rio de Janeiro", "Edmonton", "Aachen"]
from geopy.geocoders import GoogleV3
geolocator = GoogleV3(api_key='AIzaSyDZ4NjYxnFmUstA3Wpj6bjGLG7e9kfn1Bs')
results = []
for location in locations:
    print (location)
    results.append(geolocator.geocode(query=location, language='en', exactly_one=False, timeout=5))
    for result in results:
        print (results)




