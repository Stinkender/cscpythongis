# -*- coding: utf-8 -*-
"""
raster_plotting.py

Created on Wed Nov 14 09:56:05 2018

@author: Faris Alsuhail
"""
import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
import numpy as np
import os
import matplotlib.pyplot as plt


#Raster source
data_dir = r"C:\IntroGIS_faris" #with r in front, python won't interpret anything, so '\' are ok
filepath = os.path.join(data_dir, "L5_data", "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")


#Open the file
raster = rasterio.open(filepath)


#Plot band 1
show((raster,1), cmap='inferno')

#Another way to plot channel 1
show(raster.read(1), cmap='Greens')

#How different bands look like?
#------------------------------

#Initialise subplots
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, nrows=1, figsize=(10, 4), sharey=True)
#how many plots, how many columns, how many rows, figure size, share y-axis

#Plot r, g, b bands
show((raster, 3), cmap='Reds', ax=ax1)
show((raster, 2), cmap='Greens', ax=ax2)
show((raster, 1), cmap='Blues', ax=ax3)

#Add titles to figures
ax1.set_title("Red")
ax2.set_title("Green")
ax3.set_title("Blue")

#True color composite
#--------------------

#Read grid values into numpy arrays
red = raster.read(3)
green = raster.read(2)
blue = raster.read(1)

#Cell values need to be normalised into scale 0.0 - 1.0, we define a function below. It can be used later on for other bands, too!
#We can also have this function in a separate file (in same directory) and we can import it with e.g. 'from raster_tools import normalize'
def normalize(array):
    """Normalizes numpy arrays into scale 0.0 - 1.0"""
    array_min, array_max = array.min(), array.max()
    return ((array - array_min)/(array_max - array_min))

red_normalised = normalize(red)
green_normalised = normalize(green)
blue_normalised = normalize(blue)

print("Normalized bands")
print(red_normalised.min(), '-', red_normalised.max(), 'mean:', red_normalised.mean())
print(green_normalised.min(), '-', green_normalised.max(), 'mean:', green_normalised.mean())
print(blue_normalised.min(), '-', blue_normalised.max(), 'mean:', blue_normalised.mean())

# Create RGB natural color composite
rgb = np.dstack((red_normalised, green_normalised, blue_normalised))

# Let's see how our color composite looks like
plt.imshow(rgb)

#Read and normalise NIR band
nir = raster.read(4)
nir_normalised = normalize(nir)

#Create the composite stacking
nrg = np.dstack((nir_normalised, red_normalised, green_normalised))

#Show the composite
plt.imshow(nrg)

#Show histogram
show_hist(raster, bins=50,lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histamiini")


