# -*- coding: utf-8 -*-
"""
read_raster.py

Reading raster files with rasterio.

Created on Wed Nov 14 09:13:40 2018

@author: Faris Alsuhail
"""

import rasterio
import os
import numpy as np

#Data directory
#data_dir = "L5_data" #This is in IntroGIS_faris folder
data_dir = r"C:\IntroGIS_faris" #with r in front, python won't interpret anything, so '\' are ok
filepath = os.path.join(data_dir, "L5_data", "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")
print(filepath)

#Open the file
raster = rasterio.open(filepath)
type(raster)

#check projection
raster.crs

#affine transform
raster.transform

#dimensions of the raster
raster.width
raster.height

#number of channels (eli bands)
raster.count

#bounds of the file
raster.bounds

#driver
raster.driver

#No data value (for all bands)
raster.nodatavals

#All metadata at once
raster.meta

#Read the data values to python
#------------------------------

#read the first band as a separate variable
band1 = raster.read(1)

#check type for variable "band1"
print(type(band1))

#Calculate basic stats
#---------------------

#read all bands
array = raster.read()


#calculate stats for each band
stats = [] #put the stats inside a list
for band in array: #create a for loop for band
    stats.append({
            'min': band.min(),
            'mean': band.mean(),
            'median': np.median(band),
            'max': band.max()
            })
    
#show stats for each band
stats


