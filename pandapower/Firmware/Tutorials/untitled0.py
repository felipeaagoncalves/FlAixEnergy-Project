# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:49:32 2018

@author: uoa-student2
"""

#import pandapower
#from pandapower.plotting.plotly import simple_plotly
#from pandapower.plotting.plotly import pf_res_plotly
#import pandapower.networks as pn
#from pandapower.plotting.plotly.mapbox_plot import set_mapbox_token
#set_mapbox_token('pk.eyJ1IjoiZmFnb25jYWwiLCJhIjoiY2ppZzBvd3M1MDlsMTNrbjFycW51MThrNSJ9.QZS-9tcaUaoFzPhfeAfNqw')
#
##net = pn.mv_oberrhein()
#net = pn.create_cigre_network_mv(with_der="pv_wind")
##simple_plotly(net, on_map=True)
##pf_res_plotly(net, on_map=True, projection='epsg:31467', map_style='dark')
#pandapower.plotting.plotly.geo_data_to_latlong(net, projection='epsg:31467')
#pf_res_plotly(net, on_map=True, projection='epsg:31467')

#from pandapower.plotting.plotly import get_plotly_color_palette
#import pandapower as pp
#import pandapower.networks as nw
#import pandapower.plotting.plotly as pplotly
#
#net = nw.mv_oberrhein()
#
#mg = pp.topology.create_nxgraph(net, nogobuses=set(net.trafo.lv_bus.values) | set(net.trafo.hv_bus.values))
#collections = []
#ai = 0
#islands = list(pp.topology.connected_components(mg)) # getting connected components of a graph
#colors = get_plotly_color_palette(len(islands)) # getting a color for each connected component
#for color, area in zip(colors, islands):
#    collections += pplotly.create_bus_trace(net, area, size=5, color=color, trace_name='feeder {0}'.format(ai))
#    ai += 1
#collections += pplotly.create_line_trace(net, net.line.index, color="grey")
#collections += pplotly.create_bus_trace(net, net.ext_grid.bus.values, patch_type="square", size=10,
#                                              color="yellow")
#pplotly.draw_traces(collections)
#
#net = nw.mv_oberrhein()
#pplotly.geo_data_to_latlong(net, projection='epsg:31467') #transforming geodata to lat/long
#
#lc = pplotly.create_line_trace(net,net.line.index, color='purple')
#bc = pplotly.create_bus_trace(net,net.bus.index,size=10,color="orange",
#                                       infofunc=net.bus.name + '<br>' + net.bus.vn_kv.astype(str) + ' kV')
#
#pplotly.draw_traces(bc + lc, on_map = True, map_style='dark')



#import plotly.plotly as py
#import pandas as pd
#
#df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
#df_airports.head()
#
#df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
#df_flight_paths.head()
#
#airports = [ dict(
#        type = 'scattergeo',
#        locationmode = 'USA-states',
#        lon = df_airports['long'],
#        lat = df_airports['lat'],
#        hoverinfo = 'text',
#        text = df_airports['airport'],
#        mode = 'markers',
#        marker = dict( 
#            size=2, 
#            color='rgb(255, 0, 0)',
#            line = dict(
#                width=3,
#                color='rgba(68, 68, 68, 0)'
#            )
#        ))]
#        
#flight_paths = []
#for i in range( len( df_flight_paths ) ):
#    flight_paths.append(
#        dict(
#            type = 'scattergeo',
#            locationmode = 'USA-states',
#            lon = [ df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i] ],
#            lat = [ df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i] ],
#            mode = 'lines',
#            line = dict(
#                width = 1,
#                color = 'red',
#            ),
#            opacity = float(df_flight_paths['cnt'][i])/float(df_flight_paths['cnt'].max()),
#        )
#    )
#    
#layout = dict(
#        title = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
#        showlegend = False, 
#        geo = dict(
#            scope='north america',
#            projection=dict( type='azimuthal equal area' ),
#            showland = True,
#            landcolor = 'rgb(243, 243, 243)',
#            countrycolor = 'rgb(204, 204, 204)',
#        ),
#    )
#    
#fig = dict( data=flight_paths + airports, layout=layout )
#py.iplot( fig, filename='d3-flight-paths' )






#import plotly.plotly as py
#import plotly.graph_objs as go
#
#mapbox_access_token = 'pk.eyJ1IjoiZmFnb25jYWwiLCJhIjoiY2ppZzBvd3M1MDlsMTNrbjFycW51MThrNSJ9.QZS-9tcaUaoFzPhfeAfNqw'
#
#data = [
#    go.Scattermapbox(
#        lat=['45.5017'],
#        lon=['-73.5673'],
#        mode='markers',
#        marker=dict(
#            size=14
#        ),
#        text=['Montreal'],
#    )
#]
#
#layout = go.Layout(
#    autosize=True,
#    hovermode='closest',
#    mapbox=dict(
#        accesstoken=mapbox_access_token,
#        bearing=0,
#        center=dict(
#            lat=45,
#            lon=-73
#        ),
#        pitch=0,
#        zoom=5
#    ),
#)
#
#fig = dict(data=data, layout=layout)
#
#py.iplot(fig, filename='Montreal Mapbox', fileopt='new')










## -*- coding: utf-8 -*-
#
## Copyright (c) 2016-2018 by University of Kassel and Fraunhofer Institute for Energy Economics
## and Energy System Technology (IEE), Kassel. All rights reserved.
#
#
#import matplotlib.pyplot as plt
#import numpy as np
#from itertools import combinations
#import pandapower.topology as top
#import pandas as pd
#import networkx as nx
#
#
#def plot_voltage_profile(net, plot_transformers=True, ax=None, xlabel="Distance from Slack [km]",
#                         ylabel="Voltage [pu]", x0=0, trafocolor="r", bus_colors=None,
#                         line_loading_weight=False, voltage_column=None, bus_size=3, **kwargs):
#    if ax is None:
#        plt.figure(facecolor="white", dpi=120)
#        ax = plt.gca()
#    if not net.converged:
#        raise ValueError("no results in this pandapower network")
#    if voltage_column is None:
#        voltage_column = net.res_bus.vm_pu
#    for eg in net.ext_grid[net.ext_grid.in_service == True].bus:
#        d = top.calc_distance_to_bus(net, eg)
#        for lix, line in net.line[net.line.in_service == True].iterrows():
#            if line.from_bus not in d.index:
#                continue
#            if not ((net.switch.element == line.name) & ~net.switch.closed & (
#                        net.switch.et == 'l')).any():
#                from_bus = line.from_bus
#                to_bus = line.to_bus
#                x = [x0 + d.at[from_bus], x0 + d.at[to_bus]]
#                try:
#                    y = [voltage_column.at[from_bus], voltage_column.at[to_bus]]
#                except:
#                    raise UserWarning
#                if "linewidth" in kwargs or not line_loading_weight:
#                    ax.plot(x, y, **kwargs)
#                else:
#                    ax.plot(x, y, linewidth=0.4 * np.sqrt(net.res_line.loading_percent.at[lix]),
#                            **kwargs)
#                if bus_colors is not None:
#                    for bus, x, y in zip((from_bus, to_bus), x, y):
#                        if bus in bus_colors:
#                            ax.plot(x, y, 'or', color=bus_colors[bus], ms=bus_size)
#                kwargs = {k: v for k, v in kwargs.items() if not k == "label"}
#        # if plot_transformers:
#        #     if hasattr(plot_transformers, "__iter__"):  # if is a list for example
#        #         transformers = net.trafo.loc[list(plot_transformers)]
#        #     else:
#        #         transformers = net.trafo[net.trafo.in_service == True]
#        #     for _, transformer in transformers.iterrows():
#        #         if transformer.hv_bus not in d.index:
#        #             continue
#        #         ax.plot([x0 + d.loc[transformer.hv_bus],
#        #                  x0 + d.loc[transformer.lv_bus]],
#        #                 [voltage_column.loc[transformer.hv_bus],
#        #                  voltage_column.loc[transformer.lv_bus]], color=trafocolor,
#        #                 **{k: v for k, v in kwargs.items() if not k == "color"})
#
#        # trafo geodata
#        if plot_transformers:
#            for trafo_table in ['trafo', 'trafo3w']:
#                if trafo_table not in net.keys():
#                    continue
#                transformers = net[trafo_table].query('in_service')
#                for tid, tr in transformers.iterrows():
#                    t_buses = [tr[b_col] for b_col in ('lv_bus', 'mv_bus', 'hv_bus') if
#                               b_col in tr.index]
#                    if any([b not in d.index.values or b not in net.res_bus.index.values for b in
#                            t_buses]):
#                        # logger.info('cannot add trafo %d to plot' % tid)
#                        continue
#
#                    for bi, bj in combinations(t_buses, 2):
#                        tr_coords = ([x0 + d.loc[bi], x0 + d.loc[bj]],
#                                     [net.res_bus.at[bi, 'vm_pu'], net.res_bus.at[bj, 'vm_pu']])
#                        ax.plot(*tr_coords, color=trafocolor,
#                                **{k: v for k, v in kwargs.items() if not k == "color"})
#
#        if xlabel:
#            ax.set_xlabel(xlabel, fontweight="bold", color=(.4, .4, .4))
#        if ylabel:
#            ax.set_ylabel(ylabel, fontweight="bold", color=(.4, .4, .4))
#    return ax
#
#
#def plot_loading(net, element="line", boxcolor="b", mediancolor="r", whiskercolor="k", ax=None):
#    if ax is None:
#        plt.figure(facecolor="white", dpi=80)
#        ax = plt.gca()
#    loadings = net["res_%s" % element].loading_percent.values
#    boxplot = ax.boxplot(loadings[~np.isnan(loadings)], whis="range")
#    for l in list(boxplot.keys()):
#        plt.setp(boxplot[l], lw=3)
#        if l == "medians":
#            plt.setp(boxplot[l], color=mediancolor)
#        elif l == "boxes" or l == "whiskers":
#            plt.setp(boxplot[l], color=boxcolor)
#        else:
#            plt.setp(boxplot[l], color=whiskercolor)
#
#
#def voltage_profile_to_bus_geodata(net, voltages=None):
#    if voltages is None:
#        if not net.converged:
#            raise ValueError("no results in this pandapower network")
#        voltages = net.res_bus.vm_pu
#
#    mg =  top.create_nxgraph(net, respect_switches=True)
#    first_eg = net.ext_grid.bus.values[0]
#    mg.add_edges_from([(first_eg, y, {"weight": 0}) for y in net.ext_grid.bus.values[1:]])
#    dist = pd.Series(nx.single_source_dijkstra_path_length(mg, first_eg))
#
#    bgd = pd.DataFrame({"x": dist.loc[net.bus.index.values].values,
#                        "y": voltages.loc[net.bus.index.values].values},
#                       index=net.bus.index)
#    return bgd
#
#
#if __name__ == "__main__":
#    import pandapower as pp
#    import pandapower.networks as nw
#    import pandas as pd
#    import networkx as nx
#    import pandapower.plotting as plotting
#
#    net = nw.mv_oberrhein()
#    pp.runpp(net)
#    mg =  top.create_nxgraph(net, respect_switches=True)
#    feeders = list(top.connected_components(mg, notravbuses=set(net.trafo.lv_bus.values)))
#    lines_with_open_switches = set(net.switch.query("not closed and et == 'l'").element.values)
#    
#    fig, axs = plt.subplots(2)
#    for bgd, ax in zip([net.bus_geodata, voltage_profile_to_bus_geodata(net)], axs):
#        for color, f in zip(["C0", "C1", "C2", "C3"], feeders):
#            l = set(net.line.index[net.line.from_bus.isin(f)]) - lines_with_open_switches
#            c = plotting.create_line_collection(net, lines=l, use_bus_geodata=True, color=color,
#                                                bus_geodata=bgd)
#            ax.add_collection(c)
##            ax.scatter(bgd["x"], bgd["y"])
#            ax.autoscale_view(True, True, True)
#
#    h = 0.02
##    bc = plotting.create_bus_collection(net, buses=net.ext_grid.bus.values, width=h / ax.get_data_ratio(), height=h, bus_geodata=bgd)
##    ax.add_collection(bc)






# -*- coding: utf-8 -*-

# Copyright (c) 2016-2018 by University of Kassel and Fraunhofer Institute for Energy Economics
# and Energy System Technology (IEE), Kassel. All rights reserved.


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection, PatchCollection
from matplotlib.patches import Circle, Ellipse, Rectangle, RegularPolygon, Arc
from matplotlib.transforms import Affine2D
from itertools import combinations
import copy

try:
    import pplog as logging
except ImportError:
    import logging

logger = logging.getLogger(__name__)


def _rotate_dim2(arr, ang):
    """
    :param arr: array with 2 dimensions
    :param ang: angle [rad]
    """
    return np.dot(np.array([[np.cos(ang), np.sin(ang)], [-np.sin(ang), np.cos(ang)]]), arr)


def create_bus_collection(net, buses=None, size=5, marker="o", patch_type="circle", colors=None,
                          z=None, cmap=None, norm=None, infofunc=None, picker=False,
                          bus_geodata=None, cbar_title="Bus Voltage [pu]", **kwargs):
    """
    Creates a matplotlib patch collection of pandapower buses.
    Input:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **buses** (list, None) - The buses for which the collections are created.
            If None, all buses in the network are considered.
        **size** (int, 5) - patch size
        **marker** (str, "o") - patch marker
        **patch_type** (str, "circle") - patch type, can be
                - "circle" for a circle
                - "rect" for a rectangle
                - "poly<n>" for a polygon with n edges
        **infofunc** (function, None) - infofunction for the patch element
        **colors** (list, None) - list of colors for every element
        **z** (array, None) - array of bus voltage magnitudes for colormap. Used in case of given
            cmap. If None net.res_bus.vm_pu is used.
        **cmap** (ListedColormap, None) - colormap for the patch colors
        **norm** (matplotlib norm object, None) - matplotlib norm object
        **picker** (bool, False) - picker argument passed to the patch collection
        **bus_geodata** (DataFrame, None) - coordinates to use for plotting
            If None, net["bus_geodata"] is used
        **cbar_title** (str, "Bus Voltage [pu]") - colormap bar title in case of given cmap
        **kwargs - key word arguments are passed to the patch function
    OUTPUT:
        **pc** - patch collection
    """
    buses = net.bus.index.tolist() if buses is None else list(buses)
    if len(buses) == 0:
        return None
    if bus_geodata is None:
        bus_geodata = net["bus_geodata"]

    coords = zip(bus_geodata.loc[buses, "x"].values, bus_geodata.loc[buses, "y"].values)

    infos = []

    if 'height' not in kwargs and 'width' not in kwargs:
        kwargs['height'] = kwargs['width'] = 2 * size
    if patch_type == "rect":
        kwargs['height'] *= 2
        kwargs['width'] *= 2

    def figmaker(x, y, i):
        if colors:
            kwargs["color"] = colors[i]
        if patch_type == 'ellipse' or patch_type == 'circle':  # circles are just ellipses
            angle = kwargs['angle'] if 'angle' in kwargs else 0
            fig = Ellipse((x, y), angle=angle, **kwargs)
        elif patch_type == "rect":
            fig = Rectangle([x - kwargs['width'] / 2, y - kwargs['height'] / 2], **kwargs)
        elif patch_type.startswith("poly"):
            edges = int(patch_type[4:])
            fig = RegularPolygon([x, y], numVertices=edges, radius=size, **kwargs)
        else:
            logger.error("Wrong patchtype. Please choose a correct patch type.")
        if infofunc:
            infos.append(infofunc(buses[i]))
        return fig

    patches = [figmaker(x, y, i)
               for i, (x, y) in enumerate(coords)
               if x != np.nan]
    pc = PatchCollection(patches, match_original=True, picker=picker)
    pc.bus_indices = np.array(buses)
    if cmap:
        pc.set_cmap(cmap)
        pc.set_norm(norm)
        if z is None and net:
            z = net.res_bus.vm_pu.loc[buses]
        else:
            logger.warning("z is None and no net is provided")
        pc.set_array(np.array(z))
        pc.has_colormap = True
        pc.cbar_title = cbar_title

    pc.patch_type = patch_type
    pc.size = size
    if 'orientation' in kwargs:
        pc.orientation = kwargs['orientation']
    if "zorder" in kwargs:
        pc.set_zorder(kwargs["zorder"])
    pc.info = infos

    return pc


def create_line_collection(net, lines=None, line_geodata=None, bus_geodata=None,
                           use_bus_geodata=False, infofunc=None,
                           cmap=None, norm=None, picker=False, z=None,
                           cbar_title="Line Loading [%]", clim=None, **kwargs):
    """
    Creates a matplotlib line collection of pandapower lines.
    Input:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **lines** (list, None) - The lines for which the collections are created. If None, all lines
            in the network are considered.
        **line_geodata** (DataFrame, None) - coordinates to use for plotting. If None,
            net["line_geodata"] is used
        **bus_geodata** (DataFrame, None) - coordinates to use for plotting
            If None, net["bus_geodata"] is used
        **use_bus_geodata** (bool, False) - Defines whether bus or line geodata are used.
         **infofunc** (function, None) - infofunction for the patch element
        **cmap** - colormap for the patch colors
        **norm** (matplotlib norm object, None) - matplotlib norm object
        **picker** (bool, False) - picker argument passed to the patch collection
        **z** (array, None) - array of bus voltage magnitudes for colormap. Used in case of given
            cmap. If None net.res_bus.vm_pu is used.
        **cbar_title** (str, "Bus Voltage [pu]") - colormap bar title in case of given cmap
        **clim** (tuple of floats, None) - setting the norm limits for image scaling
        **kwargs - key word arguments are passed to the patch function
    OUTPUT:
        **lc** - line collection
    """
    lines = net.line.index.tolist() if lines is None else list(lines)
    if len(lines) == 0:
        return None
    if line_geodata is None:
        line_geodata = net["line_geodata"]
    if bus_geodata is None:
        bus_geodata = net["bus_geodata"]
    if len(lines) == 0:
        return None

    lines_with_geo = []
    if use_bus_geodata:
        data = []
        for line, (a, b) in net.line.loc[lines, ["from_bus", "to_bus"]].iterrows():
            if a in bus_geodata.index.values and b in bus_geodata.index.values:
                lines_with_geo.append(line)
                data.append(([(bus_geodata.at[a, "x"], bus_geodata.at[a, "y"]),
                              (bus_geodata.at[b, "x"], bus_geodata.at[b, "y"])],
                             infofunc(line) if infofunc else[]))

        lines_without_geo = set(lines)-set(lines_with_geo)
        if lines_without_geo:
            logger.warning("Could not plot lines %s. Bus geodata is missing for those lines!"
                           % lines_without_geo)
    else:
        data = []
        for line in lines:
            if line in line_geodata.index.values:
                lines_with_geo.append(line)
                data.append((line_geodata.loc[line, "coords"], infofunc(line) if infofunc else []))

        lines_without_geo = set(lines)-set(lines_with_geo)
        if lines_without_geo:
            logger.warning("Could not plot lines %s. Line geodata is missing for those lines!"
                           % lines_without_geo)

    if len(data) == 0:
        return None

    data, info = list(zip(*data))

    # This would be done anyways by matplotlib - doing it explicitly makes it a) clear and
    # b) prevents unexpected behavior when observing colors being "none"
    lc = LineCollection(data, picker=picker, **kwargs)
    lc.line_indices = np.array(lines_with_geo)
    if cmap:
        if z is None:
            z = net.res_line.loading_percent.loc[lines_with_geo]
        lc.set_cmap(cmap)
        lc.set_norm(norm)
        if clim is not None:
            lc.set_clim(clim)
        lc.set_array(np.array(z))
        lc.has_colormap = True
        lc.cbar_title = cbar_title
    lc.info = info

    return lc


def create_trafo_connection_collection(net, trafos=None, bus_geodata=None, infofunc=None, **kwargs):
    """
    Creates a matplotlib line collection of pandapower transformers.
    Input:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **trafos** (list, None) - The transformers for which the collections are created.
            If None, all transformers in the network are considered.
        **bus_geodata** (DataFrame, None) - coordinates to use for plotting
            If None, net["bus_geodata"] is used
         **infofunc** (function, None) - infofunction for the patch element
        **kwargs - key word arguments are passed to the patch function
    OUTPUT:
        **lc** - line collection
    """
    trafos = net.trafo if trafos is None else net.trafo.loc[trafos]

    if bus_geodata is None:
        bus_geodata = net["bus_geodata"]

    hv_geo = list(zip(bus_geodata.loc[trafos["hv_bus"], "x"].values,
                      bus_geodata.loc[trafos["hv_bus"], "y"].values))
    lv_geo = list(zip(bus_geodata.loc[trafos["lv_bus"], "x"].values,
                      bus_geodata.loc[trafos["lv_bus"], "y"].values))

    tg = list(zip(hv_geo, lv_geo))

    info = [infofunc(tr) if infofunc else [] for tr in trafos.index.values]

    lc = LineCollection([(tgd[0], tgd[1]) for tgd in tg], **kwargs)
    lc.info = info

    return lc


def create_trafo3w_connection_collection(net, trafos=None, bus_geodata=None, infofunc=None,
                                         **kwargs):
    """
    Creates a matplotlib line collection of pandapower 3W-transformers.
    This function can be used to create line collections for voltage fall diagrams.
    Input:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **trafos** (list, None) - The 3W-transformers for which the collections are created.
            If None, all 3W-transformers in the network are considered.
        **bus_geodata** (DataFrame, None) - coordinates to use for plotting
            If None, net["bus_geodata"] is used
         **infofunc** (function, None) - infofunction for the patch element
        **kwargs - key word arguments are passed to the patch function
    OUTPUT:
        **lc** - line collection
    """
    trafos = net.trafo3w if trafos is None else net.trafo3w.loc[trafos]

    if bus_geodata is None:
        bus_geodata = net["bus_geodata"]

    hv_geo, mv_geo, lv_geo = (list(zip(*(bus_geodata.loc[trafos[column], var].values
                                         for var in ['x', 'y'])))
                              for column in ['hv_bus', 'mv_bus', 'lv_bus'])

    # create 3 connection lines, each of 2 points, for every trafo3w
    tg = [x for c in [list(combinations(y, 2))
                      for y in zip(hv_geo, mv_geo, lv_geo)]
          for x in c]

    # 3 times infofunc for every trafo
    info = [infofunc(x) if infofunc else []
            for tr in [(t, t, t) for t in trafos.index.values]
            for x in tr]

    lc = LineCollection(tg, **kwargs)
    # from matplotlib.colors import ListedColormap, BoundaryNorm
    # cmap = ListedColormap(['r', 'g', 'b'])
    # norm = BoundaryNorm([-3, -1, 1, 3], cmap.N)
    # lc = LineCollection(tg, cmap=cmap, norm=norm, **kwargs)
    # lc.set_array(np.tile([-2, 0, 2], len(trafos)))
    lc.info = info

    return lc


def create_trafo_collection(net, trafos=None, picker=False, size=None,
                            infofunc=None, **kwargs):
    """
    Creates a matplotlib line collection of pandapower transformers.
    Input:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **trafos** (list, None) - The transformers for which the collections are created.
            If None, all transformers in the network are considered.
        **picker** (bool, False) - picker argument passed to the patch collection
        **size** (int, None) - size of transformer symbol circles. Should be >0 and
            < 0.35*bus_distance
         **infofunc** (function, None) - infofunction for the patch element
        **kwargs - key word arguments are passed to the patch function
    OUTPUT:
        **lc** - line collection
        **pc** - patch collection
    """
    trafo_table = net.trafo if trafos is None else net.trafo.loc[trafos]
    lines = []
    circles = []
    infos = []
    color = kwargs.pop("color", "k")
    linewidths = kwargs.pop("linewidths", 2.)
    for i, trafo in trafo_table.iterrows():
        p1 = net.bus_geodata[["x", "y"]].loc[trafo.hv_bus].values
        p2 = net.bus_geodata[["x", "y"]].loc[trafo.lv_bus].values
        if np.all(p1 == p2):
            continue
        d = np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        if size is None:
            size_this = np.sqrt(d) / 5
        else:
            size_this = size
        off = size_this * 0.35
        circ1 = (0.5 - off / d) * (p1 - p2) + p2
        circ2 = (0.5 + off / d) * (p1 - p2) + p2
        circles.append(Circle(circ1, size_this, fc=(1, 0, 0, 0), ec=color))
        circles.append(Circle(circ2, size_this, fc=(1, 0, 0, 0), ec=color))

        lp1 = (0.5 - off / d - size_this / d) * (p2 - p1) + p1
        lp2 = (0.5 - off / d - size_this / d) * (p1 - p2) + p2
        lines.append([p1, lp1])
        lines.append([p2, lp2])
        if infofunc is not None:
            infos.append(infofunc(i))
            infos.append(infofunc(i))
    if len(circles) == 0:
        return None, None
    lc = LineCollection((lines), color=color, picker=picker, linewidths=linewidths, **kwargs)
    lc.info = infos
    pc = PatchCollection(circles, match_original=True, picker=picker, linewidth=linewidths,
                         **kwargs)
    pc.info = infos
    return lc, pc


def create_trafo3w_collection(net, trafo3ws=None, picker=False, infofunc=None, **kwargs):
    """
    Creates a matplotlib line collection of pandapower transformers.
    Input:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **trafo3ws** (list, None) - The three winding transformers for which the collections are
            created. If None, all three winding transformers in the network are considered.
        **picker** (bool, False) - picker argument passed to the patch collection
         **infofunc** (function, None) - infofunction for the patch element
        **kwargs - key word arguments are passed to the patch function
    OUTPUT:
        **lc** - line collection
        **pc** - patch collection
    """
    trafo3w_table = net.trafo3w if trafo3ws is None else net.trafo3w.loc[trafo3ws]
    lines = []
    circles = []
    infos = []
    color = kwargs.pop("color", "k")
    linewidth = kwargs.pop("linewidths", 2.)
    for i, trafo3w in trafo3w_table.iterrows():
        # get bus geodata
        p1 = net.bus_geodata[["x", "y"]].loc[trafo3w.hv_bus].values
        p2 = net.bus_geodata[["x", "y"]].loc[trafo3w.mv_bus].values
        p3 = net.bus_geodata[["x", "y"]].loc[trafo3w.lv_bus].values
        if np.all(p1 == p2) and np.all(p1 == p3):
            continue
        p = np.array([p1, p2, p3])
        # determine center of buses and minimum distance center-buses
        center = sum(p) / 3
        d = np.linalg.norm(p - center, axis=1)
        r = d.min() / 3
        # determine closest bus to center and vector from center to circle midpoint in closest
        # direction
        closest = d.argmin()
        to_closest = (p[closest] - center) / d[closest] * 2 * r / 3
        # determine vectors from center to circle midpoint
        order = list(range(closest, 3)) + list(range(closest))
        cm = np.empty((3, 2))
        cm[order.pop(0)] = to_closest
        ang = 2 * np.pi / 3  # 120 degree
        cm[order.pop(0)] = _rotate_dim2(to_closest, ang)
        cm[order.pop(0)] = _rotate_dim2(to_closest, -ang)
        # determine midpoints of circles
        m = center + cm
        # determine endpoints of circles
        e = (center - p) * (1 - 5 * r / 3 / d).reshape(3, 1) + p
        # save circle and line collection data
        for i in range(3):
            circles.append(Circle(m[i], r, fc=(1, 0, 0, 0), ec=color))
            lines.append([p[i], e[i]])

        if infofunc is not None:
            infos.append(infofunc(i))
            infos.append(infofunc(i))
    if len(circles) == 0:
        return None, None
    lc = LineCollection((lines), color=color, picker=picker, linewidths=linewidth, **kwargs)
    lc.info = infos
    pc = PatchCollection(circles, match_original=True, picker=picker, linewidth=linewidth, **kwargs)
    pc.info = infos
    return lc, pc


def create_load_collection(net, loads=None, size=1., infofunc=None, orientation=np.pi, **kwargs):
    load_table = net.load if loads is None else net.load.loc[loads]
    """
    Creates a matplotlib patch collection of pandapower loads.
    Input:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **size** (float, 1) - patch size
        **infofunc** (function, None) - infofunction for the patch element
        **orientation** (float, np.pi) - orientation of load collection. pi is directed downwards,
            increasing values lead to clockwise direction changes.
        **kwargs - key word arguments are passed to the patch function
    OUTPUT:
        **load1** - patch collection
        **load2** - patch collection
    """
    lines = []
    polys = []
    infos = []
    off = 2.
    ang = orientation if hasattr(orientation, '__iter__') else [orientation]*net.load.shape[0]
    color = kwargs.pop("color", "k")
    for i, load in load_table.iterrows():
        p1 = net.bus_geodata[["x", "y"]].loc[load.bus]
        p2 = p1 + _rotate_dim2(np.array([0, size * off]), ang[i])
        p3 = p1 + _rotate_dim2(np.array([0, size * (off - 0.5)]), ang[i])
        polys.append(RegularPolygon(p2, numVertices=3, radius=size, orientation=-ang[i]))
        lines.append((p1, p3))
        if infofunc is not None:
            infos.append(infofunc(i))
    load1 = PatchCollection(polys, facecolor="w", edgecolor=color, **kwargs)
    load2 = LineCollection(lines, color=color, **kwargs)
    load1.info = infos
    load2.info = infos
    return load1, load2


def create_gen_collection(net, size=1., infofunc=None, **kwargs):
    """
    Creates a matplotlib patch collection of pandapower gens.
    Input:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **size** (float, 1) - patch size
        **infofunc** (function, None) - infofunction for the patch element
        **kwargs - key word arguments are passed to the patch function
    OUTPUT:
        **gen1** - patch collection
        **gen2** - patch collection
    """
    lines = []
    polys = []
    infos = []
    off = 1.7
    for i, gen in net.gen.iterrows():
        p1 = net.bus_geodata[["x", "y"]].loc[gen.bus]
        p2 = p1 - np.array([0, size * off])
        polys.append(Circle(p2, size))
        polys.append(
            Arc(p2 + np.array([-size / 6.2, -size / 2.6]), size / 2, size, theta1=45, theta2=135))
        polys.append(
            Arc(p2 + np.array([size / 6.2, size / 2.6]), size / 2, size, theta1=225, theta2=315))
        lines.append((p1, p2 + np.array([0, size])))
        if infofunc is not None:
            infos.append(infofunc(i))
    gen1 = PatchCollection(polys, facecolor="w", edgecolor="k", **kwargs)
    gen2 = LineCollection(lines, color="k", **kwargs)
    gen1.info = infos
    gen2.info = infos
    return gen1, gen2


def create_sgen_collection(net, sgens=None, size=1., infofunc=None, orientation=np.pi, **kwargs):
    sgen_table = net.sgen if sgens is None else net.sgen.loc[sgens]
    """
    Creates a matplotlib patch collection of pandapower sgen.
    Input:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **size** (float, 1) - patch size
        **infofunc** (function, None) - infofunction for the patch element
        **orientation** (float, np.pi) - orientation of load collection. pi is directed downwards,
            increasing values lead to clockwise direction changes.
        **kwargs - key word arguments are passed to the patch function
    OUTPUT:
        **sgen1** - patch collection
        **sgen2** - patch collection
    """
    lines = []
    polys = []
    infos = []
    off = 1.7
    r_triangle = size*0.4
    ang = orientation if hasattr(orientation, '__iter__') else [orientation]*net.sgen.shape[0]
    color = kwargs.pop("color", "k")
    for i, sgen in sgen_table.iterrows():
        bus_geo = net.bus_geodata[["x", "y"]].loc[sgen.bus]
        mp_circ = bus_geo + _rotate_dim2(np.array([0, size * off]), ang[i])  # mp means midpoint
        circ_edge = bus_geo + _rotate_dim2(np.array([0, size * (off-1)]), ang[i])
        mp_tri1 = mp_circ + _rotate_dim2(np.array([r_triangle, -r_triangle/4]), ang[i])
        mp_tri2 = mp_circ + _rotate_dim2(np.array([-r_triangle, r_triangle/4]), ang[i])
        perp_foot1 = mp_tri1 + _rotate_dim2(np.array([0, -r_triangle/2]), ang[i])  # dropped perpendicular foot of triangle1
        line_end1 = perp_foot1 + + _rotate_dim2(np.array([-2.5*r_triangle, 0]), ang[i])
        perp_foot2 = mp_tri2 + _rotate_dim2(np.array([0, r_triangle/2]), ang[i])
        line_end2 = perp_foot2 + + _rotate_dim2(np.array([2.5*r_triangle, 0]), ang[i])
        polys.append(Circle(mp_circ, size))
        polys.append(RegularPolygon(mp_tri1, numVertices=3, radius=r_triangle, orientation=-ang[i]))
        polys.append(RegularPolygon(mp_tri2, numVertices=3, radius=r_triangle,
                                    orientation=np.pi-ang[i]))
        lines.append((bus_geo, circ_edge))
        lines.append((perp_foot1, line_end1))
        lines.append((perp_foot2, line_end2))
        if infofunc is not None:
            infos.append(infofunc(i))
    sgen1 = PatchCollection(polys, facecolor="w", edgecolor="k", **kwargs)
    sgen2 = LineCollection(lines, color="k", **kwargs)
    sgen1.info = infos
    sgen2.info = infos
    return sgen1, sgen2


def create_ext_grid_collection(net, size=1., infofunc=None, orientation=0, picker=False, **kwargs):
    """
    Creates a matplotlib patch collection of pandapower ext_grid.
    Input:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **size** (float, 1) - patch size
        **infofunc** (function, None) - infofunction for the patch element
        **orientation** (float, 0) - orientation of load collection. 0 is directed upwards,
            increasing values lead to clockwise direction changes.
        **picker** (bool, False) - picker argument passed to the patch collection
        **kwargs - key word arguments are passed to the patch function
    OUTPUT:
        **ext_grid1** - patch collection
        **ext_grid2** - patch collection
    """
    lines = []
    polys = []
    infos = []
    color = kwargs.pop("color", "k")
    for i, ext_grid in net.ext_grid.iterrows():
        p1 = net.bus_geodata[["x", "y"]].loc[ext_grid.bus]
        p2 = p1 + _rotate_dim2(np.array([0, size]), orientation)
        polys.append(Rectangle([p2[0] - size / 2, p2[1] - size / 2], size, size))
        lines.append((p1, p2 - _rotate_dim2(np.array([0, size / 2]), orientation)))
        if infofunc is not None:
            infos.append(infofunc(i))
    ext_grid1 = PatchCollection(polys, facecolor=(1, 0, 0, 0), edgecolor=(0, 0, 0, 1),
                                hatch="XXX", picker=picker, color=color, **kwargs)
    ext_grid2 = LineCollection(lines, color=color, picker=picker, **kwargs)
    ext_grid1.info = infos
    ext_grid2.info = infos
    return ext_grid1, ext_grid2


def create_line_switch_collection(net, size=1, distance_to_bus=3, use_line_geodata=False, **kwargs):
    """
    Creates a matplotlib patch collection of pandapower line-bus switches.
    INPUT:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **size** (float, 1) - Size of the switch patches
        **distance_to_bus** (float, 3) - Distance of the switch patch from the bus patch
        **use_line_geodata** (bool, False) - If True, line coordinates are used to identify the
                                             switch position
        **kwargs - Key word arguments are passed to the patch function
    OUTPUT:
        **switches** - patch collection
    """
    lbs_switches = net.switch.index[net.switch.et == "l"]

    color = kwargs.pop("color", "k")

    switch_patches = []
    for switch in lbs_switches:
        sb = net.switch.bus.loc[switch]
        line = net.line.loc[net.switch.element.loc[switch]]
        fb = line.from_bus
        tb = line.to_bus

        line_buses = set([fb, tb])
        target_bus = list(line_buses - set([sb]))[0]

        if sb not in net.bus_geodata.index or target_bus not in net.bus_geodata.index:
            logger.warning("Bus coordinates for switch %s not found, skipped switch!" % switch)
            continue

        # switch bus and target coordinates
        pos_sb = net.bus_geodata.loc[sb, ["x", "y"]].values
        pos_tb = np.zeros(2)

        use_bus_geodata = False

        if use_line_geodata:
            if line.name in net.line_geodata.index:
                line_coords = net.line_geodata.coords.loc[line.name]
                # check, which end of the line is nearer to the switch bus
                if len(line_coords) > 2:
                    if abs(line_coords[0][0] - pos_sb[0]) < 0.01 and \
                                    abs(line_coords[0][1] - pos_sb[1]) < 0.01:
                        pos_tb = np.array([line_coords[1][0], line_coords[1][1]])
                    else:
                        pos_tb = np.array([line_coords[-2][0], line_coords[-2][1]])
                else:
                    use_bus_geodata = True
            else:
                use_bus_geodata = True

        if not use_line_geodata or use_bus_geodata:
            pos_tb = net.bus_geodata.loc[target_bus, ["x", "y"]]

        # position of switch symbol
        vec = pos_tb - pos_sb
        mag = np.linalg.norm(vec)
        pos_sw = pos_sb + vec / mag * distance_to_bus

        # rotation of switch symbol
        angle = np.arctan2(vec[1], vec[0])
        rotation = Affine2D().rotate_around(pos_sw[0], pos_sw[1], angle)

        # color switch by state
        col = color if net.switch.closed.loc[switch] else "white"

        # create switch patch (switch size is respected to center the switch on the line)
        patch = Rectangle((pos_sw[0] - size / 2, pos_sw[1] - size / 2), size, size, facecolor=col, edgecolor=color)
        # apply rotation
        patch.set_transform(rotation)

        switch_patches.append(patch)

    switches = PatchCollection(switch_patches, match_original=True, **kwargs)
    return switches


def create_bus_bus_switch_collection(net, size=1., helper_line_style=':', helper_line_size=1., helper_line_color="gray", **kwargs):
    """
    Creates a matplotlib patch collection of pandapower bus-bus switches. Switches are plotted in the center between two buses with a "helper"
    line (dashed and thin) being drawn between the buses as well.
    INPUT:
        **net** (pandapowerNet) - The pandapower network
    OPTIONAL:
        **size** (float, 1.0) - Size of the switch patches
        **helper_line_style** (string, ':') - Line style of the "helper" line being plotted between two buses connected by a bus-bus switch
        **helper_line_size** (float, 1.0) - Line width of the "helper" line being plotted between two buses connected by a bus-bus switch
        **helper_line_color** (string, "gray") - Line color of the "helper" line being plotted between two buses connected by a bus-bus switch
        **kwargs - Key word arguments are passed to the patch function
    OUTPUT:
        **switches**, **helper_lines** - tuple of patch collections
    """
    lbs_switches = net.switch.index[net.switch.et == "b"]
    color = kwargs.pop("color", "k")
    switch_patches = []
    line_patches = []
    for switch in lbs_switches:
        switch_bus = net.switch.bus.loc[switch]
        target_bus = net.switch.element.loc[switch]
        if switch_bus not in net.bus_geodata.index or target_bus not in net.bus_geodata.index:
            logger.warning("Bus coordinates for switch %s not found, skipped switch!" % switch)
            continue
        # switch bus and target coordinates
        pos_sb = net.bus_geodata.loc[switch_bus, ["x", "y"]].values
        pos_tb = net.bus_geodata.loc[target_bus, ["x", "y"]].values
        # position of switch symbol
        vec = pos_tb - pos_sb
        mag = np.linalg.norm(vec)
        pos_sw = pos_sb + vec / mag * 0.5 if not np.allclose(pos_sb, pos_tb) else pos_tb
        # rotation of switch symbol
        angle = np.arctan2(vec[1], vec[0])
        rotation = Affine2D().rotate_around(pos_sw[0], pos_sw[1], angle)
        # color switch by state
        col = color if net.switch.closed.loc[switch] else "white"
        # create switch patch (switch size is respected to center the switch on the line)
        patch = Rectangle((pos_sw[0] - size / 2, pos_sw[1] - size / 2), size, size, facecolor=col, edgecolor=color)
        # apply rotation
        patch.set_transform(rotation)
        # add to collection lists
        switch_patches.append(patch)
        line_patches.append([pos_sb.tolist(), pos_tb.tolist()])
    # create collections and return
    switches = PatchCollection(switch_patches, match_original=True, **kwargs)
    helper_lines = LineCollection(line_patches, linestyles=helper_line_style, linewidths=helper_line_size, colors=helper_line_color)
    return switches, helper_lines


def add_collections_to_axes(ax, collections, plot_colorbars=True):
    for c in collections:
        if c:
            c = copy.copy(c)
            ax.add_collection(c)
            if plot_colorbars and hasattr(c, "has_colormap") and c.has_colormap:
                extend = c.extend if hasattr(c, "extend") else "neither"
                cbar_load = plt.colorbar(c, extend=extend, ax=ax)
                if hasattr(c, "cbar_title"):
                    cbar_load.ax.set_ylabel(c.cbar_title)


def draw_collections(collections, figsize=(10, 8), ax=None, plot_colorbars=True, set_aspect=True,
                     axes_visible=(False, False)):
    """
    Draws matplotlib collections which can be created with the create collection functions.
    Input:
        **collections** (list) - iterable of collection objects
    OPTIONAL:
        **figsize** (tuple, (10,8)) - figsize of the matplotlib figure
        **ax** (axis, None) - matplotlib axis object to plot into, new axis is created if None
        **plot_colorbars** (bool, True) - defines whether colorbars should be plotted
        **set_aspect** (bool, True) - defines whether 'equal' and 'datalim' aspects of axis scaling
            should be set.
        **axes_visible** (tuple, (False, False)) - defines visibility of (xaxis, yaxis)
    OUTPUT:
        **ax** - matplotlib axes
    """

    if not ax:
        plt.figure(facecolor="white", figsize=figsize)
        plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.05,
                            wspace=0.02, hspace=0.04)
    ax = ax or plt.gca()

    add_collections_to_axes(ax, collections, plot_colorbars=plot_colorbars)

    try:
        ax.set_facecolor("white")
    except:
        ax.set_axis_bgcolor("white")
    ax.xaxis.set_visible(axes_visible[0])
    ax.yaxis.set_visible(axes_visible[1])
    if set_aspect:
        ax.set_aspect('equal', 'datalim')
    ax.autoscale_view(True, True, True)
    ax.margins(.02)
    plt.draw()
    return ax


if __name__ == "__main__":
    if 0:
        import pandapower as pp

        net = pp.create_empty_network()
        b1 = pp.create_bus(net, 10, geodata=(5, 10))
        b2 = pp.create_bus(net, 0.4, geodata=(5, 15))
        b3 = pp.create_bus(net, 0.4, geodata=(0, 22))
        b4 = pp.create_bus(net, 0.4, geodata=(8, 20))
        pp.create_gen(net, b1, p_kw=100)
        pp.create_load(net, b3, p_kw=100)
        pp.create_ext_grid(net, b4)

        pp.create_line(net, b2, b3, 2.0, std_type="NAYY 4x50 SE")
        pp.create_line(net, b2, b4, 2.0, std_type="NAYY 4x50 SE")
        pp.create_transformer(net, b1, b2, std_type="0.63 MVA 10/0.4 kV")
        pp.create_transformer(net, b3, b4, std_type="0.63 MVA 10/0.4 kV")

        bc = create_bus_collection(net, size=0.2, color="k")
        lc = create_line_collection(net, use_line_geodata=False, color="k", linewidth=3.)
        lt, bt = create_trafo_collection(net, size=2, linewidth=3.)
        load1, load2 = create_load_collection(net, linewidth=2.,
                                              infofunc=lambda x: ("load", x))
        gen1, gen2 = create_gen_collection(net, linewidth=2.,
                                           infofunc=lambda x: ("gen", x))
        eg1, eg2 = create_ext_grid_collection(net, size=2.,
                                              infofunc=lambda x: ("ext_grid", x))

        draw_collections([bc, lc, load1, load2, gen1, gen2, lt, bt, eg1, eg2])
    else:
        pass












