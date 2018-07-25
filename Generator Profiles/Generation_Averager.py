# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:37:37 2018

@author: uoa-student2
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# Start and end dates of Summer and Winter in 2014
START_SUMMER   = dt.datetime.strptime('2014-06-21 00:00:00', "%Y-%m-%d %H:%M:%S")
END_SUMMER     = dt.datetime.strptime('2014-09-23 23:59:59', "%Y-%m-%d %H:%M:%S")

START_WINTER13 = dt.datetime.strptime('2013-12-21 00:00:00', "%Y-%m-%d %H:%M:%S")
END_WINTER13   = dt.datetime.strptime('2014-03-20 23:59:59', "%Y-%m-%d %H:%M:%S")

START_WINTER14 = dt.datetime.strptime('2014-12-22 00:00:00', "%Y-%m-%d %H:%M:%S")
END_WINTER14   = dt.datetime.strptime('2015-03-20 23:59:59', "%Y-%m-%d %H:%M:%S")



# Create paths
path = r'C:\Users\uoa-student2\Desktop\Felipe Goncalves'
path1 = path + '\FlAixEnergy-Project\Google Maps\Generation_Geocode.xlsx'
path4 = path + '\Generation_Profiles.xlsx'

# Import files
file1 = pd.read_excel(path1)
file4 = pd.read_excel(path4, [0,1])

# file 1
lat1 = file1.get_values()[:, 6].tolist()
lng1 = file1.get_values()[:, 7].tolist()
pwr1 = file1.get_values()[:, 8].tolist()
gen_type1 = file1.get_values()[:, 9].tolist()

# file 4
pv   = []
wind = []
for i in range (0, len(np.transpose(file4[0]))): # Number of PVs                   1342
    pv.append(file4[0].get_values()[:, i].tolist())
for i in range (0, len(np.transpose(file4[1]))): # Number of Wind Turbines         13
    wind.append(file4[1].get_values()[:, i].tolist())



# Initialize np arrays to store average 15-minute-step days
no_pv    = len(file4[0].transpose())
no_win   = len(file4[1].transpose())
pv_s_wd  = np.zeros((96, no_pv))
pv_w_wd  = np.zeros((96, no_pv))
pv_s_we  = np.zeros((96, no_pv))
pv_w_we  = np.zeros((96, no_pv))
win_s_wd = np.zeros((96, no_win))
win_w_wd = np.zeros((96, no_win))
win_s_we = np.zeros((96, no_win))
win_w_we = np.zeros((96, no_win))

# Count how many instances in each average day
count_pv_s_wd  = 0
count_pv_s_we  = 0
count_pv_w_wd  = 0
count_pv_w_we  = 0
count_win_s_wd = 0
count_win_s_we = 0
count_win_w_wd = 0
count_win_w_we = 0


# PV


for col in file4[0].transpose()['2014-01-01 00:00:00'].index:

    for row in range (0, len(file4[0])):

        if file4[0].index[row].hour == 0 and file4[0].index[row].minute == 0:
        # Check if 00:00:00 of the day, then add all following 95 datapoints for the day
            
            if file4[0].index[row] >= START_SUMMER and file4[0].index[row] <= END_SUMMER:
                
                if file4[0].index[row].isoweekday() in [1,2,3,4,5]:
                # Weekday
                    for c in range (row, row + 96):
                        pv_s_wd[c % 96, file4[0].transpose().index.tolist().index(col)] +=  file4[0][col][c]
                    count_pv_s_wd += 1
    
                if file4[0].index[row].isoweekday() in [6,7]:
                # Weekend
                    for c in range (row, row + 96):
                        pv_s_we[c % 96, file4[0].transpose().index.tolist().index(col)] += file4[0][col][c]
                    count_pv_s_we += 1
                    
            if file4[0].index[row] >= START_WINTER13 and file4[0].index[row] <= END_WINTER13:
                
                if file4[0].index[row].isoweekday() in [1,2,3,4,5]:
                # Weekday
                    for c in range (row, row + 96):
                        pv_w_wd[c % 96, file4[0].transpose().index.tolist().index(col)] +=  file4[0][col][c]
                    count_pv_w_wd += 1
    
                if file4[0].index[row].isoweekday() in [6,7]:
                # Weekend
                    for c in range (row, row + 96):
                        pv_w_we[c % 96, file4[0].transpose().index.tolist().index(col)] += file4[0][col][c]
                    count_pv_w_we += 1
            
            if file4[0].index[row] >= START_WINTER14 and file4[0].index[row] <= END_WINTER14:
                
                if file4[0].index[row].isoweekday() in [1,2,3,4,5]:
                # Weekday
                    for c in range (row, row + 96):
                        pv_w_wd[c % 96, file4[0].transpose().index.tolist().index(col)] +=  file4[0][col][c]
                    count_pv_w_wd += 1
    
                if file4[0].index[row].isoweekday() in [6,7]:
                # Weekend
                    for c in range (row, row + 96):
                        pv_w_we[c % 96, file4[0].transpose().index.tolist().index(col)] += file4[0][col][c]
                    count_pv_w_we += 1

# Get the average PV profiles
pv_s_wd_avg = pv_s_wd/count_pv_s_wd
pv_s_we_avg = pv_s_we/count_pv_s_we
pv_w_wd_avg = pv_w_wd/count_pv_w_wd
pv_w_we_avg = pv_w_we/count_pv_w_we


# Wind


for col in file4[1].transpose()['2014-01-01 00:00:00'].index:

    for row in range (0, len(file4[1])):

        if file4[1].index[row].hour == 0 and file4[1].index[row].minute == 0:
        # Check if 00:00:00 of the day, then add all following 95 datapoints for the day
            
            if file4[1].index[row] >= START_SUMMER and file4[1].index[row] <= END_SUMMER:
                
                if file4[1].index[row].isoweekday() in [1,2,3,4,5]:
                # Weekday
                    for c in range (row, row + 96):
                        win_s_wd[c % 96, file4[1].transpose().index.tolist().index(col)] +=  file4[1][col][c]
                    count_win_s_wd += 1
    
                if file4[1].index[row].isoweekday() in [6,7]:
                # Weekend
                    for c in range (row, row + 96):
                        win_s_we[c % 96, file4[1].transpose().index.tolist().index(col)] += file4[1][col][c]
                    count_win_s_we += 1
                    
            if file4[1].index[row] >= START_WINTER13 and file4[1].index[row] <= END_WINTER13:
                
                if file4[1].index[row].isoweekday() in [1,2,3,4,5]:
                # Weekday
                    for c in range (row, row + 96):
                        win_w_wd[c % 96, file4[1].transpose().index.tolist().index(col)] +=  file4[1][col][c]
                    count_win_w_wd += 1
    
                if file4[1].index[row].isoweekday() in [6,7]:
                # Weekend
                    for c in range (row, row + 96):
                        win_w_we[c % 96, file4[1].transpose().index.tolist().index(col)] += file4[1][col][c]
                    count_win_w_we += 1
            
            if file4[1].index[row] >= START_WINTER14 and file4[1].index[row] <= END_WINTER14:
                
                if file4[1].index[row].isoweekday() in [1,2,3,4,5]:
                # Weekday
                    for c in range (row, row + 96):
                        win_w_wd[c % 96, file4[1].transpose().index.tolist().index(col)] +=  file4[1][col][c]
                    count_win_w_wd += 1
    
                if file4[1].index[row].isoweekday() in [6,7]:
                # Weekend
                    for c in range (row, row + 96):
                        win_w_we[c % 96, file4[1].transpose().index.tolist().index(col)] += file4[1][col][c]
                    count_win_w_we += 1

# Get the average Wind profiles
win_s_wd_avg = win_s_wd/count_win_s_wd
win_s_we_avg = win_s_we/count_win_s_we
win_w_wd_avg = win_w_wd/count_win_w_wd
win_w_we_avg = win_w_we/count_win_w_we



## Plot the results to some visualization
#plt.figure()
#plt.title('pv_wd_avg')
#plt.plot(pv_wd_avg)
#plt.figure()
#plt.title('pv_we_avg')
#plt.plot(pv_we_avg)
#plt.figure()
#plt.title('win_wd_avg')
#plt.plot(win_wd_avg)
#plt.figure()
#plt.title('win_we_avg')
#plt.plot(win_we_avg)