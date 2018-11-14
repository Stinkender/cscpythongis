# -*- coding: utf-8 -*-
"""
spatial_join.py

Here we do spatial joins because we can

Created on Tue Nov 13 14:44:30 2018

@author: Faris Alsuhail
"""

import geopandas as gpd

#filepath for vaestoruudut
fp = "L4_data/Vaestotietoruudukko_2015.shp"

#filepath for addresses
fpp = "L4_data/addresses.shp"

pop = gpd.read_file(fp)
points = gpd.read_file(fpp)

pop.head()
points.head()

#Ensure the data are in the same crs
points = points.to_crs(crs=pop.crs)


assert points.crs == pop.crs, "MEIN GOTT! The CRS of the layers do not match"

#Make spatial join

join = gpd.sjoin(points, pop, how="inner", op="within") #point within pop polygons, inner join
join.head()

#Visualise
join.plot(column='ASUKKAITA', cmap="Reds", markersize=join['ASUKKAITA'])
