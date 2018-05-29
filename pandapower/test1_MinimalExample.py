# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

######################################################################################
# Tutorial at:                                                                       #
# https://github.com/lthurner/pandapower/blob/master/tutorials/minimal_example.ipynb #
######################################################################################

import pandapower as pp
#create empty net
net = pp.create_empty_network(name='Net 1', f_hz=50.0, sn_kva=1000.0)

#create buses
b1 = pp.create_bus(net, vn_kv=20., name="Bus 1")
b2 = pp.create_bus(net, vn_kv=0.4, name="Bus 2")
b3 = pp.create_bus(net, vn_kv=0.4, name="Bus 3")

#create bus elements
pp.create_ext_grid(net, bus=b1, vm_pu=1.02, name="Grid Connection")
pp.create_load(net, bus=b3, p_kw=100, q_kvar=50, name="Load")

#create branch elements
tid = pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.4 MVA 20/0.4 kV",
                            name="Trafo")
pp.create_line(net, from_bus=b2, to_bus=b3, length_km=0.1, name="Line",
               std_type="NAYY 4x50 SE")
