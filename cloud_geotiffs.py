# -*- coding: utf-8 -*-
"""
Read cloud optimised geotiffs

Created on Wed Nov 14 15:05:45 2018

@author: Faris Alsuhail
"""

import rasterio
import matplotlib.pyplot as plt
import numpy as np

# Specify the path for Landsat TIF on AWS
url = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'



# See the profile
src = rasterio.open(url)
print(src.profile)
    
#Get the list overviews
oviews = src.overviews(1)
oview = oviews[-1] #retrieve the smallest thumbnail

#Read image thumbnail using low resolution source
thumbnail = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))

#plot overview
show(thumbnail, cmap='viridis')

#Retrieve a "Window" (a subset) from full resolution raster
window = rasterio.windows.Window(1024, 1024, 1280, 2560) #(offsets and size)

with rasterio.open(url) as src:
    subset = src.read(1, window=window)
    
plt.figure(figsize=(6,8.5))
plt.imshow(subset)
plt.colorbar(shrink=0.5)
#plt.title(f'Band 4 Subset\n{window}')
plt.xlabel('Column #')
plt.ylabel('Row #')
