# -*- coding: utf-8 -*-
"""
read_wfs.py

Read WFS

Created on Tue Nov 13 09:18:02 2018

@author: Faris Alsuhail
"""

import geopandas as gpd
import requests
import geojson
import pycrs

# Specify the url for the backend
#url = 'http://geo.stat.fi/geoserver/vaestoruutu/wfs'
url = 'https://kartta.hel.fi/ws/geoserver/avoindata/wfs'

# Specify parameters (read data in json format)
#params = dict(service='WFS', version='2.0.0', request='GetFeature',
 #        typeName='vaestoruutu:vaki2017_5km', outputFormat='json')

# Specify parameters (read data in json format)
params = dict(service='WFS', version='2.0.0', request='GetFeature',
         typeName='avoindata:Halke_aanestysalue', outputFormat='json')


# Fetch data from WFS using requests
r = requests.get(url, params=params)

# Create GeoDataFrame from geojson
data = gpd.GeoDataFrame.from_features(geojson.loads(r.content))

#define CRS
#data.crs = {'init' : 'epsg:3067'}
#data.crs = pycrs.parser.from_epsg_code(3879).to_proj4()

#Plot data
data.plot()

#data = data.drop('bbox', axis = 1)

outfp  = "L2_data/population_grid5km.shp"
data.to_file(outfp)
