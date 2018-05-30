# -*- coding: utf-8 -*-
"""
Created on Thu May 24 15:46:50 2018

@author: uoa-student2
"""

import pandapower as pp
import numpy as np
net = pp.create_empty_network()

#create buses
bus1 = pp.create_bus(net, vn_kv=220.)
bus2 = pp.create_bus(net, vn_kv=110.)
bus3 = pp.create_bus(net, vn_kv=110.)
bus4 = pp.create_bus(net, vn_kv=110.)

#create 220/110 kV transformer
trafo1 = pp.create_transformer(net, bus1, bus2, std_type="100 MVA 220/110 kV")
trafo = net.trafo

#create 110 kV lines
line1 = pp.create_line(net, bus2, bus3, length_km=70., std_type='149-AL1/24-ST1A 110.0')
line2 = pp.create_line(net, bus3, bus4, length_km=50., std_type='149-AL1/24-ST1A 110.0')
line3 = pp.create_line(net, bus4, bus2, length_km=40., std_type='149-AL1/24-ST1A 110.0')
line = net.line

#create loads
pp.create_load(net, bus2, p_kw=60e3, controllable = False)
pp.create_load(net, bus3, p_kw=70e3, controllable = False)
pp.create_load(net, bus4, p_kw=10e3, controllable = False)
load = net.load

#create generators
eg = pp.create_ext_grid(net, bus1)
g0 = pp.create_gen(net, bus3, p_kw=-80*1e3, min_p_kw=-80e3, max_p_kw=0, vm_pu=1.01, name='Generator 0', controllable=True)
g1 = pp.create_gen(net, bus4, p_kw=-100*1e3, min_p_kw=-100e3, max_p_kw=0, vm_pu=1.01, name='Generator 1', controllable=True)
ext_grid = net.ext_grid
gen = net.gen

## Loss Minimization
## We specify the same costs for the power at the external grid and all
## generators to minimize the overall power feed in. This equals an overall
## loss minimization.
costeg = pp.create_polynomial_cost(net, 0, 'ext_grid', np.array([1, 0]))
costgen1 = pp.create_polynomial_cost(net, 0, 'gen', np.array([1, 0]))
costgen2 = pp.create_polynomial_cost(net, 1, 'gen', np.array([1, 0]))
#
#pp.runopp(net, verbose=True)

# Individual Generator Costs
# Let's now assign individual costs to each generator.
net.polynomial_cost.c.at[costeg] = np.array([[0.1, 0]])
net.polynomial_cost.c.at[costgen1] = np.array([[0.15, 0]])
net.polynomial_cost.c.at[costgen2] = np.array([[0.12, 0]])

pp.runopp(net, verbose=True)
