# -*- coding: utf-8 -*-
"""
Created on Wed May 30 14:04:16 2018

@author: uoa-student2
"""

import pandapower as pp
from numpy import array
net = pp.create_empty_network()

b1 = pp.create_bus(net, 380)
b2 = pp.create_bus(net, 380)
b3 = pp.create_bus(net, 380)
b4 = pp.create_bus(net, 380)
b5 = pp.create_bus(net, 380)

l1 = pp.create_line(net, b1, b2, 30, "490-AL1/64-ST1A 380.0")
l2 = pp.create_line(net, b3, b4, 20, "490-AL1/64-ST1A 380.0")
l3 = pp.create_line(net, b4, b5, 20, "490-AL1/64-ST1A 380.0")

dcl1 = pp.create_dcline(net, name="dc line", from_bus=b2, to_bus=b3, p_kw=0.2e6, loss_percent=1.0, 
                  loss_kw=500, vm_from_pu=1.01, vm_to_pu=1.012, max_p_kw=1e6,
                  in_service=True)

eg1 = pp.create_ext_grid(net, b1, 1.02, max_p_kw=0.)
eg2 = pp.create_ext_grid(net, b5, 1.02, max_p_kw=0.)

l1 = pp.create_load(net, bus=b4, p_kw=800e3, controllable = False)

pp.runpp(net)

costeg0 = pp.create_polynomial_cost(net, 0, 'ext_grid', array([.1, 0]))
costeg1 = pp.create_polynomial_cost(net, 1, 'ext_grid', array([.08, 0]))
net.bus['max_vm_pu'] = 1.5
net.line['max_loading_percent'] = 1000

net.polynomial_cost.c.at[costeg0]= array([[0.08, 0]])
net.polynomial_cost.c.at[costeg1]= array([[0.1, 0]])
pp.runopp(net)





