'''
SCRIPT NAME: ONS Hexmap Automation Tool - CORE CODE
SCRIPT DESCRIPTION: Code to generate BASIC hex-based Equal Area Cartogram
PROJECT CONCEPTION: Bruce Mitchell, January 2017
METHODOLOGY: Bruce Mitchell, George Tzelepis
SCRIPT AUTHORS: Code core written by George Tzelepis (Γιωργος Τζελέπης).
                Restructuring, additional code and annotations by Bruce Mitchell.

ONS Geography Branch, June 2019

 Input:   an ESRI shapefile
 Output:  an ESRI shapefile 

 Potentially, either input or output could be any boundary file format recognised by FIONA
'''


'''
===============================================================================
INITIAL SETUP
===============================================================================
'''

''' LIBRARY IMPORT '''

import time
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.pylab as pylab
#from scipy.spatial import voronoi_plot_2d as Voronoi
from scipy.spatial import Voronoi
import shapely.ops
from shapely.ops import polygonize
from shapely.ops import nearest_points
from shapely.geometry import Point
import geopandas
from geopandas import GeoDataFrame

import HexTool__Setup as parameters
INPUT_POLYGON_PATH = parameters.INPUT_POLYGON_PATH
OUTPUT_IMAGE_PATH = parameters.OUTPUT_IMAGE_PATH
OUTPUT_HEXMAP_PATH = parameters.OUTPUT_HEXMAP_PATH
OUTPUT_FILE_TYPE = parameters.OUTPUT_FILE_TYPE
GEOGRAPHY_NAME = parameters.GEOGRAPHY_NAME
HEXSIZE = parameters.HEXSIZE
HEXORIENTATION = parameters.HEXORIENTATION
COMPRESSION_FACTOR = parameters.COMPRESSION_FACTOR


''' NAMING THE HEXMAP '''
#
STYLE = "_B_HXMP"
MYHEXMAP = GEOGRAPHY_NAME + "__" + str(HEXSIZE) + "_" + str(HEXORIENTATION) + "__" + STYLE
print("My hexmap = " + MYHEXMAP) 
print("\n")

''' TIMING INITIALISATION '''

START_TIME = time.time()

'''
# *** VARIABLE RENAMES (from George Tzelepis' original code)***

# GT's "FeatClass" has been renamed to "INPUT_POLYGON"
# GT's "FeatCl" to "INPUT_POLYGON_CENTROIDS"
# GT's "featmultipoint" to "SHAPELY_MULTI_POINT"0


# GT's "centr" to "CENTROID_OF_CENTROIDS"
# GT's "geom" to "SELECTED_POINT"
# GT's "DISTANCES_from_centroid" to "DISTANCES_FROM_CxC"
# GT's "plt" to "pyplot"
# GT's "plb" to "pylab"
# GT's "grid" to "MESH".
# GT's "snap" to "SNAPLIST"
# GT's "final" to "SELECTED_HEXES_LIST"
# GT's "Final" to "HEXMAP_GDF"
'''

'''
===============================================================================
PART ONE: File inputs
===============================================================================
'''

'''
Import a specified geography file as geodataframe.
This example is an ESRI shapefile, read with Geopandas.
But any geography file type recognised by FIONA can be used.
'''

''' INPUT GEOGRAPHY '''
INPUT_POLYGON = geopandas.read_file(INPUT_POLYGON_PATH + GEOGRAPHY_NAME + '.shp')
''' *** INPUT GEOGRAPHY COORDINATE REFERENCE SYSTEM *** '''
CRS = INPUT_POLYGON.crs
#print(CRS)
#print("\n")

''' 
Display and save image of the original shapefile. These HAVE TO BE polygons. 
Points have to be converted beforehand, via generation of buffers.
'''
INPUT_POLYGON.plot()
pylab.savefig(OUTPUT_IMAGE_PATH + MYHEXMAP + '_INPUT_POLYGON.png')

'''
SEE IMPORTANT NOTE IN PART TWO (below)
'''

'''
===============================================================================
PART TWO: Creating the area centroids and the Centroid of Centroids (CxC)
===============================================================================
'''

'''
    Renaming "INPUT_POLYGON" (calling on the 'centroid' property), creates a 
    new GeoPandas 'GeoDataFrame', holding the centroids of the geometry.

IMPORTANT NOTE:
    After the following instruction, not only "INPUT_POLYGON_CENTROIDS" but also
    "INPUT_POLYGON" relates to the centroids, and no longer the input polygons.
    This why the "INPUT_POLYGON.plot()" and "pylab.savefig..." instructions
    have to be given at the end of Part One (above), when they still show the
    input polygons, rather than in Part Seven.
'''

INPUT_POLYGON_CENTROIDS = GeoDataFrame(INPUT_POLYGON, geometry=INPUT_POLYGON.centroid, crs=CRS)

'''
For viewing the centroids, it is easiest if the corresponding "INPUT_POLYGON_CENTROIDS.plot()"
and "pylab.savefig..." instructions are given here rather than in Part Seven.
"INPUT_POLYGON_CENTROIDS" soon becomes associated with the MESH: in Part Seven,
they would be plotted as HEXAGONS.
'''

''' If required, display and save image of the original shapefile centroids '''
#INPUT_POLYGON_CENTROIDS.plot()
#pylab.savefig(OUTPUT_IMAGE_PATH + GEOGRAPHY_NAME + "_" + str(HEXSIZE) + "_" + str(HEXORIENTATION) + '_b_INPUT_POLYGON_POINTS.png')

'''
From the centroids in this new geoDataFrame, create a SHAPELY object of
                            ... points ...
SHAPELY is faster than GEOPANDAS for calculation of centroids. This geometry 
will later be rejoined to the shapefile.
'''

SHAPELY_MULTI_POINT = shapely.geometry.MultiPoint(INPUT_POLYGON_CENTROIDS.geometry)

''' Calculate the CENTROID_OF_CENTROIDS (CxC) within the "SHAPELY_MULTI_POINT" ''' 

CENTROID_OF_CENTROIDS = SHAPELY_MULTI_POINT.centroid

''' 
Save the SHAPELY CENTROID_OF_CENTROIDS object 
as a GEOPANDAS GeoSeries named 'CENT_DF' (dataframe) 
'''

CENT_DF = geopandas.GeoSeries(CENTROID_OF_CENTROIDS, crs=CRS)

#print(CENT_DF.crs)
#print("\n")

'''
===============================================================================
PART THREE: CALCULATING THE DISTANCES FROM THE 'CxC' (abbrev. of 'CENTROID_OF_CENTROIDS')
===============================================================================
'''

'''
Calculate DISTANCES of points/areas from the median (origin) location.
(in FIONA)
    i.  Create a list: 'DISTANCES_FROM_CxC'
    ii. Populate the list

"SELECTED_POINT" is the name for the single centroid within the SHAPELY_MULTI_POINT
that is *currently* being compared for distance against the CxC.
The value of "DISTANCE_BETWEEN_PTS" for that point is then appended to
the list "DISTANCES_FROM_CxC"
'''

DISTANCES_FROM_CxC = []
for feature in SHAPELY_MULTI_POINT:
    SELECTED_POINT = shapely.geometry.point.Point(feature)
    DISTANCE_BETWEEN_PTS = CENTROID_OF_CENTROIDS.distance(SELECTED_POINT)
    DISTANCES_FROM_CxC.append(DISTANCE_BETWEEN_PTS)
   
'''
Add a new field ("distance") to the INPUT_POLYGON_CENTROIDS
Update it for all points from the list "DISTANCES_FROM_CxC"
'''    

INPUT_POLYGON_CENTROIDS['distance'] = DISTANCES_FROM_CxC

'''
Create a NUMPY array called "DISTANCES" to contain the value "DISTANCES_FROM_CxC" 
'''

DISTANCES = numpy.array(DISTANCES_FROM_CxC)

'''
Recalibrate the areas to set the median centroid in the CxC_DataFrame to
the 'origin' location (0,0).
This enables us to standardise the distances between the centroids of the the
'target' geographical units that are the subject of our hexmap and the median
'centroid of centroids (CxC) location. 
Also to to easily locate them N S E and W of the CxC.
'''

'''
===============================================================================
PART FOUR: CALCULATING the ANGLES
4:1 - "gonia"
===============================================================================
'''

'''
ONLY REQUIRED FOR COMPRESSED HEXMAPS
'''

'''
===============================================================================
PART FOUR: CALCULATING "THE BEARINGS"
  4:2 - "BEARING"
===============================================================================
'''

'''
ONLY REQUIRED FOR COMPRESSED HEXMAPS
'''

'''
===============================================================================
# PART FIVE: APPLYING THE GRAVITY FUNCTION (COMPRESSION)
===============================================================================
'''

'''
ONLY REQUIRED FOR COMPRESSED HEXMAPS
'''


'''
===============================================================================
PART SIX: CREATING THE HEX MESH AND SNAPPING TO IT
===============================================================================
'''

''' For BASIC hexmap - using the original points to create the MESH '''

INPUT_POLYGON_CENTROIDS = GeoDataFrame(INPUT_POLYGON_CENTROIDS, crs=CRS)

''' For COMPRESSED hexmap - using the transformed points to create the MESH '''

#INPUT_POLYGON_CENTROIDS = GeoDataFrame(INPUT_POLYGON_CENTROIDS, crs=CRS, geometry=GEOMETRY1)

#print(INPUT_POLYGON_CENTROIDS.crs)
#print("\n")


# If using the raw (non-transformed) points to create the MESH
INPUT_POLYGON_CENTROIDS = INPUT_POLYGON_CENTROIDS.sort_values('distance', ascending=1)
INPUT_POLYGON_CENTROIDS = INPUT_POLYGON_CENTROIDS.reset_index(drop=True)

'''
The Minimum bounding Rectangle (MBR) limits of the HEX CENTROIDS geography 
for which you will create the hex MESH

This embraces the extent of the HEX CENTROIDS only.
'''


minX = INPUT_POLYGON_CENTROIDS.geometry.x.min()
minY = INPUT_POLYGON_CENTROIDS.geometry.y.min()
maxX = INPUT_POLYGON_CENTROIDS.geometry.x.max()
maxY = INPUT_POLYGON_CENTROIDS.geometry.y.max()

#print(minX)
#print(minY)
#print(maxX)
#print(maxY)
#print("\n")

'''
Create a MESH of points to sit behind the transformed geography

NOTES:    HEXORIENTATION  1 = pointy-uppy
          HEXORIENTATION  2 = flatty-uppy
          HEXSIZE = magnitude. 1 unit of HEXSIZE == 1 unit of input goegoraphy's CRS
'''

if HEXORIENTATION == 1:
    x1 = numpy.arange(minX - 4 * HEXSIZE, maxX + 4 * HEXSIZE, HEXSIZE)
    y1 = numpy.arange(minY - 2 * ((3 * HEXSIZE) / numpy.sqrt(3)), maxY + 2 * ((3 * HEXSIZE) / numpy.sqrt(3)), (3 * HEXSIZE) / numpy.sqrt(3))
#''' create the MESH based on these arrays '''
    X1, Y1 = numpy.meshgrid(x1, y1)
    X1 = X1.reshape((numpy.prod(X1.shape),))
    Y1 = Y1.reshape((numpy.prod(Y1.shape),))
#''' create one-dimensional arrays x2 and y2 '''
    x2 = numpy.arange((minX + float(HEXSIZE) / 2) - 4 * HEXSIZE, (maxX + HEXSIZE / 2) + 4 * HEXSIZE, HEXSIZE)
    y2 = numpy.arange((minY + 3 * HEXSIZE / (2 * numpy.sqrt(3))) - 2 * ((3 * HEXSIZE) / numpy.sqrt(3)), (maxY + 3 * HEXSIZE / (2 * numpy.sqrt(3))) + 2 * ((3 * HEXSIZE) / numpy.sqrt(3)), (3 * HEXSIZE) / numpy.sqrt(3))
#''' create the MESH based on these arrays '''
    X2, Y2 = numpy.meshgrid(x2, y2)
    X2 = X2.reshape((numpy.prod(X2.shape),))
    Y2 = Y2.reshape((numpy.prod(Y2.shape),))
elif HEXORIENTATION == 2:
    y1 = numpy.arange(minY - 3 * HEXSIZE, maxY + 3 * HEXSIZE, HEXSIZE)
    x1 = numpy.arange(minX - 2 * ((3 * HEXSIZE) / numpy.sqrt(3)), maxX + 2 * ((3 * HEXSIZE) / numpy.sqrt(3)), (3 * HEXSIZE) / numpy.sqrt(3))
    X1, Y1 = numpy.meshgrid(x1, y1)
    X1 = X1.reshape((numpy.prod(X1.shape),))
    Y1 = Y1.reshape((numpy.prod(Y1.shape),))
    y2 = numpy.arange((minY + float(HEXSIZE) / 2) - 3 * HEXSIZE, (maxY + HEXSIZE / 2) + 3 * HEXSIZE, HEXSIZE)
    x2 = numpy.arange((minX + 3 * HEXSIZE / (2 * numpy.sqrt(3))) - 2 * ((3 * HEXSIZE) / numpy.sqrt(3)), (maxX + 3 * HEXSIZE / (2 * numpy.sqrt(3))) + 2 * ((3 * HEXSIZE) / numpy.sqrt(3)), (3 * HEXSIZE) / numpy.sqrt(3))
    X2, Y2 = numpy.meshgrid(x2, y2)
    X2 = X2.reshape((numpy.prod(X2.shape),))
    Y2 = Y2.reshape((numpy.prod(Y2.shape),))

Xg = numpy.append(X1, X2)
Yg = numpy.append(Y1, Y2)
#print(x1)
#print(y1)
#print(x2)
#print(y2)
#print("\n")
#print(INPUT_POLYGON_CENTROIDS.crs)
#print("\n")
#print(X1)
#print(Y1)
#print(X2)
#print(Y2)
#print("\n")

''' Turn the numpy array into 'GEOMETRY2' = the points from which the MESH will be created. '''
 
GEOMETRY2 = [Point(xy) for xy in zip(Xg, Yg)]

''' We create a shapely multipoint geometry object from 'GEOMETRY2' '''

MESH = shapely.geometry.MultiPoint(GEOMETRY2)

'''
Apply scipy.spatial's 'Voronoi' routine to the MESH of points to create...
                    ... 'VORONOI_BDY' ... 
At present, they are just separate lines rather than polygon boundaries, 
buit they will form the boundaries for a MESH of HEXES.
'''


VORONOI_BDY = Voronoi(MESH)

''' These 'VORONOI_BDY' LINES are then {placed in a list?} called 'LINES'. '''

LINES = [
    shapely.geometry.LineString(VORONOI_BDY.vertices[line])
    for line in VORONOI_BDY.ridge_vertices
    if -1 not in line
]

''' 
NEXT, WE CONVERT THESE LINES INTO HEXAGONS.
"HEXES" = a list of the individual HEXAGONS 
created by using the function 'polygonize' on the LINES.
''' 

HEXES = list(polygonize(LINES))

'''
Hexagon MESH generated by use of Shapely geometry method, 
with 'multipolygon' format
'''

''' 
Is this line (below) supposed to be commented out ???
'HEXPOLYGONS' does not appear elsewhere.
'''

# HEXPOLYGONS = shapely.geometry.MultiPolygon(HEXES)

'''
Create a list named 'SNAPLIST', which will enumerate each transformed point 
along with the point on the MESH to which it will be SNAPPED.
'''

SNAPLIST = []

'''
Determine the sequence of nearness of the transformed points to the CxC.

In that sequence, snap each of the transformed points in turn to their 
nearest (available) hexagon MESH centroid. 

Once a hex MESH centroid is 'taken', is is no longer available.

"GEOMETRY1" ... our transformed points
"GEOMETRY2" ... the points from which the MESH has been created.

The loop below selects the HEXES from the MESH that contain 
                ... INPUT_POLYGON_CENTROIDS ...

Selected HEXES (only) are held in a list called 'SELECTED_HEXES_LIST' to snap 
to the closest available points to the MESH.

'''

for i in INPUT_POLYGON_CENTROIDS.geometry:
    MESH = shapely.geometry.MultiPoint(GEOMETRY2)
    ''' k consists of 't1' geometry of the INPUT_POLYGON_CENTROIDS, 't2' the geometry of the MESH '''
    k = nearest_points(i, MESH)
    t1, t2 = k
    SNAPLIST.append(t2)
    ''' the MESH point to which your point is being SNAPPED is then removed. '''
    GEOMETRY2.remove(t2)
    ''' that point is therefore no longer available to be SNAPPED to. '''

SNAPPED = shapely.geometry.MultiPoint(SNAPLIST)

SELECTED_HEXES_LIST = []

#print(SELECTED_HEXES_LIST)
#print("\n")

''' populating 'SELECTED_HEXES_LIST' '''

for i in SNAPPED:
    for h in HEXES:
        con = h.contains(i)
        if con == True:
            SELECTED_HEXES_LIST.append(h)


'''selecting a list of HEXAGONS with the SNAPPED centroids '''
HEXAGONS = geopandas.GeoSeries(SELECTED_HEXES_LIST)

#print(SELECTED_HEXES_LIST)
#print(HEXAGONS)
#print("\n")

'''
Creating a geodataframe which has three components:
the featureclass, the geometry and the projection
'''
HEXMAP_GDF = GeoDataFrame(INPUT_POLYGON_CENTROIDS, geometry=HEXAGONS.geometry, crs=CRS)
HEXMAP_GDF.crs = INPUT_POLYGON_CENTROIDS.crs
#print(HEXMAP_GDF.crs)
#print("\n")

'''
===============================================================================
PART SEVEN - GENERATING OUTPUT
===============================================================================
'''

''' A. GEOGRAPHY OUTPUT

The format of the OUTPUT is set at the end of HexTool__Parameters.py

The output hexmap is named on the pattern of the input geography and settings.

'''

''' for ESRI shapefile '''

''' THE HEXMAP '''
OUTPUT_HEXMAP = OUTPUT_HEXMAP_PATH + MYHEXMAP
HEXMAP_GDF.to_file(OUTPUT_HEXMAP, driver='ESRI Shapefile')         

''' THE CxC '''
OUTPUT_HEXMAPCxC = OUTPUT_HEXMAP_PATH + MYHEXMAP + "_CxC."
CENT_DF.to_file(OUTPUT_HEXMAPCxC, driver='ESRI Shapefile')


''' For OCG GeoPackage '''

''' THE HEXMAP '''
#OUTPUT_HEXMAP = OUTPUT_HEXMAP_PATH + MYHEXMAP
#HEXMAP_GDF.to_file(OUTPUT_HEXMAP, driver='GPKG') 
                             
''' THE CxC '''
#OUTPUT_HEXMAPCxC = OUTPUT_HEXMAP_PATH + MYHEXMAP
#HEXMAP_GDF.to_file(OUTPUT_HEXMAPCxC, driver='GPKG') 

                            
HEXMAP_GDF['coords'] = HEXMAP_GDF['geometry'].apply(lambda x: x.representative_point().coords[:])
HEXMAP_GDF['coords'] = [coords[0] for coords in HEXMAP_GDF['coords']]


''' B. IMAGE OUTPUT ''' 


OUTPUT_HEXMAPCxC = OUTPUT_HEXMAP_PATH + MYHEXMAP + "_CxC."

''' Display and save image of the centroid of centroids '''

#CENT_DF.plot()
#pylab.savefig(OUTPUT_IMAGE_PATH + MYHEXMAP + '_GeoPandas_CxC_dataframe.png')

''' Display and save image of the distances of the original GEOGRAPHY centroids from their CxC '''

HEXMAP_GDF.plot(column='distance', scheme='QUANTILES', k=5, cmap='OrRd', legend=True)
pylab.savefig(OUTPUT_IMAGE_PATH + MYHEXMAP + '_distances.png')

''' Display and save image of the distances of the transformed GEOGRAPHY centroids from the original CxC '''

#HEXMAP_GDF.plot(column='trans_distance', scheme='QUANTILES', k=5, cmap='OrRd', legend=True)
#pylab.savefig(OUTPUT_IMAGE_PATH + MYHEXMAP + '_xformed_distances.png')

''' Display and save image of the processed hexmap '''

HEXMAP_GDF.plot()
pylab.savefig(OUTPUT_IMAGE_PATH + MYHEXMAP + '.png')

'''
For a labelled hexmap (for testing only)
    Note - this takes a LONG time with more detailed geographies
    Better results are achieved in a GIS in any event!
    The field that supplies the label should be named within code phrase:
        s=row['myfieldname'] ... in this example, 'AreaName'
'''

#for idx, row in HEXMAP_GDF.iterrows():
#    pyplot.annotate(s=row['AreaName'], xy=row['coords'], horizontalalignment='center')
#    pylab.savefig(OUTPUT_IMAGE_PATH + MYHEXMAP + '_LabelledHexmap.png')

'''
===============================================================================
PART EIGHT - CLEANUP
===============================================================================
'''

#print(HEXMAP_GDF.crs)
#print("\n")

END_TIME = time.time()

print("Generation of  '" + MYHEXMAP + "'  took: {}".format(END_TIME - START_TIME) + " seconds")
print("\n")   

del HEXAGONS, con, t1, t2, x2, y2, HEXMAP_GDF, INPUT_POLYGON_CENTROIDS, SELECTED_HEXES_LIST, SNAPPED, SNAPLIST, HEXES, LINES, VORONOI_BDY, minX, minY, maxX, maxY, GEOMETRY2, Xg, Yg, Y1, X1, Y2, X2, CENTROID_OF_CENTROIDS, CENT_DF, DISTANCES, DISTANCE_BETWEEN_PTS, DISTANCES_FROM_CxC, SELECTED_POINT, MESH, i, k, SHAPELY_MULTI_POINT, HEXSIZE, polygonize, START_TIME, parameters, INPUT_POLYGON_PATH, OUTPUT_IMAGE_PATH, OUTPUT_HEXMAP_PATH, GEOGRAPHY_NAME, HEXORIENTATION, COMPRESSION_FACTOR, OUTPUT_FILE_TYPE, MYHEXMAP, STYLE
