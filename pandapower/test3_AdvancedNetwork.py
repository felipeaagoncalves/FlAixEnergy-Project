# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:24:43 2018

@author: uoa-student2
"""

#import the pandapower module
import pandapower as pp
import pandas as pd

#create an empty network 
net = pp.create_empty_network()

# Double busbar
pp.create_bus(net, name='Double Busbar 1', vn_kv=380, type='b')
pp.create_bus(net, name='Double Busbar 2', vn_kv=380, type='b')
for i in range(10):
    pp.create_bus(net, name='Bus DB T%s' % i, vn_kv=380, type='n')
for i in range(1, 5):
    pp.create_bus(net, name='Bus DB %s' % i, vn_kv=380, type='n')

# Single busbar
pp.create_bus(net, name='Single Busbar', vn_kv=110, type='b')
for i in range(1, 6):
    pp.create_bus(net, name='Bus SB %s' % i, vn_kv=110, type='n')
for i in range(1, 6):
    for j in [1, 2]:
        pp.create_bus(net, name='Bus SB T%s.%s' % (i, j), vn_kv=110, type='n')

# Remaining buses
for i in range(1, 5):
    pp.create_bus(net, name='Bus HV%s' % i, vn_kv=110, type='n')

# show bustable
net.bus

hv_lines = pd.read_csv('example_advanced/hv_lines.csv', sep=';', header=0, decimal=',')
hv_lines

# create lines
for _, hv_line in hv_lines.iterrows():
        from_bus = pp.get_element_index(net, "bus", hv_line.from_bus)
        to_bus = pp.get_element_index(net, "bus", hv_line.to_bus)
        pp.create_line(net, from_bus, to_bus, length_km=hv_line.length,std_type=hv_line.std_type, name=hv_line.line_name, parallel=hv_line.parallel)

# show line table
net.line

hv_bus = pp.get_element_index(net, "bus", "Bus DB 2")
lv_bus = pp.get_element_index(net, "bus", "Bus SB 1")
pp.create_transformer_from_parameters(net, hv_bus, lv_bus, sn_kva=300000, vn_hv_kv=380, vn_lv_kv=110, vscr_percent=0.06,
                                      vsc_percent=8, pfe_kw=0, i0_percent=0, tp_pos=0, shift_degree=0, name='EHV-HV-Trafo')

net.trafo # show trafo table

hv_bus_sw = pd.read_csv('example_advanced/hv_bus_sw.csv', sep=';', header=0, decimal=',')
hv_bus_sw

# Bus-bus switches
for _, switch in hv_bus_sw.iterrows():
    from_bus = pp.get_element_index(net, "bus", switch.from_bus)
    to_bus = pp.get_element_index(net, "bus", switch.to_bus)
    pp.create_switch(net, from_bus, to_bus, et=switch.et, closed=switch.closed, type=switch.type, name=switch.bus_name)

# Bus-line switches
hv_buses = net.bus[(net.bus.vn_kv == 380) | (net.bus.vn_kv == 110)].index
hv_ls = net.line[(net.line.from_bus.isin(hv_buses)) & (net.line.to_bus.isin(hv_buses))]
for _, line in hv_ls.iterrows():
        pp.create_switch(net, line.from_bus, line.name, et='l', closed=True, type='LBS', name='Switch %s - %s' % (net.bus.name.at[line.from_bus], line['name']))
        pp.create_switch(net, line.to_bus, line.name, et='l', closed=True, type='LBS', name='Switch %s - %s' % (net.bus.name.at[line.to_bus], line['name']))

# Trafo-line switches
pp.create_switch(net, pp.get_element_index(net, "bus", 'Bus DB 2'), pp.get_element_index(net, "trafo", 'EHV-HV-Trafo'), et='t', closed=True, type='LBS', name='Switch DB2 - EHV-HV-Trafo')
pp.create_switch(net, pp.get_element_index(net, "bus", 'Bus SB 1'), pp.get_element_index(net, "trafo", 'EHV-HV-Trafo'), et='t', closed=True, type='LBS', name='Switch SB1 - EHV-HV-Trafo')

# show switch table
net.switch

pp.create_ext_grid(net, pp.get_element_index(net, "bus", 'Double Busbar 1'), vm_pu=1.03, va_degree=0, name='External grid',
                   s_sc_max_mva=10000, rx_max=0.1, rx_min=0.1)

net.ext_grid # show external grid table

hv_loads = pd.read_csv('example_advanced/hv_loads.csv', sep=';', header=0, decimal=',')
hv_loads

for _, load in hv_loads.iterrows():
    bus_idx = pp.get_element_index(net, "bus", load.bus)
    pp.create_load(net, bus_idx, p_kw=load.p, q_kvar=load.q, name=load.load_name)

# show load table
net.load

pp.create_gen(net, pp.get_element_index(net, "bus", 'Bus HV4'), vm_pu=1.03, p_kw=-100e3, name='Gas turbine')

# show generator table
net.gen

pp.create_sgen(net, pp.get_element_index(net, "bus", 'Bus SB 5'), p_kw=-20e3, q_kvar=-4e3, sn_kva=45e3, 
               type='WP', name='Wind Park')

# show static generator table
net.sgen

pp.create_shunt(net, pp.get_element_index(net, "bus", 'Bus HV1'), p_kw=0, q_kvar=-960, name='Shunt')

# show shunt table
net.shunt

# Impedance
pp.create_impedance(net, pp.get_element_index(net, "bus", 'Bus HV3'), pp.get_element_index(net, "bus", 'Bus HV1'), 
                    rft_pu=0.074873, xft_pu=0.198872, sn_kva=100000, name='Impedance')

# show impedance table
net.impedance

# xwards
pp.create_xward(net, pp.get_element_index(net, "bus", 'Bus HV3'), ps_kw=23942, qs_kvar=-12241.87, pz_kw=2814.571, 
                qz_kvar=0, r_ohm=0, x_ohm=12.18951, vm_pu=1.02616, name='XWard 1')
pp.create_xward(net, pp.get_element_index(net, "bus", 'Bus HV1'), ps_kw=3776, qs_kvar=-7769.979, pz_kw=9174.917, 
                qz_kvar=0, r_ohm=0, x_ohm=50.56217, vm_pu=1.024001, name='XWard 2')

# show xward table
net.xward

pp.create_bus(net, name='Bus MV0 20kV', vn_kv=20, type='n')
for i in range(8):
    pp.create_bus(net, name='Bus MV%s' % i, vn_kv=10, type='n')

#show only medium voltage bus table
mv_buses = net.bus[(net.bus.vn_kv == 10) | (net.bus.vn_kv == 20)]
mv_buses

mv_lines = pd.read_csv('example_advanced/mv_lines.csv', sep=';', header=0, decimal=',')
for _, mv_line in mv_lines.iterrows():
    from_bus = pp.get_element_index(net, "bus", mv_line.from_bus)
    to_bus = pp.get_element_index(net, "bus", mv_line.to_bus)
    pp.create_line(net, from_bus, to_bus, length_km=mv_line.length, std_type=mv_line.std_type, name=mv_line.line_name)

# show only medium voltage lines
net.line[net.line.from_bus.isin(mv_buses.index)]

hv_bus = pp.get_element_index(net, "bus", "Bus HV2")
mv_bus = pp.get_element_index(net, "bus", "Bus MV0 20kV")
lv_bus = pp.get_element_index(net, "bus", "Bus MV0")
pp.create_transformer3w_from_parameters(net, hv_bus, mv_bus, lv_bus, vn_hv_kv=110, vn_mv_kv=20, vn_lv_kv=10, 
                                        sn_hv_kva=40000, sn_mv_kva=15000, sn_lv_kva=25000, vsc_hv_percent=10.1, 
                                        vsc_mv_percent=10.1, vsc_lv_percent=10.1, vscr_hv_percent=0.266667, 
                                        vscr_mv_percent=0.033333, vscr_lv_percent=0.04, pfe_kw=0, i0_percent=0, 
                                        shift_mv_degree=30, shift_lv_degree=30, tp_side="hv", tp_mid=0, tp_min=-8, 
                                        tp_max=8, tp_st_percent=1.25, tp_pos=0, name='HV-MV-MV-Trafo')

# show transformer3w table
net.trafo3w

# Bus-line switches
mv_buses = net.bus[(net.bus.vn_kv == 10) | (net.bus.vn_kv == 20)].index
mv_ls = net.line[(net.line.from_bus.isin(mv_buses)) & (net.line.to_bus.isin(mv_buses))]
for _, line in mv_ls.iterrows():
        pp.create_switch(net, line.from_bus, line.name, et='l', closed=True, type='LBS', name='Switch %s - %s' % (net.bus.name.at[line.from_bus], line['name']))
        pp.create_switch(net, line.to_bus, line.name, et='l', closed=True, type='LBS', name='Switch %s - %s' % (net.bus.name.at[line.to_bus], line['name']))

# open switch
open_switch_id = net.switch[(net.switch.name == 'Switch Bus MV5 - MV Line5')].index
net.switch.closed.loc[open_switch_id] = False

#show only medium voltage switch table
net.switch[net.switch.bus.isin(mv_buses)]

mv_loads = pd.read_csv('example_advanced/mv_loads.csv', sep=';', header=0, decimal=',')
for _, load in mv_loads.iterrows():
    bus_idx = pp.get_element_index(net, "bus", load.bus)
    pp.create_load(net, bus_idx, p_kw=load.p, q_kvar=load.q, name=load.load_name)

# show only medium voltage loads
net.load[net.load.bus.isin(mv_buses)]

mv_sgens = pd.read_csv('example_advanced/mv_sgens.csv', sep=';', header=0, decimal=',')
for _, sgen in mv_sgens.iterrows():
    bus_idx = pp.get_element_index(net, "bus", sgen.bus)
    pp.create_sgen(net, bus_idx, p_kw=sgen.p, q_kvar=sgen.q, sn_kva=sgen.sn, type=sgen.type, name=sgen.sgen_name)

# show only medium voltage static generators
net.sgen[net.sgen.bus.isin(mv_buses)]

pp.create_bus(net, name='Bus LV0', vn_kv=0.4, type='n')
for i in range(1, 6):
    pp.create_bus(net, name='Bus LV1.%s' % i, vn_kv=0.4, type='m')
for i in range(1, 5):
    pp.create_bus(net, name='Bus LV2.%s' % i, vn_kv=0.4, type='m')
pp.create_bus(net, name='Bus LV2.2.1', vn_kv=0.4, type='m')
pp.create_bus(net, name='Bus LV2.2.2', vn_kv=0.4, type='m')

# show only low voltage buses
lv_buses = net.bus[net.bus.vn_kv == 0.4]
lv_buses

# create lines
lv_lines = pd.read_csv('example_advanced/lv_lines.csv', sep=';', header=0, decimal=',')
for _, lv_line in lv_lines.iterrows():
    from_bus = pp.get_element_index(net, "bus", lv_line.from_bus)
    to_bus = pp.get_element_index(net, "bus", lv_line.to_bus)
    pp.create_line(net, from_bus, to_bus, length_km=lv_line.length, std_type=lv_line.std_type, name=lv_line.line_name)

# show only low voltage lines
net.line[net.line.from_bus.isin(lv_buses.index)]

hv_bus = pp.get_element_index(net, "bus", "Bus MV4")
lv_bus = pp.get_element_index(net, "bus","Bus LV0")
pp.create_transformer_from_parameters(net, hv_bus, lv_bus, sn_kva=400, vn_hv_kv=10, vn_lv_kv=0.4, vscr_percent=1.325, vsc_percent=4, pfe_kw=0.95, i0_percent=0.2375, tp_side="hv", tp_mid=0, tp_min=-2, tp_max=2, tp_st_percent=2.5, tp_pos=0, shift_degree=150, name='MV-LV-Trafo')

#show only low voltage transformer
net.trafo[net.trafo.lv_bus.isin(lv_buses.index)]

# Bus-line switches
lv_ls = net.line[(net.line.from_bus.isin(lv_buses)) & (net.line.to_bus.isin(lv_buses))]
for _, line in lv_ls.iterrows():
        pp.create_switch(net, line.from_bus, line.name, et='l', closed=True, type='LBS', name='Switch %s - %s' % (net.bus.name.at[line.from_bus], line['name']))
        pp.create_switch(net, line.to_bus, line.name, et='l', closed=True, type='LBS', name='Switch %s - %s' % (net.bus.name.at[line.to_bus], line['name']))

# Trafo-line switches
pp.create_switch(net, pp.get_element_index(net, "bus", 'Bus MV4'), pp.get_element_index(net, "trafo", 'MV-LV-Trafo'), et='t', closed=True, type='LBS', name='Switch MV4 - MV-LV-Trafo')
pp.create_switch(net, pp.get_element_index(net, "bus", 'Bus LV0'), pp.get_element_index(net, "trafo", 'MV-LV-Trafo'), et='t', closed=True, type='LBS', name='Switch LV0 - MV-LV-Trafo')

# show only low vvoltage switches
net.switch[net.switch.bus.isin(lv_buses.index)]

lv_loads = pd.read_csv('example_advanced/lv_loads.csv', sep=';', header=0, decimal=',')
for _, load in lv_loads.iterrows():
    bus_idx = pp.get_element_index(net, "bus", load.bus)
    pp.create_load(net, bus_idx, p_kw=load.p, q_kvar=load.q, name=load.load_name)
    
# show only low voltage loads
net.load[net.load.bus.isin(lv_buses.index)]

lv_sgens = pd.read_csv('example_advanced/lv_sgens.csv', sep=';', header=0, decimal=',')
for _, sgen in lv_sgens.iterrows():
    bus_idx = pp.get_element_index(net, "bus", sgen.bus)
    pp.create_sgen(net, bus_idx, p_kw=sgen.p, q_kvar=sgen.q, sn_kva=sgen.sn, type=sgen.type, name=sgen.sgen_name)

# show only low voltage static generators
net.sgen[net.sgen.bus.isin(lv_buses.index)]

pp.runpp(net, calculate_voltage_angles=True, init="dc")
net
