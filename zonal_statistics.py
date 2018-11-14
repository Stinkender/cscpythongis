# -*- coding: utf-8 -*-
"""
How to calculate zonal statistics using rasterio and rasterstats.

Created on Wed Nov 14 13:53:25 2018

@author: Faris Alsuhail
"""

import rasterio
from rasterio.plot import show
from rasterstats import zonal_stats
import osmnx as ox
import geopandas as gpd
import os
import matplotlib.pyplot as plt

#Filepaths
data_dir = "L5_data"
dem_fp = os.path.join(data_dir, "Helsinki_DEM2x2m_Mosaic2.tif")

#Read the data
dem = rasterio.open(dem_fp)

#Fetch polygons for zonal stats from OSM
kallio_q = "Kallio, Helsinki, Finland"
pihlajamaki_q = "Pihlajamäki, Malmi, Helsinki, Finland"

#Retrieve the geometries of the areas
kallio = ox.gdf_from_place(kallio_q)
pihlajamaki = ox.gdf_from_place(pihlajamaki_q)

#Reproject fetched geometries to same CRS with DEM
kallio = kallio.to_crs(crs = "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs ")
pihlajamaki = pihlajamaki.to_crs(crs ="+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs ")


# Plot the Polygons on top of the DEM
ax = kallio.plot(facecolor='None', edgecolor='yellow', linewidth=2)
ax = pihlajamaki.plot(ax=ax, facecolor='None', edgecolor='orange', linewidth=2)

# Plot DEM
show((dem, 1), ax=ax)

#Use zonal stats to asses which area is higher
#---------------------------------------------

#Read the data from DEM
array = dem.read(1) #read channel 1

#Get the affine from DEM
affine = dem.transform

# Calculate zonal statistics for Kallio geometry
zs_kallio = zonal_stats(kallio, array, affine=affine, stats=['min', 'max', 'mean', 'median', 'majority'])


# Calculate zonal statistics for Pihlajamäki geometry
zs_pihlajamaki = zonal_stats(pihlajamaki, array, affine=affine, stats=['min', 'max', 'mean', 'median', 'majority'])

print(zs_kallio)
print(zs_pihlajamaki)



#Which has a higher max point?
if zs_kallio[0]['max'] > zs_pihlajamaki[0]['max']:
    print("Kallio on korkiampi")
else:
    print("Pihlajamäki on korkiampi")

erotus = zs_kallio[0]['max'] - zs_pihlajamaki[0]['max']
print(erotus)




































