# -*- coding: utf-8 -*-
"""
download_osm_data.py

Use OSMnx package to download OSM data using Overpass API

Created on Tue Nov 13 11:17:56 2018

@author: Faris Alsuhail
"""

import osmnx as ox
import matplotlib.pyplot as plt

#Specify place name
place_name = "Viikki, Helsinki, Finland"
place_name2 = "Munkkivuori, Helsinki, Finland"

#Fetch data
graph = ox.graph_from_place(place_name)
type(graph)

#Plot the streets
fig, ax = ox.plot_graph(graph)

#Convert the graph to GeoDataFrames
nodes, edges = ox.graph_to_gdfs(graph)

#Retrieve buildings

buildings = ox.buildings_from_address(place_name, distance = 1000)
buildings.plot()

#Fetch footprint
footprint = ox.gdf_from_place(place_name)
footprint.plot()

#Retrieve POIs from OSM
restaurants = ox.pois_from_place(place_name, amenities=['restaurant'])
restaurants.plot()

#!!!plot all layers together!!!
ax = footprint.plot(facecolor = 'green') #added as ax in the plot() below
#ax = 
edges.plot(ax=ax, edgecolor = 'gray', linewidth = 1)
#ax = 
buildings.plot(ax=ax, facecolor = 'yellow', alpha = 0.7)
#ax  =
restaurants.plot(ax=ax, color = 'red', alpha = 0.7, markersize = 12)