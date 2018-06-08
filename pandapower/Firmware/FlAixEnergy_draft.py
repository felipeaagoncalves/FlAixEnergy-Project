# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:25:35 2018

@author: uoa-student2
"""

#import pandapower as pp
#import numpy as np
#import pandapower.networks
#import pandas as pd
#
#net = pp.create_empty_network(name='Net 1', f_hz=50.0)

import os
import pandas as pd
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../Firmware/Auction EPEX Spot Market - Average Price.xlsx"))