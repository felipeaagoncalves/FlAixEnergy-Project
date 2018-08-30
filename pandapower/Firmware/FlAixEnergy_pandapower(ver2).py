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
import time

start = time.time()
ID_SCALE = 1000
ID_SUBSTATION_DFA = 108444849
ID_SUBSTATION_STREET = 165544946
ID_SUBSTATION_STEEL = 165544946

LOAD_PWR = 1023.452         # Average Load per MV/LV trafo at 00:15 time in an
                            # average day of the year

set_mapbox_token(('pk.eyJ1IjoiZmFnb25jYWwiLCJhIjoiY2ppZzBvd3M1MDlsMTNrbjFycW5'
                  '1MThrNSJ9.QZS-9tcaUaoFzPhfeAfNqw'))
plotly.tools.set_credentials_file(username='fagoncal', 
                                  api_key='WDyaQUbd9y0clzpoaEzs')

path = r'C:\Users\uoa-student2\Desktop\Felipe Goncalves\FlAixEnergy-Project'

###############################################################################
# Paths
###############################################################################

# Load Profiles
path_auto = path + ('\Load Profiles\Industry Profiles\DFA'
                    '\DFA-Daten-Input.xlsx')
path_street = path + ('\Load Profiles\Industry Profiles\Street Scooter'
                      '\Street-Scooter-Input.xlsx')
path_steel = path + ('\Load Profiles\Industry Profiles\Steel Industry'
                     '\Steel-Industry-Input.xlsx')
path_house = path + ('\Load Profiles\Household Profiles'
                     '\Aachen-region-weighted Household Load Profiles.xlsx')

# Generator Profiles
path_gen_pwr = path + '\pandapower\Generator_Profiles_Power.xlsx'
path_gen_geo = path + '\Google Maps\Generation_Geocode.xlsx'

# Busbars / Ext Grids Profiles
path_busbar = path + '\OpenGridMap\Copy of AC Knoten OpenGridMap Gonca.xlsm'

# SMARD Energy Prices
path_price = path + ('\Energy Prices\SMARD Prices'
                     '\SMARD-Input.xlsx')

# AIMMS Results
path_aimms_swd = path + '\AIMMS\Lastfluss_results_Matrizen_Summer_Weekday.xlsx'
#path_aimms_swe = path + '\AIMMS\Lastfluss_results_Matrizen_Summer_Weekend.xlsx'
#path_aimms_wwd = path + '\AIMMS\Lastfluss_results_Matrizen_Winter_Weekday.xlsx'
#path_aimms_wwe = path + '\AIMMS\Lastfluss_results_Matrizen_Winter_Weekend.xlsx'


###############################################################################
# Files
###############################################################################

# Load Profiles
file_auto = pd.ExcelFile(path_auto)
file_street = pd.ExcelFile(path_street)
file_steel = pd.ExcelFile(path_steel)
file_house = pd.ExcelFile(path_house)

# Generator Profiles
file_gen_pwr = pd.ExcelFile(path_gen_pwr)
file_gen_geo = pd.ExcelFile(path_gen_geo)

# Busbars / Ext Grids Profiles
file_busbar = pd.ExcelFile(path_busbar)

# SMARD Energy Prices
file_price = pd.ExcelFile(path_price)

# AIMMS Results
file_aimms_swd = pd.ExcelFile(path_aimms_swd)
#file_aimms_swe = pd.ExcelFile(path_aimms_swe)
#file_aimms_wwd = pd.ExcelFile(path_aimms_wwd)
#file_aimms_wwe = pd.ExcelFile(path_aimms_wwe)


###############################################################################
# Data Frames
###############################################################################

# Load Profiles
auto = {sheet_name: file_auto.parse(sheet_name) for sheet_name in file_auto.sheet_names}
auto = auto[list(auto.keys())[0]]
auto.index = auto['Time of the day']
del auto['Time of the day']
street = {sheet_name: file_street.parse(sheet_name) for sheet_name in file_street.sheet_names}
street = street[list(street.keys())[0]]
street.index = street['Time of the day']
del street['Time of the day']
steel = {sheet_name: file_steel.parse(sheet_name) for sheet_name in file_steel.sheet_names}
steel = steel[list(steel.keys())[0]]
steel.index = steel['Time of the day']
del steel['Time of the day']
house = {sheet_name: file_house.parse(sheet_name) for sheet_name in file_house.sheet_names}
house_SWD = house[list(house.keys())[1]]
house_SWD.index = house_SWD['id:']
del house_SWD['id:']
house_SWE = house[list(house.keys())[2]]
house_SWE.index = house_SWE['id:']
del house_SWE['id:']
house_WWD = house[list(house.keys())[3]]
house_WWD.index = house_WWD['id:']
del house_WWD['id:']
house_WWE = house[list(house.keys())[4]]
house_WWE.index = house_WWE['id:']
del house_WWE['id:']

# Generator Profiles
gen_pwr = {sheet_name: file_gen_pwr.parse(sheet_name) for sheet_name in file_gen_pwr.sheet_names}
#pv_SWD = gen_pwr[list(gen_pwr.keys())[0]]
#pv_SWD.index = pv_SWD['time of the day']
#del pv_SWD['index']
#del pv_SWD['time of the day']
#pv_SWE = gen_pwr[list(gen_pwr.keys())[1]]
#pv_SWE.index = pv_SWE['time of the day']
#del pv_SWE['index']
#del pv_SWE['time of the day']
#pv_WWD = gen_pwr[list(gen_pwr.keys())[2]]
#pv_WWD.index = pv_WWD['time of the day']
#del pv_WWD['index']
#del pv_WWD['time of the day']
#pv_WWE = gen_pwr[list(gen_pwr.keys())[3]]
#pv_WWE.index = pv_WWE['time of the day']
#del pv_WWE['index']
#del pv_WWE['time of the day']
#wind_SWD = gen_pwr[list(gen_pwr.keys())[4]]
#wind_SWD.index = wind_SWD['time of the day']
#del wind_SWD['index']
#del wind_SWD['time of the day']
#wind_SWE = gen_pwr[list(gen_pwr.keys())[5]]
#wind_SWE.index = wind_SWE['time of the day']
#del wind_SWE['index']
#del wind_SWE['time of the day']
#wind_WWD = gen_pwr[list(gen_pwr.keys())[6]]
#wind_WWD.index = wind_WWD['time of the day']
#del wind_WWD['index']
#del wind_WWD['time of the day']
#wind_WWE = gen_pwr[list(gen_pwr.keys())[7]]
#wind_WWE.index = wind_WWE['time of the day']
#del wind_WWE['index']
#del wind_WWE['time of the day']
gen_geo = {sheet_name: file_gen_geo.parse(sheet_name) for sheet_name in file_gen_geo.sheet_names}
gen_geo = gen_geo[list(gen_geo.keys())[0]]

# Busbars / Ext Grids Profiles
busbar = {sheet_name: file_busbar.parse(sheet_name) for sheet_name in file_busbar.sheet_names}

# SMARD Energy Prices
price = {sheet_name: file_price.parse(sheet_name) for sheet_name in file_price.sheet_names}
price = price[list(price.keys())[0]]
price.index = price['Time of day (hr)']
del price['Index']
del price['Time of day (hr)']





for time_step in range (0, 1):
    
    for scenario in ['SWD']:
    
        # AIMMS Results + Load Profiles
        if scenario == 'SWD':
            matrix = {sheet_name: file_aimms_swd.parse(sheet_name) for sheet_name in file_aimms_swd.sheet_names}
            matrix = matrix[list(matrix.keys())[time_step + 1]]
            house_prof = house_SWD
            SCENARIO = 0
            DAY = 'Summer Weekday'
        if scenario == 'SWE':
            matrix = {sheet_name: file_aimms_swd.parse(sheet_name) for sheet_name in file_aimms_swd.sheet_names}
            matrix = matrix[list(matrix.keys())[time_step + 1]]
            house_prof = house_SWE
            SCENARIO = 1
            DAY = 'Summer Weekend'
        if scenario == 'WWD':
            matrix = {sheet_name: file_aimms_swd.parse(sheet_name) for sheet_name in file_aimms_swd.sheet_names}
            matrix = matrix[list(matrix.keys())[time_step + 1]]
            house_prof = house_WWD
            SCENARIO = 2
            DAY = 'Winter Weekday'
        if scenario == 'WWE':
            matrix = {sheet_name: file_aimms_swd.parse(sheet_name) for sheet_name in file_aimms_swd.sheet_names}
            matrix = matrix[list(matrix.keys())[time_step + 1]]
            house_prof = house_WWE
            SCENARIO = 3
            DAY = 'Winter Weekend'
        
        
        # Create the Pandapower network called 'Net 1'
        net = pp.create_empty_network(name='Net 1', f_hz=50.)
        
        
        count = 0
        for i in range (0, len(gen_geo)):
            
            x = gen_geo['Latitude'][i]
            y = gen_geo['Longitude'][i]
            if (gen_geo['Energieträger'][i] == 'SOL' or gen_geo['Energieträger'][i] == 'WIN') and (gen_geo['Ort'][i] == 'Aachen'):
                
                pp.create_bus(net, 
                              index=count, 
                              vn_kv=10., 
                              name='bus_'+str(count),
                              geodata=(x, y))
                
                if gen_geo['Energieträger'][i] == 'SOL':
                    pp.create_gen(net, 
                                  index=count,
                                  bus=count, 
                                  p_kw=gen_pwr[list(gen_pwr.keys())[SCENARIO]]['id: '+str(i)][time_step], 
                                  name='gen_'+str(count),
                                  scaling=1., 
                                  type="async")                                 # create generators
                
                if gen_geo['Energieträger'][i] == 'WIN':
                    pp.create_gen(net, 
                                  index=count,
                                  bus=count, 
                                  p_kw=gen_pwr[list(gen_pwr.keys())[SCENARIO+4]]['id: '+str(i)][time_step], 
                                  name='gen_'+str(count),
                                  scaling=1., 
                                  type="async")                                 # create generators
                count += 1
        
        check1 = count - 1
        trafo_id = []
        busbar_id = []
        for i in range (0, len(busbar['MVLV'])):
            
            x = busbar['MVLV']['lat:'][i]
            y = busbar['MVLV']['lon:'][i]
            pp.create_bus(net, 
                          index=busbar['HVMV']['id:'][i],
                          vn_kv=10.,
                          name='bus_'+str(busbar['HVMV']['id:'][i]),
                          geodata=(x, y-0.00007))                               # HV
            pp.create_bus(net, 
                          index=busbar['HVMV']['id:'][i]*ID_SCALE,
                          vn_kv=10.,
                          name='bus_'+str(busbar['HVMV']['id:'][i]*ID_SCALE),
                          geodata=(x, y),
                          type='b')                                             # LV
            busbar_id.append(busbar['HVMV']['id:'][i]*ID_SCALE)
            pp.create_transformer(net,
                                  hv_bus=busbar['HVMV']['id:'][i], 
                                  lv_bus=busbar['HVMV']['id:'][i]*ID_SCALE, 
                                  std_type='25 MVA 110/10 kV')                  # create HV / MV trafo
            trafo_id.append(busbar['HVMV']['id:'][i])
                                
        pp.create_bus(net, 
                      index=count,
                      vn_kv=110.,
                      name='bus_'+str(count),
                      geodata=(50,58007, 6,26393))                             
        pp.create_ext_grid(net, 
                           bus=count,
                           name='ext_grid_'+str(count))                         # create external grid
        check2 = count
        count += 1
              
        
        for substation in house_prof.columns:
            pp.create_load(net, 
                           bus=substation,
                           name='load_'+str(substation),
                           p_kw=house_prof[substation][time_step])              # create region-weighted household load
            
            if substation == ID_SUBSTATION_DFA:
                pp.create_load(net, 
                               bus=substation,
                               name='load_0',
                               p_kw=auto[DAY][time_step])
            if substation == ID_SUBSTATION_STREET:
                pp.create_load(net, 
                               bus=substation,
                               name='load_1',
                               p_kw=street[DAY][time_step])
            if substation == ID_SUBSTATION_STEEL:
                pp.create_load(net, 
                               bus=substation,
                               name='load_2',
                               p_kw=steel[DAY][time_step])
        
        for substation in matrix.columns:
            for generator in ma
    
              
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
#                                       infofunc= net.line.name.astype(str) + '<br>'
#                                       + '110.0 kV')
        
        tc = pplotly.create_trafo_trace(net,net.trafo.index,width=5,color="pink")
        
        pplotly.draw_traces(bc + lc + tc, on_map = True, 
                            map_style='dark', showlegend=True, aspectratio='auto')
        
        #pf_res_plotly(net, on_map=True)
        
        
        
        
        pp.to_excel(net, filename="Aachen Net.xlsx", include_results=True)
        
        
        
end = time.time()
elapsed_time = end - start
print('Elapsed time: ' + str(elapsed_time) + ' seconds.')








