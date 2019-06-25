'''
SCRIPT NAME: ONS Hexmap Automation Tool - INPUT GEOGRAPHIES
SCRIPT DESCRIPTION: A sample of tested OVERSEAS geographies for generation 
                    of hex-based Equal Area Cartograms
                    Users may replace these with their own.
                    GEOGRAPHY_NAME, HEXSIZE, HEXORIENTATION and COMPRESSION_FACTOR
PROJECT CONCEPTION: Bruce Mitchell, January 2017
METHODOLOGY: Bruce Mitchell, George Tzelepis
SCRIPT AUTHORS: Code core written by George Tzelepis (Γιωργος Τζελέπης).
                Restructuring, additional code and annotations by Bruce Mitchell.

ONS Geography Branch, June 2019

'''

'''
*** FLEXIBLE PARAMETER SET-UP ***

GEOGRAPHY_NAME      ## Filename of the geography for which hexmap is to be generated   
                    ## Note: has to be present in 'INPUT_POLYGON_PATH' folder.
HEXSIZE 		    ##  Controls the size of the hexes
                    ## expressed in units of the geograhical reference system or projection
                   	## e.g microns, meters, miles or decimal degrees
HEXORIENTATION 		##  Controls the orientation of the hexes
                    ##  vertical 'pointy-uppy' (1) - better for geographies with EAST-WEST extent
                    ## or horizontal 'flatty-uppy'(2) - better for geographies with NORTH-SOUTH extent
COMPRESSION_FACTOR 	##  Controls the shift of the input geography centroids towards the Centroid of Centroids (CxC)  ...
	                ##  values range from 1 (max) to 7 (min)
        	        ## COMPRESSION_FACTOR(or) VALUE OF 0 PRODUCES 'MAXIMUM ALLOWED SIZE EXCEEDED' ERROR.

*** SOURCE GEOGRAPHY FILES ***
'''
#

# ===============================================================
#
'  N O N - U N I T E D  K I N G D O M '
#  Projection - Various (individually specified)
#
# ===============================================================                 

'''
=========================================
TEST GEOGRAPHIES
Projection = EPSG:4326 - WGS 84
=========================================
'''

' star locations ' 

GEOGRAPHY_NAME = 'hyg_star_locations_within_10_buffered'   
HEXSIZE =  0.25
HEXORIENTATION = 1
COMPRESSION_FACTOR = 2


' Fly Brain '
#GEOGRAPHY_NAME = 'FlyBrainSliceData_USER_10000_simplified'   
#HEXSIZE =  1
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 2



'''
=========================================
EXTRACTS FROM  N A T U R A L  E A R T H  '
=========================================
'''

#WORLD
#GEOGRAPHY_NAME = 'ne_10m_admin_0_countries_lakes__EPSG_4326_WGS84'   
#HEXSIZE =  2
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3

#GEOGRAPHY_NAME = 'ne_10m_admin_0_countries_lakes__Robinson_sphere'
#HEXSIZE = 2
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3


#CONTINENTS
#GEOGRAPHY_NAME = 'ne_50m_admin_0_countries_WCE_Europe_ETRS_1989_LAEA'
#HEXSIZE = 140000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3

#GEOGRAPHY_NAME = 'ne_50m_admin_0_countries_North_America_Equidistant_Conic'
#HEXSIZE = 250000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 2

#GEOGRAPHY_NAME = 'ne_50m_admin_0_countries_Central_America_Equidistant_Conic'
#HEXSIZE = 150000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 2.5


#GEOGRAPHY_NAME = 'ne_50m_admin_0_countries_South_America_Equidistant_Conic'
#HEXSIZE = 250000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 1

#
#GEOGRAPHY_NAME = 'ne_50m_admin_0_countries_Africa_Lambert_Conformal_Conic'
#HEXSIZE = 200000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3


#GEOGRAPHY_NAME = 'ne_50m_admin_0_countries_Asia_Lambert_Conformal_Conic'
#HEXSIZE = 200000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 1.4


#GEOGRAPHY_NAME = 'ne_50m_admin_0_countries_Oceania_Bab_South_Palau_Azimuthal_Equidistant'
#HEXSIZE = 250000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 1.2


'''
=========================================
 I N D I V I D U A L   C O U N T R I E S 
=========================================
'''                            

'''
.................
CHILE (CL)
Projection = SIRGAS-Chile / UTM zone 18S, EPSG: 5362
.................
'''

#GEOGRAPHY_NAME = 'CL_ne_10m_admin_1__EPSG_5362'            
#HEXSIZE = 250000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3


'''
.................
EU_EFTA
Projection = EPSG 3035 ETRS89 / LAEA Europe
.................
'''

#GEOGRAPHY_NAME = 'EU_EFTA_NUTS3__ESPG_3035_ETRS_1989_LAEA'       
#HEXSIZE = 35000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3 


#GEOGRAPHY_NAME = 'ne_50m_admin_0_countries_WCE_Europe_ETRS_1989_LAEA' 
#HEXSIZE = 100000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 2


'''
.................
FRANCE (FR)
Projection = EPSG_27584_NTF_FRANCE_IV
.................
'''
#
#GEOGRAPHY_NAME = 'FR_Canton__EPSG_27584_NTF_FRANCE_IV'         
#HEXSIZE = 14000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 4


#GEOGRAPHY_NAME = 'FR_Arrondissement__EPSG_27584_NTF_FRANCE_IV' 
#HEXSIZE = 28000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3


#GEOGRAPHY_NAME = 'FR_Department__EPSG_27584_NTF_FRANCE_IV'     
#HEXSIZE = 57500
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 4

                         
'''
.................
CROATIA (HR)
Projection = EPSG:102013 - Europe Albers Equal Area Conic
.................
'''

#GEOGRAPHY_NAME = 'HR_ne_10m_admin_1____EPSG_102013'          
#HEXSIZE = 55000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 4

                            
'''
.................
INDONESIA (ID) '
Projection = EPSG:4326 - WGS 84
.................
'''

#GEOGRAPHY_NAME = 'ID_KABUPATEN__EPSG_4326_WGS84'                
#HEXSIZE = 0.6
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3

#
#GEOGRAPHY_NAME = 'ID_PROPINSI__EPSG_4326_WGS84'                 
#HEXSIZE = 2.4
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3


'''
.................
ITALY (IT)
Projection = EPSG 3857 WGS84 / Pseudo-Mercator
.................
'''

#GEOGRAPHY_NAME = 'IT_Provinci__EPSG_3857_WGS84'         
#HEXSIZE =  55000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3


#GEOGRAPHY_NAME = 'IT_NUTS2__EPSG_3857_WGS84'                   
#HEXSIZE = 120000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3


'''
.................
NORWAY (NO)
Projection = EPSG 102013 Europe Albers Equal Area Conic
.................
'''

#GEOGRAPHY_NAME = 'NO_ne_10m_admin_1__EPSG_102013_Europe_AEAC'    
#HEXSIZE = 115000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 7


'''
.................
RUSSIA (RU)
Projection = EPSG 102027 Asia North Lambert Conformal Conic
.................
'''

#GEOGRAPHY_NAME = 'RU_ne_10m_admin_1__EPSG_102027_Asia_North_LCC'  
#HEXSIZE = 190000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 2.5


'''
.................
TURKEY (TK)
Projection = Turkey_country_with_Lambert_Conic_Conformal_Europe_1950_datum
.................
'''

#GEOGRAPHY_NAME = 'TK_ne_10m_admin_1__custom_LCC_GCS_ERP50_IQ'    
#HEXSIZE = 80000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 4

'''
.................
' USA (contiguous) '
#Projection = EPSG 5070 - NAD83 / Conus Albers
.................
'''

#GEOGRAPHY_NAME = 'US48_ne_10m_admin_1__EPSG_102039_USA_Contig_AEAC'    
#HEXSIZE = 225000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3

