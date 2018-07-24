# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:26:18 2018

@author: uoa-student2
"""








# Create paths
path = r'C:\Users\uoa-student2\Desktop\Felipe Goncalves'
path2 = path + '\FlAixEnergy-Project\Load Profiles\Household Profiles\Copy of AC Knoten OpenGridMap Christoph.xlsm'
path5 = path + '\Christoph\VDEW-Lastprofile-Haushalt.xls'

# Import files
file2 = pd.read_excel(path2, [0,1,2,3,4])
file5 = pd.read_excel(path5, [0,1,2,3,4])
