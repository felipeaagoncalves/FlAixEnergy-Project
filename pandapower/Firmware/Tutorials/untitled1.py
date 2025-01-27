# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:10:30 2018

@author: uoa-student2
"""

# -*- coding: utf-8 -*-

# Copyright (c) 2016-2018 by University of Kassel and Fraunhofer Institute for Energy Economics
# and Energy System Technology (IEE), Kassel. All rights reserved.


import pandas as pd

from pandapower.plotting.generic_geodata import create_generic_coordinates
from pandapower.plotting.plotly.mapbox_plot import *
from pandapower.plotting.plotly.traces import create_bus_trace, create_line_trace, \
    create_trafo_trace, draw_traces
from pandapower.run import runpp

try:
    import pplog as logging
except ImportError:
    import logging
logger = logging.getLogger(__name__)


def pf_res_plotly(net, cmap="Jet", use_line_geodata=None, on_map=False, projection=None,
                  map_style='basic', figsize=1, aspectratio='auto', line_width=2, bus_size=10,
                  filename="temp-plot.html"):
    """
    Plots a pandapower network in plotly
    using colormap for coloring lines according to line loading and buses according to voltage in p.u.
    If no geodata is available, artificial geodata is generated. For advanced plotting see the tutorial
    INPUT:
        **net** - The pandapower format network. If none is provided, mv_oberrhein() will be
        plotted as an example
    OPTIONAL:
        **respect_switches** (bool, False) - Respect switches when artificial geodata is created
        *cmap** (str, True) - name of the colormap
        *colors_dict** (dict, None) - by default 6 basic colors from default collor palette is used.
        Otherwise, user can define a dictionary in the form: voltage_kv : color
        **on_map** (bool, False) - enables using mapbox plot in plotly
        If provided geodata are not real geo-coordinates in lon/lat form, on_map will be set to False.
        **projection** (String, None) - defines a projection from which network geo-data will be transformed to
        lat-long. For each projection a string can be found at http://spatialreference.org/ref/epsg/
        **map_style** (str, 'basic') - enables using mapbox plot in plotly
            - 'streets'
            - 'bright'
            - 'light'
            - 'dark'
            - 'satellite'
        **figsize** (float, 1) - aspectratio is multiplied by it in order to get final image size
        **aspectratio** (tuple, 'auto') - when 'auto' it preserves original aspect ratio of the network geodata
        any custom aspectration can be given as a tuple, e.g. (1.2, 1)
        **line_width** (float, 1.0) - width of lines
        **bus_size** (float, 10.0) -  size of buses to plot.
        **filename** (str, "temp-plot.html") - filename / path to plot to. Should end on *.html
    """
    if 'res_bus' not in net or net.get('res_bus').shape[0] == 0:
        logger.warning('There are no Power Flow results. A Newton-Raphson power flow will be executed.')
        runpp(net)

    # create geocoord if none are available
    if 'line_geodata' not in net:
        net.line_geodata = pd.DataFrame(columns=['coords'])
    if 'bus_geodata' not in net:
        net.bus_geodata = pd.DataFrame(columns=["x", "y"])
    if len(net.line_geodata) == 0 and len(net.bus_geodata) == 0:
        logger.warning("No or insufficient geodata available --> Creating artificial coordinates." +
                       " This may take some time")
        create_generic_coordinates(net, respect_switches=True)
        if on_map == True:
            logger.warning("Map plots not available with artificial coordinates and will be disabled!")
            on_map = False

    # check if geodata are real geographycal lat/lon coordinates using geopy
    if on_map and projection is not None:
        geo_data_to_latlong(net, projection=projection)

    # ----- Buses ------
    # initializating bus trace
    idx = net.bus.index
    # hoverinfo which contains name and pf results
    precision = 3
    hoverinfo = (net.bus.loc[idx, 'name'].astype(str) + '<br>' +
                 'U = ' + net.res_bus.loc[idx, 'vm_pu'].round(precision).astype(str) + ' pu' + '<br>' +
                 'U = ' + (net.res_bus.loc[idx, 'vm_pu'].round(precision) * net.bus.loc[idx, 'vn_kv'].round(2)).astype(
                str) + ' kV' + '<br>' +
                 'ang = ' + net.res_bus.loc[idx, 'va_degree'].round(precision).astype(str) + ' deg'
                 ).tolist()
    bus_trace = create_bus_trace(net, net.bus.index, size=bus_size, infofunc=hoverinfo, cmap=cmap,
                                 cbar_title='Bus Voltage [pu]', cmin=0.9, cmax=1.1)

    # ----- Lines ------
    # if bus geodata is available, but no line geodata
    # if bus geodata is available, but no line geodata
    cmap_lines = 'jet' if cmap is 'Jet' else cmap
    if use_line_geodata is None:
        use_line_geodata = False if len(net.line_geodata) == 0 else True
    elif use_line_geodata and len(net.line_geodata) == 0:
        logger.warning("No or insufficient line geodata available --> only bus geodata will be used.")
        use_line_geodata = False
    idx = net.line.index
    # hoverinfo which contains name and pf results
    hoverinfo = (net.line.loc[idx, 'name'].astype(str) + '<br>' +
                 'I = ' + net.res_line.loc[idx, 'loading_percent'].round(precision).astype(str) + ' %' + '<br>' +
                 'I_from = ' + net.res_line.loc[idx, 'i_from_ka'].round(precision).astype(str) + ' kA' + '<br>' +
                 'I_to = ' + net.res_line.loc[idx, 'i_to_ka'].round(precision).astype(str) + ' kA' + '<br>'
                 ).tolist()
    line_traces = create_line_trace(net, use_line_geodata=use_line_geodata, respect_switches=True,
                                    width=line_width,
                                    infofunc=hoverinfo,
                                    cmap=cmap_lines,
                                    cmap_vals=net.res_line.loc[:, 'loading_percent'].values,
                                    cmin=0,
                                    cmax=100,
                                    cbar_title='Line Loading [%]')

    # ----- Trafos ------
    idx = net.trafo.index
    # hoverinfo which contains name and pf results
    hoverinfo = (net.trafo.loc[idx, 'name'].astype(str) + '<br>' +
                 'I = ' + net.res_trafo.loc[idx, 'loading_percent'].round(precision).astype(str) + ' %' + '<br>' +
                 'I_hv = ' + net.res_trafo.loc[idx, 'i_hv_ka'].round(precision).astype(str) + ' kA' + '<br>' +
                 'I_lv = ' + net.res_trafo.loc[idx, 'i_lv_ka'].round(precision).astype(str) + ' kA' + '<br>'
                 ).tolist()
    trafo_traces = create_trafo_trace(net, width=line_width * 1.5, infofunc=hoverinfo,
                                      cmap=cmap_lines, cmin=0, cmax=100)

    # ----- Ext grid ------
    # get external grid from create_bus_trace
    marker_type = 'circle' if on_map else 'square'
    ext_grid_trace = create_bus_trace(net, buses=net.ext_grid.bus,
                                      color='grey', size=bus_size * 2, trace_name='external_grid',
                                      patch_type=marker_type)

    draw_traces(line_traces + trafo_traces + ext_grid_trace + bus_trace,
                showlegend=False, aspectratio=aspectratio, on_map=on_map, map_style=map_style, figsize=figsize,
                filename=filename)
    
