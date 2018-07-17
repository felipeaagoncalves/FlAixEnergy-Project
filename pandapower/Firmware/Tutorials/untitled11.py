# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 09:40:52 2018

@author: uoa-student2
"""
###############################################################################
#import datetime
#datetime.datetime.today()
#print(datetime.datetime.today().weekday())
###############################################################################

###############################################################################
#import pandapower.plotting as plot
#import pandapower.networks as nw
#
## load example net (IEEE 9 buses)
#net = nw.mv_oberrhein()
## simple plot of net with existing geocoordinates or generated artificial geocoordinates
#plot.simple_plot(net, bus_size=0.7)
###############################################################################

###############################################################################
import matplotlib.pyplot as plt
import os
import pandapower as pp
import pandapower.plotting as plot
import pandapower.networks as nw
try:
    import seaborn
    colors = seaborn.color_palette()
except:
    colors = ["b", "g", "r", "c", "y"]
#%matplotlib inline

net = nw.mv_oberrhein()
#net = nw.create_cigre_network_mv(with_der="pv_wind")

#lc = plot.create_line_collection(net, net.line.index, color="grey", zorder=1) #create lines
#bc = plot.create_bus_collection(net, net.bus.index, size=80, color=colors[0], zorder=2) #create buses
#plot.draw_collections([lc, bc], figsize=(8,6)) # plot lines and buses

long_lines = net.line[net.line.length_km > 2.].index
lc = plot.create_line_collection(net, net.line.index, color="grey", zorder=1)
lcl = plot.create_line_collection(net, long_lines, color=(.3,1,.3), zorder=2)

pp.runpp(net)
low_voltage_buses = net.res_bus[net.res_bus.vm_pu < 0.98].index
bc = plot.create_bus_collection(net, net.bus.index, size=90, color=(.2,.2,1), zorder=10)
bch = plot.create_bus_collection(net, low_voltage_buses, size=90, color=(1,0,0), zorder=11)
plot.draw_collections([lc, lcl, bc, bch], figsize=(8,6))

im = plt.imread("")

plt.savefig('test', dpi=300)
###############################################################################

###############################################################################
#"""
#Stitch together Google Maps images from lat, long coordinates
#Based on work by heltonbiker and BenElgar
#Changes: 
#  * updated for Python 3
#  * added Google Maps API key (compliance with T&C, although can set to None)
#  * handle http request exceptions
#"""
#
#import requests
#from io import BytesIO
#from math import log, exp, tan, atan, pi, ceil
#from PIL import Image
#import sys
#
#EARTH_RADIUS = 6378137
#EQUATOR_CIRCUMFERENCE = 2 * pi * EARTH_RADIUS
#INITIAL_RESOLUTION = EQUATOR_CIRCUMFERENCE / 256.0
#ORIGIN_SHIFT = EQUATOR_CIRCUMFERENCE / 2.0
#GOOGLE_MAPS_API_KEY = 'AIzaSyDZ4NjYxnFmUstA3Wpj6bjGLG7e9kfn1Bs'  # set to 'your_API_key'
#
#def latlontopixels(lat, lon, zoom):
#    mx = (lon * ORIGIN_SHIFT) / 180.0
#    my = log(tan((90 + lat) * pi/360.0))/(pi/180.0)
#    my = (my * ORIGIN_SHIFT) /180.0
#    res = INITIAL_RESOLUTION / (2**zoom)
#    px = (mx + ORIGIN_SHIFT) / res
#    py = (my + ORIGIN_SHIFT) / res
#    return px, py
#
#def pixelstolatlon(px, py, zoom):
#    res = INITIAL_RESOLUTION / (2**zoom)
#    mx = px * res - ORIGIN_SHIFT
#    my = py * res - ORIGIN_SHIFT
#    lat = (my / ORIGIN_SHIFT) * 180.0
#    lat = 180 / pi * (2*atan(exp(lat*pi/180.0)) - pi/2.0)
#    lon = (mx / ORIGIN_SHIFT) * 180.0
#    return lat, lon
#
#
#def get_maps_image(NW_lat_long, SE_lat_long, zoom=18):
#
#  ullat, ullon = NW_lat_long
#  lrlat, lrlon = SE_lat_long
#
#  # Set some important parameters
#  scale = 1
#  maxsize = 640
#
#  # convert all these coordinates to pixels
#  ulx, uly = latlontopixels(ullat, ullon, zoom)
#  lrx, lry = latlontopixels(lrlat, lrlon, zoom)
#
#  # calculate total pixel dimensions of final image
#  dx, dy = lrx - ulx, uly - lry
#
#  # calculate rows and columns
#  cols, rows = int(ceil(dx/maxsize)), int(ceil(dy/maxsize))
#
#  # calculate pixel dimensions of each small image
#  bottom = 120
#  largura = int(ceil(dx/cols))
#  altura = int(ceil(dy/rows))
#  alturaplus = altura + bottom
#
#  # assemble the image from stitched
#  final = Image.new("RGB", (int(dx), int(dy)))
#  for x in range(cols):
#      for y in range(rows):
#          dxn = largura * (0.5 + x)
#          dyn = altura * (0.5 + y)
#          latn, lonn = pixelstolatlon(ulx + dxn, uly - dyn - bottom/2, zoom)
#          position = ','.join((str(latn), str(lonn)))
#          print(x, y, position)
#          urlparams = {'center': position,
#                        'zoom': str(zoom),
#                        'size': '%dx%d' % (largura, alturaplus),
#                        'maptype': 'satellite',
#                        'sensor': 'false',
#                        'scale': scale}
#          if GOOGLE_MAPS_API_KEY is not None:
#            urlparams['key'] = GOOGLE_MAPS_API_KEY
#
#          url = 'http://maps.google.com/maps/api/staticmap'
#          try:                  
#            response = requests.get(url, params=urlparams)
#            response.raise_for_status()
#          except requests.exceptions.RequestException as e:
#            print(e)
#            sys.exit(1)
#
#          im = Image.open(BytesIO(response.content))                  
#          final.paste(im, (int(x*largura), int(y*altura)))
#
#  return final
#
#############################################
#
#if __name__ == '__main__':
#
#  # a neighbourhood in Lajeado, Brazil:
#  NW_lat_long =  (-29.44,-52.0)
#  SE_lat_long = (-29.45,-51.98)
#
#  zoom = 18   # be careful not to get too many images!
#
#  result = get_maps_image(NW_lat_long, SE_lat_long, zoom=18)
#  result.show()





