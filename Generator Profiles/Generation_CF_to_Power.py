# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 14:44:26 2018

@author: uoa-student2
"""

import pandas as pd
import numpy as np


# Create paths
path = r'C:\Users\uoa-student2\Desktop\Felipe Goncalves'
path1 = path + '\FlAixEnergy-Project\Google Maps\Generation_Geocode.xlsx'
path2 = path + '\FlAixEnergy-Project\pandapower\Generator_Profiles_Normalized.xlsx'

# Import files
file1 = pd.read_excel(path1)
file2 = pd.read_excel(path2, [0,1,2,3,4,5,6,7])

# file 1
lat1 = file1.get_values()[:, 6].tolist()
lng1 = file1.get_values()[:, 7].tolist()
pwr1 = file1.get_values()[:, 8].tolist()
gen_type1 = file1.get_values()[:, 9].tolist()

# file 2
sol_s_wd = []
sol_s_we = []
sol_w_wd = []
sol_w_we = []
win_s_wd = []
win_s_we = []
win_w_wd = []
win_w_we = []

for i in range (2, len(np.transpose(file2[0]))): # Number of PVs                   1342
    sol_s_wd.append(file2[0].get_values()[:, i].tolist())
for i in range (2, len(np.transpose(file2[1]))): # Number of PVs                   1342
    sol_s_we.append(file2[1].get_values()[:, i].tolist())
for i in range (2, len(np.transpose(file2[2]))): # Number of PVs                   1342
    sol_w_wd.append(file2[2].get_values()[:, i].tolist())
for i in range (2, len(np.transpose(file2[3]))): # Number of PVs                   1342
    sol_w_we.append(file2[3].get_values()[:, i].tolist())


for i in range (2, len(np.transpose(file2[4]))): # Number of Wind Turbines         13
    win_s_wd.append(file2[4].get_values()[:, i].tolist())
for i in range (2, len(np.transpose(file2[5]))): # Number of Wind Turbines         13
    win_s_we.append(file2[5].get_values()[:, i].tolist())
for i in range (2, len(np.transpose(file2[6]))): # Number of Wind Turbines         13
    win_w_wd.append(file2[6].get_values()[:, i].tolist())
for i in range (2, len(np.transpose(file2[7]))): # Number of Wind Turbines         13
    win_w_we.append(file2[7].get_values()[:, i].tolist())


# Multiply CFs by the corresponding generator's Rated Power
for page in range (0, 8):
    for gen in file1.index.tolist():
        for ids in file2[page].transpose().index[2:]:
            if int(ids[4:]) == gen:
                file2[page][ids] = 0
file2[7]['id: 180'] = file2[7]['id: 180']*1500





#output = np.zeros((1342*96+13*96, 1))
#count = 0
#for page in [0, 4]:
#    for ids in file2[page].transpose().index[2:]:
#        for iterator in range (count, count+96):
#            output[iterator] = file2[page][ids][iterator % 96]
#        count += 96

#file2[7]['id: 180'] = file2[7]['id: 180']*1500
#output = list()
#count = 0
#for page in [0, 4]:
#    for ids in file2[page].transpose().index[2:]:
#        output.append('gen_'+str(ids[4:]))
#        count += 1
        
      
        
        
        
        
        
        