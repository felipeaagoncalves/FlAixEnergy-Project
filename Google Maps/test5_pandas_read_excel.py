# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:59:56 2018

@author: uoa-student2
"""

import pandas

file = pandas.read_excel('../../../Resources/FG/RES geodata for Aachen/eeg_anlagen_aachen.xlsx', sheet_name=0,  header=0)

file2 = pandas.read_excel('../../../Resources/FG/RES geodata for Aachen/test_excel_file.xlsx', sheet_name=0,  header=0, names=['Strasse', 'Hausmummer', 'Ort', 'PLZ'])

