# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:30:52 2018

@author: uoa-student2
"""

import requests
import pandas as pd

token = '4533b9ec9d4e1447604f9dfc4d139626f52e2e45'
api_base = 'https://www.renewables.ninja/api/'

s = requests.session()
# Send token header with each request
s.headers = {'Authorization': 'Token ' + token}

SIM='sarah'
YEAR='2016'


##
# PV example
##

url = api_base + 'data/pv'

args = {
    'lat': 34.125,
    'lon': 39.814,
    'date_from': '2014-01-01',
    'date_to': '2014-12-31',
    'dataset': 'sarah',
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
#pv.columns = ['PV']
#pv.plot(title='PV '+SIM+' Profile Aachen '+YEAR+'')
#plot_pv.set_xlabel("Time")
#plot_pv.set_ylabel("Capacity Factor")
#plot_pv.set_ylim(0., 1.)
#fig_pv = plot_pv.get_figure()
#fig_pv.savefig('PV_'+SIM+'_'+YEAR+'.png', dpi=300)
#
#i = pv.index.tolist()
#for u in range (0, len(i)):
#    i[u] = str(i[u])
#startid = i.index(YEAR+'-07-14 00:00:00')
#endid = i.index(YEAR+'-07-14 23:00:00')
#plot_pv = pv[startid:endid+1].plot(title='PV '+SIM+' Profile Summer Day ('+YEAR+'-07-14)')
#plot_pv.set_ylabel("Capacity Factor")
#fig_pv = plot_pv.get_figure()
#fig_pv.savefig('PV_'+SIM+'_day_'+YEAR+'.png', dpi=300)

##
# Wind example
##

url = api_base + 'data/wind'

args = {
    'lat': 34.125,
    'lon': 39.814,
    'date_from': '2014-01-01',
    'date_to': '2014-12-31',
    'capacity': 1.0,
    'height': 100,
    'turbine': 'Vestas V80 2000',
    'format': 'json',
    'metadata': False,
    'raw': False
}

r = s.get(url, params=args)
wind = pd.read_json(r.text, orient='index')