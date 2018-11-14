# -*- coding: utf-8 -*-
"""
raster_mosaic.py

How to create a raster mosaic using witchcraft?

Created on Wed Nov 14 13:20:35 2018

@author: Faris Alsuhail
"""

import rasterio
from rasterio.merge import merge
from rasterio.plot import show
import glob
import os
import pycrs

#File and folder paths
data_dir = "L5_data"
out_fp = os.path.join(data_dir, "Helsinki_DEM2x2m_Mosaic2.tif") #this is for output

#Make a search criteria to select DEM files
search_criteria = "L*.tif"
query = os.path.join(data_dir, search_criteria)
print(query)

#We use glob to list all DEM files
dem_filepaths = glob.glob(query)

#List found files
dem_filepaths

#Open source files with rasterio
source_files_to_mosaic = [rasterio.open(fp) for fp in dem_filepaths]


# Merge function returns a single mosaic array and the transformation info
mosaic, out_trans = merge(source_files_to_mosaic)

# Plot the result
show(mosaic, cmap='gist_earth')

#We are ready to save our mosaic to disk.
#First update the metadata with our new dimensions, transform and CRS

# Copy the metadata from one of the open raster files
out_meta = source_files_to_mosaic[0].meta.copy() #source_files_to_mosaic[0] = first one of the files

# Update the metadata with new dimensions and crs
out_meta.update({"driver": "GTiff",
                 "height": mosaic.shape[1],
                 "width": mosaic.shape[2],
                 "transform": out_trans,
                 "crs": "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs "
                 }
                )


# Write the mosaic raster to disk
with rasterio.open(out_fp, "w", **out_meta) as dest:
    dest.write(mosaic)


