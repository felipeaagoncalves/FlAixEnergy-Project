# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:37:56 2018

@author: uoa-student2
"""

import pandapower as pp
from numpy import array

net = pp.create_empty_network()

#create buses
bus1 = pp.create_bus(net, vn_kv=220., min_vm_pu=1.0, max_vm_pu=1.02)
bus2 = pp.create_bus(net, vn_kv=110., min_vm_pu=1.0, max_vm_pu=1.02)
bus3 = pp.create_bus(net, vn_kv=110., min_vm_pu=1.0, max_vm_pu=1.02)
bus4 = pp.create_bus(net, vn_kv=110., min_vm_pu=1.0, max_vm_pu=1.02)
bus = net.bus

#create 220/110 kV transformer
pp.create_transformer(net, bus1, bus2, std_type="100 MVA 220/110 kV", max_loading_percent=50)
trafo = net.trafo

#create 110 kV lines
pp.create_line(net, bus2, bus3, length_km=70., std_type='149-AL1/24-ST1A 110.0', max_loading_percent=50)
pp.create_line(net, bus3, bus4, length_km=50., std_type='149-AL1/24-ST1A 110.0', max_loading_percent=50)
pp.create_line(net, bus4, bus2, length_km=40., std_type='149-AL1/24-ST1A 110.0', max_loading_percent=50)
line = net.line

#create loads
pp.create_load(net, bus2, p_kw=60e3, controllable = False)
pp.create_load(net, bus3, p_kw=70e3, controllable = False)
pp.create_load(net, bus4, p_kw=10e3, controllable = False)
load = net.load

#create generators
eg = pp.create_ext_grid(net, bus1)
g0 = pp.create_gen(net, bus3, p_kw=-80e3, min_p_kw=-80e3, max_p_kw=0., vm_pu=1.01, controllable=True)
g1 = pp.create_gen(net, bus4, p_kw=-100e3, min_p_kw=-100e3, max_p_kw=0., vm_pu=1.01, controllable=True)
ext_grid = net.ext_grid
gen = net.gen

pp.create_polynomial_cost(net, 0, 'gen', array([-1e5, 0]))
pp.create_polynomial_cost(net, 1, 'gen', array([-1e5, 0]))
pp.runopp(net, verbose=True)

res_gen = net.res_gen
res_cost = net.res_cost
res_ext_grid = net.res_ext_grid
res_bus = net.res_bus
res_trafo = net.res_trafo
res_line = net.res_line



