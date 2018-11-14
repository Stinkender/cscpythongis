# -*- coding: utf-8 -*-
"""
Let's mask some rasters

Created on Wed Nov 14 11:09:05 2018

@author: Faris Alsuhail
"""

import rasterio
from rasterio.plot import show
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
import pycrs
import os
import json

#Specify data directory
data_dir = "L5_data"

#input raster
fp = os.path.join(data_dir, "p188r018_7t20020529_z34__LV-FIN.tif")

#output raster
out_tif = os.path.join(data_dir, "Helsinki_Masked.tif")

#read the data
raster = rasterio.open(fp)

#Visualise NIR
show((raster, 4), cmap="terrain")

# WGS84 coordinates
minx, miny = 24.60, 60.00
maxx, maxy = 25.22, 60.35
bbox = box(minx, miny, maxx, maxy)

#Create a GeoDataframe
crs_code = pycrs.parser.from_epsg_code(4326).to_proj4()
geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=crs_code)

geo.plot()

#Project the GeoDataFrame to the same projection as the raster
geo = geo.to_crs(crs=raster.crs)

def get_features(gdf):
    """Converts geodataframe into a format suitable for rasterio mask function"""
    features = [json.loads(gdf.to_json())['features'][0]['geometry']] #Could this approach be used to convert json to csv?
    return features

#Convert gdf to geometric features dict

coords = get_features(geo)

#Clip the raster based on polygon
out_img, out_transform = mask(dataset=raster, shapes=coords, crop=True)

#Copy metadata from original raster
out_meta = raster.meta.copy()
print(out_meta)

#Parse proj4 transformation to store with raster
epsg_code = int(raster.crs.data['init'].replace('epsg:', ''))
print(epsg_code)

epsg_proj4 = pycrs.parser.from_epsg_code(epsg_code).to_proj4()
print(epsg_proj4)

#Update metadata with new dimensions, crs etc.
out_meta.update({
     #   "driver": "GTiff",
        "height": out_img.shape[1],
        "width": out_img.shape[2],
        "transform": out_transform,
        "crs": epsg_proj4
        
        })

#Save the clipped raster to disk
with rasterio.open(out_tif, "w", **out_meta) as dest:
    dest.write(out_img)


# Open the clipped raster file
clipped = rasterio.open(out_tif)

# Visualize
show((clipped, 5), cmap='inferno')

























