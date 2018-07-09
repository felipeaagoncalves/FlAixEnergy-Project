# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:17:11 2018

@author: uoa-student2
"""

import requests
import pandas as pd
import time
import numpy as np
import scipy as sp
import scipy.interpolate
import matplotlib.pyplot as plt

token = '4533b9ec9d4e1447604f9dfc4d139626f52e2e45'
api_base = 'https://www.renewables.ninja/api/'
path1 = r'C:\Users\uoa-student2\Desktop\Felipe Goncalves\Forschungscampus_Flexible_Elektrische_Netze_FEN\Google Maps\Generation_Geocode.xlsx'
file1 = pd.read_excel(path1)
lat1 = file1.get_values()[:, 6].tolist()
lng1 = file1.get_values()[:, 7].tolist()
pwr1 = file1.get_values()[:, 8].tolist()
gen_type1 = file1.get_values()[:, 9].tolist()
#LAT_LOW = 50.715395
#LAT_UP = 50.949572
#LNG_LOW = 5.977154
#LNG_UP = 6.332900

s = requests.session()
# Send token header with each request
s.headers = {'Authorization': 'Token ' + token}

YEAR = '2014'
SIM = 'sarah'

sol = []
win = []
count_s = 0
count_w = 0

writer = pd.ExcelWriter('Generation_Profiles.xlsx', engine='openpyxl')


for i in range (554, len(file1)):
    x = lat1[i]
    y = lng1[i]
    pwr = pwr1[i]
    if (gen_type1[i] == 'SOL' or gen_type1[i] == 'WIN') and (file1['Ort'][i] == 'Aachen'):
            # input Renewables Ninja data request here (one for each generator).
            # note distinction between SOL and WIN.
            # focus on 2015 sarah data and save it to a Dataframe.
            # then, figure how to move from 1 hr to 15 min steps.
            # now interpolate the 1 hr steps.
            # don't forget to multiply the power rating from each generator to
            # the given Capacity Factor from Renewables Ninja.
            
            if gen_type1[i] == 'SOL':
                ##
                # PV example
                ##
                
                url = api_base + 'data/pv'
                
                args = {
                    'lat': x,
                    'lon': y,
                    'date_from': YEAR+'-01-01',
                    'date_to': YEAR+'-12-31',
                    'dataset': SIM,
                    'capacity': 1.0,
                    'system_loss': 10,
                    'tracking': 0,
                    'tilt': 35,
                    'azim': 180,
                    'format': 'json',
                    'metadata': False,
                    'raw': False
                }
                
                r = s.get(url, params=args)
                
                # Parse JSON to get a pandas.DataFrame
                pv = pd.read_json(r.text, orient='index')
                #pv.columns = ['PV']                            # for merra2
                pv.columns = [pv.columns[0], 'PV']             # for sarah
                
                t1 = np.linspace(pv.index.min().value, pv.index.max().value, 4*len(pv)-3)
                t1 = pd.to_datetime(t1)
                f = sp.interpolate.interp1d([float(np.array(pv.index)[i]) for i in range (0, len(pv.index))], np.array(pv['PV']), kind='linear')
                pv_new = f([float(np.array(t1)[i]) for i in range (0, len(t1))])
                
                
                sol.append([])
                sol[count_s].append(pd.DataFrame(data=pv_new, index=t1))
                sol[count_s].append(file1.loc[[i]])
                sol[count_s].append('id: '+str(i))
                sol[count_s][0].columns = [sol[count_s][2]]
                
#                if count_s == 0:
#                    sol[count_s][0].to_excel(writer, header=False, startcol=count_s, sheet_name='PV')
#                else:
#                    sol[count_s][0].to_excel(writer, header=False, startcol=count_s+1, index=False, sheet_name='PV')
#                writer.save()
                
                count_s += 1
            
            if gen_type1[i] == 'WIN':
                ##
                # Wind example
                ##
                
                url = api_base + 'data/wind'
                
                args = {
                    'lat': x,
                    'lon': y,
                    'date_from': YEAR+'-01-01',
                    'date_to': YEAR+'-12-31',
                    'capacity': 1.0,
                    'height': 100,
                    'turbine': 'Vestas V80 2000',
                    'format': 'json',
                    'metadata': False,
                    'raw': False
                }
                
                r = s.get(url, params=args)
                wind = pd.read_json(r.text, orient='index')
                wind.columns = ['Wind']
                
                t2 = np.linspace(wind.index.min().value, wind.index.max().value, 4*len(wind)-3)
                t2 = pd.to_datetime(t2)
                f = sp.interpolate.interp1d([float(np.array(pv.index)[i]) for i in range (0, len(pv.index))], np.array(pv['PV']), kind='linear')
                wind_new = f([float(np.array(t2)[i]) for i in range (0, len(t2))])
                
                win.append([])
                win[count_w].append(pd.DataFrame(data=wind_new, index=t2))
                win[count_w].append(file1.loc[[i]])
                win[count_w].append('id: '+str(i))
                win[count_w][0].columns = [win[count_w][2]]
                
                count_w += 1
            
            time.sleep(10)
           
#writer = pd.ExcelWriter('Generation_Profiles(1).xlsx', engine='openpyxl')
#for u in range (0, len(sol)):
#    if u == 0:
#        sol[u][0].to_excel(writer, header=sol[u][2], startcol=u, sheet_name='PV')
#    else:
#        sol[u][0].to_excel(writer, header=sol[u][2], startcol=u+1, index=False, sheet_name='PV')
#for u in range(0, len(win)):
#    if u == 0:
#        win[u][0].to_excel(writer, header=win[u][2], startcol=u, sheet_name='Wind')
#    else:
#        win[u][0].to_excel(writer, header=win[u][2], startcol=u+1, index=False, sheet_name='Wind')
#writer.save()
#writer.close()
            
            
            
            
            