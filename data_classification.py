# -*- coding: utf-8 -*-
"""
Classify data values based on common classifiers.

Created on Tue Nov 13 13:08:54 2018

@author: Faris Alsuhail
"""

import geopandas as gpd
import pysal as ps
import matplotlib.pyplot as plt

#Filepath
fp = "L3_data/TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"

#Read the data
data = gpd.read_file(fp)

#Print 2 first rows
#print(data.head(2))

#Exclude -1 values, i.e. select rows where values >=0
data = data.loc[data['pt_r_tt'] >= 0]

#Plot data with Fisher-Jenks with 9 classes
data.plot(column="pt_r_tt", scheme="Fisher_Jenks", k=9, cmap="cool", linewidth=0, legend=True)

#use tight layout
plt.tight_layout()


#Define number of classes
k = 12

#Initialise the natural breaks classifier
classifier = ps.Natural_Breaks.make(k=k)

#Classify the travel time values
classifications = data[['pt_r_tt']].apply(classifier)

#Rename column pt_r_tt in classifications to nb_pt_r_tt
classifications = classifications.rename(columns={'nb_r_tt': 'nb_pt_r_tt'}) #can also rename multiple columns at the same time

#join classifications based on index value
data  = data.join(classifications)

ax = data.plot(column="nb_pt_r_tt", linewidth=0, legend=True, cmap="plasma")


#Create custom classifier
class_bins = [10, 20, 30, 40, 50, 60]
c_classifier = ps.User_Defined.make(class_bins)


c_classifications = data[['pt_r_tt']].apply(c_classifier) #creates the c_classification table with the defined classes
c_classifications = c_classifications.rename(columns={'pt_r_tt': 'c_pt_r_tt'}) #can also rename multiple columns at the same time
data  = data.join(c_classifications) #join classified values to data table

ax = data.plot(column="c_pt_r_tt", linewidth=0, legend=True, cmap="plasma")
