'''
SCRIPT NAME: ONS Hexmap Automation Tool - SETUP
SCRIPT DESCRIPTION: User-editable parameters for generation of hex-based Equal Area Cartograms
PROJECT CONCEPTION: Bruce Mitchell, January 2017
METHODOLOGY: Bruce Mitchell, George Tzelepis
SCRIPT AUTHORS: Code core written by George Tzelepis (Γιωργος Τζελέπης).
                Restructuring, additional code and annotations by Bruce Mitchell.

ONS Geography Branch, June 2019

# Input:   an ESRI shapefile - but potentially, any boundary file format recognised by FIONA
# Output:  an ESRI shapefile

'''

'''
===============================================================================
I N I T I A L   S E T U P 
===============================================================================
'''

'''
.............................................
PATHS and FOLDERS
.............................................
'''

'''
Ensure these paths / folders are created before you run the code!
ROOT LOCATION
'''


#ROOT_FOLDER = r'C:/HEXMAPS_beta/'   # - ONS - ONS27797
#ROOT_FOLDER = r'D:/HEXMAPS_beta/' 	# - ONS - geoCentaurs
ROOT_FOLDER = r'G:/HEXMAPS_beta/' 	# - HOME - MESH II

# INPUT GEOGRAPHY PATH
INPUT_POLYGON_PATH = ROOT_FOLDER + 'GIS/Input/Geometry/'
# OUTPUT PATHS
# * Saved figure images *
OUTPUT_IMAGE_PATH = ROOT_FOLDER + 'GIS/Output/Image/'
# * Hexagon geometry files *
OUTPUT_HEXMAP_PATH = ROOT_FOLDER + 'GIS/Output/Geometry/'
#


'''
.............................................
WHICH GEOGRAPHY DO YOU WANT TO HEXMAP? 
.............................................
'''

''' United Kingdom '''
import HexTool__Geographies_UK as geographies

''' Elsewhere '''
#import HexTool__Geographies_Elsewhere as geographies

GEOGRAPHY_NAME = geographies.GEOGRAPHY_NAME
HEXSIZE = geographies.HEXSIZE
HEXORIENTATION = geographies.HEXORIENTATION
COMPRESSION_FACTOR = geographies.COMPRESSION_FACTOR



'''
.............................................
WHAT TYPE OF HEXMAP DO YOU WANT TO CREATE?
.............................................
'''

''' For BASIC HEXMAP '''
#import HexTool__Basic

''' Or, for COMPRESSED HEXMAP ''' 

import HexTool__Compressed 

'''
.............................................<built-in method mean of numpy.ndarray object at 0x000000000F4F06C0>810

F_CORRECTION
.............................................
'''

''' 
'f' is the 'gravity function' which, in the 'Compressed' script, pulls 
the centroids towards the CxC. It impinges on instances MORE more with 
increasing distance * from the CxC.

Counter-intuitively, it is at its *strongest when zero* and *weakest when 1.

At high compression rates (i.e. CF < 2), peripheral instances can 'overtake' 
interior instances during the transformation towards the CxC 

Any hexes with actual 'f' value of zero will be pulled *right onto* the CxC.

So F_CORRECTION sets minimum f to 0.1. 

Values below this will be set to 0.1. 
'''

F_CORRECTION = 0.3

#F_CORRECTION = 0.1
#F_CORRECTION = 0.05
#F_CORRECTION = 0.01 

'''
.............................................
OUTPUT FILE FORMAT
.............................................
'''

'''
Choose the format of the OUTPUT FILE 
ESRI shapefiles (shp) are supported.
Support for OGC GeoPackage(gpkg)is being developed, but not yet implemented.
'''

OUTPUT_FILE_TYPE = "shp"
#OUTPUT_FILE_TYPE = "gpkg"
