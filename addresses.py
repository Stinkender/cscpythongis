# -*- coding: utf-8 -*-
"""
addresses.py

Rambling around with some addresses. Convert addresses to points and vice versa.

Created on Tue Nov 13 10:21:45 2018

@author: Faris Alsuhail
"""

#Import modules
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from geopandas.tools import geocode
import contextily as ctx

def add_basemap(ax, zoom, url='http://tiles.kartat.kapsi.fi/taustakartta/tileZ/tileX/tileY.png'):
    xmin, xmax, ymin, ymax = ax.axis()
    basemap, extent = ctx.bounds2img(xmin, ymin, xmax, ymax, zoom=zoom, url=url)
    ax.imshow(basemap, extent=extent, interpolation='bilinear')
    # restore original x/y limits
    ax.axis((xmin, xmax, ymin, ymax))

# Filepath for addresses
fp = "L3_data/addresses.txt"

# Read the data
data = pd.read_csv(fp, sep=';')

#data.head()
#type(data)

#Geocode addresses with Nominatim backend
geo = geocode(data['addr'], provider='nominatim', user_agent='csc_user_fa')
geo.head()

#Merge geocoded locations back to the original dataframe
geo = geo.join(data)

#Reproject to webmercator
geo = geo.to_crs(epsg=3857)

#Plot points with background map
ax = geo.plot()

#Add basemap
add_basemap(ax=ax, zoom = 10)
