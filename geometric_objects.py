# -*- coding: utf-8 -*-
"""
geometric_objects.py



Introduction to Shapely geometric objects and functionalities.

Requirements:
    -shapely

Notes:
    -This is probably the best python script ever scripted in the history of scripting.

Created on Mon Nov 12 10:59:03 2018

@author: Faris Alsuhail
"""

#import necessary geometric objects from shapely module
#one could also use 'import shapely', but not necessary in this case
from shapely.geometry import Point, LineString, Polygon

#POINT
#----------

#Let's create point objects!
point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point3D = Point(9.26, -2.456, 0.57)

#Get the coordinates
point_coords = point1.coords

#Get xy coordinates
xy = point1.xy
print(xy)

#Get x and y coordinate
x = point1.x
y = point1.y

#Calculate distance between point1 and point2
point_dist = point1.distance(point2)
print(point_dist)

#Create a buffer with 20 units
point_buffer = point1.buffer(20)


#LINESTRING
#----------

#Let's do a line based on the points made earlier!
line = LineString([point1, point2, point3])

#Here's a line made with coordinate tuples
line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

#Coordinates
lxy = line.xy
print(lxy)

#Get x and y coordinates
x = line.xy[0]
y = line.xy[1]

#Get the lenght
l_length = line.length
print(l_length)

#Get the centroid of the line
l_centroid = line.centroid
print(l_centroid)


#POLYGON
#----------

#Create a polygon based on coordinate tuples
poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

#Create a polygon based on Points
point_list = [point1, point2, point3]
poly2 = Polygon([(p.x, p.y) for p in point_list])

#Get geometry type as string
poly_type = poly.geom_type

#Calculate polygon area
poly_area = poly.area

#Polygon centroid
poly_centroid = poly.centroid.coords.xy
#centroid_coords = poly_centroid.coords
#centroid_xy = centroid_coords.xy


#Bounding box
poly_bbox = poly.bounds

#Create bbox geometry
from shapely.geometry import box

#Unpack the bounding box coordinates with an asterisk
bbox = box(*poly_bbox)

#Get exterior
poly_exterior = poly.exterior

#Lenght of exterior
poly_ext_lenght = poly.exterior.length

# Let's create a bounding box of the world and make a whole in it
# First we define our exterior
world_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]

# Let's create a single big hole where we leave ten decimal degrees at the boundaries of the world
# Notice: there could be multiple holes, thus we need to provide a list of holes
hole = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]

world_poly = Polygon(shell = world_exterior, holes = hole)
