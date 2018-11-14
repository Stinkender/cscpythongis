# -*- coding: utf-8 -*-
"""
map_projections.py

Map projections

Created on Mon Nov 12 15:25:05 2018

@author: Faris Alsuhail
"""

# Import necessary packages
import geopandas as gpd
import matplotlib.pyplot as plt

# Read the file
fp = "L2_data/Europe_borders.shp"
data = gpd.read_file(fp)

data.columns
data.head()

# Check the coordinate reference system
data.crs

data['geometry'].head()

#Copy the data
orig = data.copy()

#Reproject the data
data = data.to_crs(epsg=3035)
data.plot()

#Check the new geometry values
print(data['geometry'].head())

#Let's compare! Make subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,8))

#Plot the data in LAEA, gray
orig.plot(ax=ax1, facecolor='gray');

#add title
ax1.set_title("WGS84");

#Plot the data in WGS84, blue
data.plot(ax=ax2, facecolor='blue');

#add title
ax2.set_title("Lambert azimuthal");

plt.tight_layout()

#save
plt.savefig("projections.png", dpi=300)

outfp = "L2_data/Europe_borders_3035.shp"
data.to_file(outfp)

#If crs not working in output
#import pycrs
#proj4 =  pycrs.parser.from_epsg_code(3035).to_proj()
#geo.crs = proj4