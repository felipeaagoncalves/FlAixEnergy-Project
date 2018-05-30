# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:29:25 2018

@author: uoa-student2
"""

import pandapower as pp
import pandapower.networks

net = pandapower.networks.example_simple()
net

pp.runpp(net)

net

net.res_bus

net.res_bus[net.bus.vn_kv==20.].vm_pu.min()

load_or_generation_busesload_or_  = set(net.load.bus.values) | set(net.sgen.bus.values) | set(net.gen.bus.values)
net.res_bus.vm_pu.loc[load_or_generation_buses].max()

net.res_bus
net.res_ext_grid
net.res_line
net.res_trafo
net.res_load
net.res_sgen
net.res_gen
net.res_shunt

net.ext_grid.va_degree
net.trafo.shift_degree
pp.runpp(net)
net.res_bus.va_degree
pp.runpp(net, calculate_voltage_angles=True)
pp.runpp(net, calculate_voltage_angles=True, init="dc")
net.res_bus.va_degree
pp.runpp(net, calculate_voltage_angles=True, init="results")
net.res_bus.va_degree
pp.runpp(net, trafo_model="t")
net.res_trafo
pp.runpp(net, trafo_model="pi")
net.res_trafo
pp.runpp(net, trafo_loading="current")
net.res_trafo
pp.runpp(net, trafo_loading="power")
net.res_trafo

net.gen
pp.runpp(net)
net.res_gen

