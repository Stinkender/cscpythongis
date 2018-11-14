# -*- coding: utf-8 -*-
"""
geopandas_testi.py

Requirements:
    -geopandas

Notes:
    -Introduction to Geopandas exercise

Created on Mon Nov 12 13:15:46 2018

@author: Faris Alsuhail
"""

#Import necessary modules
import geopandas as gpd
import pandas as pd #not necessary
import fiona as fn

#Set filepath
fp = "L2_data/DAMSELFISH_distributions.shp"

#Read file using gpd.read_file()
data = gpd.read_file(fp)

#View two first rows
print(data.head(2))

#Print column names from GeoDataFrame
cols = data.columns
print(cols)

#Plot the map
data.plot()

#WRITE A SHAPEFILE
#----------

#Specify output filepath
outfp = "L2_data/DAMSELFISH_distributions_selection.shp"
outfp2 = "L2_data/DAMSELFISH_distributions_selection.geojson"

#Select first 50 rows
selection = data[0:50]


#Write selection into a new Shapefile
selection.to_file(outfp)
selection.to_file(outfp2, driver = 'GeoJSON')

#GEOMETRIES IN GeoDataFrame
#----------
data.columns
sel3 = data[['geometry', 'BINOMIAL']].head()

#Select rows based on criteria
#List unique species
unique_species = data['BINOMIAL'].unique()
print(unique_species)

#species we are interested in
criteria = 'Chromis cyanea'

fish_a = data.loc[data['BINOMIAL'] == criteria]
print(fish_a)

#You can even write the selection!
outfp3 = "L2_data/DAMSELFISH_distributions_fish_a_selection.geojson"
fish_a.to_file(outfp3, driver = 'GeoJSON')

#POSTGIS TRICKS
# import psycopg2 #
# Initialise connection with driver such as psycopg2
# conn, cursor = psycopg2.connect() #
# pgdata = gpd.read_postgis(sql="SELECT *  FROM TABLEX;", con = conn) #

#Iterate over geodataframe
selection2 = data[0:5]

#alternative 1 iterate over geodataframe
for index, row in selection2.iterrows():
    #calculate the area of each Polygon
    poly_area = row['geometry'].area
    #print them to me!
    print(poly_area)

#alternative 2 iterate over geodataframe
def calculate_area(row):
    return row['geometry'].area

data['area2']  = data.apply(calculate_area, axis = 1)

#alternative 3 iterate over geodataframe
data['area']  = data.apply(lambda row: row['geometry'].area, axis = 1)


    #print("Polygon area at index {index} is: {area:.3f}".format(index=index, area=poly_area))

#Geometric attributes from GeoDataFrame
#----------

#Calculate the area using geopandas directly
data['area3'] = data.area
data['centroid'] = data.centroid

#Set the geometry source for geodataframe

geo = data.copy()
geo = geo.set_geometry('centroid')
geo.plot()

#Drop the 'geometry' column from geodataframe
geo = geo.drop('geometry', axis = 1)
#save points
geo.to_file('geom_centroids.shp')

#Calculate basic stats
mean_area = geo['area'].mean()
print(mean_area)
min_area = geo['area'].min()
print(min_area)

#Calculate in (geo)dataframe
geo['areaX2'] = geo['area'] + geo['area2']









































