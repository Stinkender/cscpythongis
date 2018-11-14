# -*- coding: utf-8 -*-
"""
raster_algebra.py

How to do raster calculations using rasterio and numpy


Created on Wed Nov 14 12:58:33 2018

@author: Faris Alsuhail
"""


import rasterio
import numpy as np
from rasterio.plot import show
import os
import matplotlib.pyplot as plt

#Set the data directory
data_dir = "L5_data"

fp = os.path.join(data_dir, "Helsinki_Masked.tif")

#Open the data
raster = rasterio.open(fp)

#Read channels/bands for red and NIR, channel number inside ()
red = raster.read(3)
nir = raster.read(4)

show(nir, cmap='terrain_r')

#convert to floats
red = red.astype('f4')
nir = nir.astype('f4')

"""
we need to tweak the behaviour of numpy a little bit.
By default numpy will complain about dividing with zero values.
We need to change that behaviour because we have a lot of 0 values
in our data.
"""
np.seterr(divide='ignore', invalid='ignore')


#Calculate NDVI

ndvi = (nir - red) / (nir + red)

#Plot ndvi with legend
plt.imshow(ndvi, cmap="plasma_r")
plt.colorbar()
