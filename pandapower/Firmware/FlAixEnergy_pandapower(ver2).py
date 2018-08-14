# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 14:46:01 2018

@author: uoa-student2
"""

import plotly
import numpy as np
import datetime as dt
import pandas as pd
import pandapower as pp
from pandapower.plotting.plotly import get_plotly_color_palette
import pandapower.plotting.plotly as pplotly
from pandapower.plotting.plotly.mapbox_plot import set_mapbox_token
import geopy.distance as gd

LOAD_PWR = 1023.452         # Average Load per MV/LV trafo at 00:15 time in an average day of the year

set_mapbox_token('pk.eyJ1IjoiZmFnb25jYWwiLCJhIjoiY2ppZzBvd3M1MDlsMTNrbjFycW51MThrNSJ9.QZS-9tcaUaoFzPhfeAfNqw')
plotly.tools.set_credentials_file(username='fagoncal', api_key='WDyaQUbd9y0clzpoaEzs')

path = r'C:\Users\uoa-student2\Desktop\Felipe Goncalves'
path1 = path + '\FlAixEnergy-Project\Google Maps\Generation_Geocode.xlsx'
path2 = path + '\FlAixEnergy-Project\Load Profiles\Household Profiles\Copy of AC Knoten OpenGridMap Christoph.xlsm'
path3 = path + '\FlAixEnergy-Project\OpenGridMap\Copy of AC Knoten OpenGridMap Gonca.xlsm'
path4 = path + '\Generation_Profiles.xlsx'

file1 = pd.read_excel(path1)
file2 = pd.read_excel(path2, [0,1,2,3,4])
file3 = pd.read_excel(path3, [0,1,2])
file4 = pd.read_excel(path4, [0,1])

# file 1
lat1 = file1.get_values()[:, 6].tolist()
lng1 = file1.get_values()[:, 7].tolist()
pwr1 = file1.get_values()[:, 8].tolist()
gen_type1 = file1.get_values()[:, 9].tolist()

# file 2
id2 = file2[2].get_values()[:, 0].tolist()
lat2 = file2[2].get_values()[:, 5].tolist()
lng = file2[2].get_values()[:, 7].tolist()
weight = file2[2].get_values()[:, 14].tolist()

# file 3
id3_1 = file3[1].get_values()[:, 0].tolist()
lat3_1 = file3[1].get_values()[:, 5].tolist()
lng3_1 = file3[1].get_values()[:, 7].tolist()
id3_2 = file3[2].get_values()[:, 0].tolist()
lat3_2 = file3[2].get_values()[:, 5].tolist()
lng3_2 = file3[2].get_values()[:, 7].tolist()

# file 4
time = file4[0].get_values()[:, 0].tolist()
pv = []
wind = []
for i in range (0, len(np.transpose(file4[0]))): # Number of PVs                   1342
    pv.append(file4[0].get_values()[:, i].tolist())
for i in range (0, len(np.transpose(file4[1]))): # Number of Wind Turbines         13
    wind.append(file4[1].get_values()[:, i].tolist())


# Create the Pandapower network called 'Net 1'
net = pp.create_empty_network(name='Net 1', f_hz=50.)


count = 0

for i in range (0, len(file1)):
    x = lat1[i]
    y = lng1[i]
    if (gen_type1[i] == 'SOL' or gen_type1[i] == 'WIN') and (file1['Ort'][i] == 'Aachen'):
        pp.create_bus(net, index=count, vn_kv=10., name='bus_'+str(count),
                      geodata=(x, y))
        pp.create_gen(net, index=count, bus=count, p_kw=pwr1[i], 
                      name='gen_'+str(count), scaling=1., type="async")                                 # create generators
        count += 1

check1 = count - 1
trafo_id = []

for i in range (0, len(file3[1])):
    x = lat3_1[i]
    y = lng3_1[i]
    if (file1['Ort'][i] == 'Aachen'):
        pp.create_bus(net, index=count, vn_kv=110., name='bus_'+str(count),
                      geodata=(x, y))                                                                   # create external grid
        pp.create_bus(net, index=id3_1[i], vn_kv=10., name='bus_'+str(id3_1[i]),
                      geodata=(x, y-0.00007))                                                           # create HV / MV trafo
        pp.create_ext_grid(net, bus=count, name='ext_grid_'+str(count))
        pp.create_transformer(net, hv_bus=count, lv_bus=id3_1[i], 
                              std_type='25 MVA 110/10 kV')
        trafo_id.append(id3_1[i])
        count += 1

busbar_id = []
check2 = count - 1
iterator = 0

for i in range (0, len(file3[2])):
    x = lat3_2[i]
    y = lng3_2[i]
    
    pp.create_bus(net, index=id3_2[i], vn_kv=10., name='bus_'+str(id3_2[i]),
                  geodata=(x, y), type='b')                                                             # create busbar (MV / LV trafo)
    for u in range (0, len(file2[2])):
        if file3[2]['id:'][i] == file2[2]['id:'][u]:
            pp.create_load(net, bus=id3_2[i], name='load_'+str(id3_2[i]),
                           p_kw=weight[u]*LOAD_PWR)                                                     # create weighted household load
    for start_bus in net.trafo['lv_bus']:
        it = id3_1.index(start_bus)
        (start_x, start_y) = (lat3_1[it], lng3_1[it])
        geodata  = [(start_x, start_y), (x, y)]
        length = gd.distance(geodata[0], geodata[1]).km
        
        pp.create_line(net, from_bus=start_bus, to_bus=id3_2[i] ,
                       name='line_'+str(iterator), length_km=length,
                       std_type='94-AL1/15-ST1A 10.0', geodata=geodata)                                 # create ext grid to busbar lines  
        pp.create_switch(net, bus=start_bus, element=id3_2[i], et="b",
                         closed=False, type="CB",
                         name="switch_"+str(i))
        iterator += 1
            
    for start_bus in net.gen['bus']:
        gen_x = net.bus_geodata[0:len(net.gen['bus'])]['x'][start_bus]
        gen_y = net.bus_geodata[0:len(net.gen['bus'])]['y'][start_bus]
        (start_x, start_y) = (gen_x, gen_y)
        geodata  = [(start_x, start_y), (x, y)]
        length = gd.distance(geodata[0], geodata[1]).km
        pp.create_line(net, from_bus=start_bus, to_bus=id3_2[i] ,
                       name='line_'+str(iterator), length_km=length,
                       std_type='94-AL1/15-ST1A 10.0', geodata=geodata)                               # create busbar to generator lines 
        pp.create_switch(net, bus=start_bus, element=id3_2[i], et="b",
                         closed=False, type="CB",
                         name="switch_"+str(i))
        iterator += 1
        
    busbar_id.append(id3_2[i])
    count += 1

      
line = net.line
bus = net.bus
gen = net.gen
bus_geodata = net.bus_geodata
ext_grid = net.ext_grid
trafo = net.trafo
load = net.load
switch = net.switch

#pp.runopp(net)



bc_gen = pplotly.create_bus_trace(net,np.arange(0, check1+1, 1),size=5,color="blue", 
                                  infofunc=net.bus.name + '<br>' 
                                  + net.bus.vn_kv.astype(str) + ' kV')

bc_ext_grid = pplotly.create_bus_trace(net, np.arange(check1+1, check2+1, 1), 
                                    size=8,color="yellow", infofunc=net.bus.name 
                                    + '<br>' + net.bus.vn_kv.astype(str) + ' kV')

bc_trafo = pplotly.create_bus_trace(net,trafo['lv_bus'], 
                                    size=8,color="orange", infofunc=net.bus.name 
                                    + '<br>' + net.bus.vn_kv.astype(str) + ' kV')

bc_busbar = pplotly.create_bus_trace(net,busbar_id, size=8, color="red", 
                                     infofunc=net.bus.name + '<br>' +
                                     net.bus.vn_kv.astype(str) + ' kV')

bc = bc_gen + bc_ext_grid + bc_trafo + bc_busbar

lc = pplotly.create_line_trace(net,lines=None, color="blue", 
                               infofunc= net.line.name.astype(str) + '<br>'
                               + '110.0 kV')

tc = pplotly.create_trafo_trace(net,net.trafo.index,width=5,color="pink")

pplotly.draw_traces(bc + lc + tc, on_map = True, 
                    map_style='dark', showlegend=True, aspectratio='auto')

#pf_res_plotly(net, on_map=True)




pp.to_excel(net, filename="Aachen Net.xlsx", include_results=True)








