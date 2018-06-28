# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:01:03 2018

@author: uoa-student2
"""

import pandas
from datetime import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

summer2017 = pandas.read_excel('Summer_2017_Amprion_Day-ahead prices_201706210000_201709222359_1.xlsx', sheet_name=0,  header=0)
summer2017_array = summer2017.get_values()

summer_date = summer2017_array[:, 0]
for i in range (0, len(summer_date) - 1):
    summer_date[i] = str(summer_date[i])[5:10]
    summer_date[i] = '2017-' + summer_date[i]
    summer_date[i] = dt.strptime(summer_date[i], "%Y-%m-%d")
summer_time = summer2017_array[:, 2]
for i in range (0, len(summer_time) - 1):
    summer_date[i] = str(summer_date[i])[5:10]
    summer_date[i] = '2017-' + summer_date[i]
    summer_date[i] = dt.strptime(summer_date[i], "%Y-%m-%d")
summer_price = summer2017_array[:, 3]

winter2018 = pandas.read_excel('Winter_2017_Amprion_Day-ahead prices_201712210000_201803202359_1.xlsx', sheet_name=0,  header=0)
winter2018_array = winter2018.get_values()

winter_date = winter2018_array[:, 0]
for i in range (0, len(winter_date) - 1):
    winter_date[i] = str(winter_date[i])[5:10]
    if winter_date[i][0:1] == '12':
        winter_date[i] = '2017-' + winter_date[i]
    else:
        winter_date[i] = '2018-' + winter_date[i]
    winter_date[i] = dt.strptime(winter_date[i], "%Y-%m-%d")
winter_time = winter2018_array[:, 2]
winter_price = winter2018_array[:, 3]







plt.figure()
time = []
time_avg_swd = [0] * 24
time_avg_swe = [0] * 24
price = []
price_avg_swd = [0] * 24
price_avg_swe = [0] * 24
count = 0
day_count_swd = 0
day_count_swe = 0
for i in range (0, len(summer2017)):
    if count < 24:
        time.append(summer_time[i].hour)
        price.append(summer_price[i])
    if count == 23:
        # weekday() return the day of the week as an integer,
        # where Monday is 0 and Sunday is 6.
        if summer_date[i-23].weekday() in [0,1,2,3,4]:
            plt.plot(time, price, 'b')
            #plt.xticks(np.arange(min(time), max(time)+1, 2.0))
            #plt.xlabel("Time of day")
            #plt.ylabel("Energy Price [EUR/MWh]")
            #plt.ylim((0, 60))
            #plt.title(str(summer_date[i-23].date()))
            #plt.grid()
            time_avg_swd = [sum(x) for x in zip(time_avg_swd, time)]
            price_avg_swd = [sum(x) for x in zip(price_avg_swd, price)]
            day_count_swd += 1
        else:
            plt.plot(time, price, 'r')
            #plt.xticks(np.arange(min(time), max(time)+1, 2.0))
            #plt.xlabel("Time of day")
            #plt.ylabel("Energy Price [EUR/MWh]")
            #plt.ylim((0, 60))
            #plt.title(str(summer_date[i-23].date()))
            #plt.grid()
            time_avg_swe = [sum(x) for x in zip(time_avg_swe, time)]
            price_avg_swe = [sum(x) for x in zip(price_avg_swe, price)]
            day_count_swe += 1
    if count == 24:
        #plt.figure()
        time = []
        price = []
        count = 0
        time.append(summer_time[i].hour)
        price.append(summer_price[i])
    count += 1
plt.xticks(np.arange(min(time), max(time)+2, 2.0))
plt.xlabel("Time of day")
plt.ylabel("Energy Price [EUR/MWh]")
#plt.ylim((0, 60))
plt.title("Summer 2017 Energy Prices (SMARD)")
count_wd = 0
count_we = 0
#plt.grid()
plt.savefig('Summer 2017 Energy Prices (SMARD)', dpi=300)

time_avg_swd = [int(x / day_count_swd) for x in time_avg_swd]
price_avg_swd = [x / day_count_swd for x in price_avg_swd]
time_avg_swe = [int(x / day_count_swe) for x in time_avg_swe]
price_avg_swe = [x / day_count_swe for x in price_avg_swe]
plt.figure()
plt.plot(time_avg_swd, price_avg_swd, 'b')
plt.plot(time_avg_swe, price_avg_swe, 'r')
plt.legend(['Weekday', 'Weekend'], frameon=False, prop={'size': 8})
plt.xticks(np.arange(min(time), max(time)+2, 2.0))
plt.xlabel("Time of day")
plt.ylabel("Energy Price [EUR/MWh]")
#plt.ylim((0, 60))
plt.title("Summer 2017 Energy Price Average (SMARD)")
#plt.grid()
plt.savefig('Summer 2017 Energy Price Average (SMARD)', dpi=300)






plt.figure()
time = []
time_avg_wwd = [0] * 24
time_avg_wwe = [0] * 24
price = []
price_avg_wwd = [0] * 24
price_avg_wwe = [0] * 24
count = 0
day_count_wwd = 0
day_count_wwe = 0
for i in range (0, len(winter2018)):
    if count < 24:
        time.append(winter_time[i].hour)
        price.append(winter_price[i])
    if count == 23:
        # weekday() return the day of the week as an integer,
        # where Monday is 0 and Sunday is 6.
        if winter_date[i-23].weekday() in [0,1,2,3,4]:
            plt.plot(time, price, 'b')
            #plt.xticks(np.arange(min(time), max(time)+1, 2.0))
            #plt.xlabel("Time of day")
            #plt.ylabel("Energy Price [EUR/MWh]")
            #plt.ylim((0, 60))
            #plt.title(str(summer_date[i-23].date()))
            #plt.grid()
            time_avg_wwd = [sum(x) for x in zip(time_avg_wwd, time)]
            price_avg_wwd = [sum(x) for x in zip(price_avg_wwd, price)]
            day_count_wwd += 1
        else:
            plt.plot(time, price, 'r')
            #plt.xticks(np.arange(min(time), max(time)+1, 2.0))
            #plt.xlabel("Time of day")
            #plt.ylabel("Energy Price [EUR/MWh]")
            #plt.ylim((0, 60))
            #plt.title(str(summer_date[i-23].date()))
            #plt.grid()
            time_avg_wwe = [sum(x) for x in zip(time_avg_wwe, time)]
            price_avg_wwe = [sum(x) for x in zip(price_avg_wwe, price)]
            day_count_wwe += 1
    if count == 24:
        #plt.figure()
        time = []
        price = []
        count = 0
        time.append(winter_time[i].hour)
        price.append(winter_price[i])
    count += 1
plt.xticks(np.arange(min(time), max(time)+2, 2.0))
plt.xlabel("Time of day")
plt.ylabel("Energy Price [EUR/MWh]")
#plt.ylim((0, 60))
plt.title("Winter 2017-18 Energy Prices (SMARD)")
count_wd = 0
count_we = 0
#plt.grid()
plt.savefig('Winter 2017-18 Energy Prices (SMARD)', dpi=300)

time_avg_wwd = [int(x / day_count_wwd) for x in time_avg_wwd]
price_avg_wwd = [x / day_count_wwd for x in price_avg_wwd]
time_avg_wwe = [int(x / day_count_wwe) for x in time_avg_wwe]
price_avg_wwe = [x / day_count_wwe for x in price_avg_wwe]
plt.figure()
plt.plot(time_avg_wwd, price_avg_wwd, 'b')
plt.plot(time_avg_wwe, price_avg_wwe, 'r')
plt.legend(['Weekday', 'Weekend'], frameon=False, prop={'size': 8})
plt.xticks(np.arange(min(time), max(time)+2, 2.0))
plt.xlabel("Time of day")
plt.ylabel("Energy Price [EUR/MWh]")
#plt.ylim((0, 60))
plt.title("Winter 2017-18 Energy Price Average (SMARD)")
#plt.grid()
plt.savefig('Winter 2017-18 Energy Price Average (SMARD)', dpi=300)

plt.figure()
plt.plot(time_avg_swd, price_avg_swd, ':b')
plt.plot(time_avg_swe, price_avg_swe, ':r')
plt.plot(time_avg_wwd, price_avg_wwd, 'b')
plt.plot(time_avg_wwe, price_avg_wwe, 'r')
plt.legend(['Summer Weekday', 'Summer Weekend', 'Winter Weekday', 'Winter Weekend'], frameon=False, prop={'size': 8})
plt.xticks(np.arange(min(time), max(time)+2, 2.0))
plt.xlabel("Time of day")
plt.ylabel("Energy Price [EUR/MWh]")
plt.title("Summer - Winter Energy Price Average (SMARD)")
plt.savefig('Summer - Winter Energy Price Average (SMARD)', dpi=300)

