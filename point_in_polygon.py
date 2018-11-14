# -*- coding: utf-8 -*-
"""
point_in_polygon.py

Point in polygon and intersect operations with python


Created on Tue Nov 13 13:50:28 2018

@author: Faris Alsuhail
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import shapely.speedups

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
shapely.speedups.enable()

#Filepath for KML file
fp = "L4_data/PKS_suuralue.kml"

#Filepath for addresses
fpa = "L4_data/addresses.shp"

suuralueet = gpd.read_file(fp, driver = 'KML')
addresses = gpd.read_file(fpa)

#suuralueet.plot()

southern = suuralueet.loc[suuralueet['Name'] == 'Eteläinen']
southern = southern.reset_index(drop=True) #drop-arvo pitää kirjoittaa isolla alkukirjaimella

#Conduct point in polygon query

pip_mask = addresses.within(southern.loc[0, 'geometry'])


#Select points that are within polygon
pip_addresses = addresses.loc[pip_mask]

# Plot
ax = suuralueet.plot(facecolor='green')
southern.plot(ax=ax, facecolor='blue')
pip_addresses.plot(ax=ax, color='gold', markersize=5)
plt.tight_layout()