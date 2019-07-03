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

' random square '

#GEOGRAPHY_NAME = 'oneArm'   
#HEXSIZE =  1
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 1

#GEOGRAPHY_NAME = 'RandomSquarePolygons'   
#HEXSIZE =  250
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 2

' star locations ' 

#GEOGRAPHY_NAME = 'hyg_star_locations_within_10_buffered'   
#HEXSIZE =  0.25
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 2


#' Fly Brain '
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
#COMPRESSION_FACTOR = 1.2


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
BULGARIA (BGR)
Projection = EPSG:7801_BGS2005/CCS2005
.................
'''

GEOGRAPHY_NAME = 'BGR_adm1__EPSG7801_BGS_2005'    
HEXSIZE = 72500
HEXORIENTATION = 1
COMPRESSION_FACTOR = 3
#
#GEOGRAPHY_NAME = 'BGR_adm2__EPSG7801_BGS_2005'    
#HEXSIZE = 17500
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3

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
FINLAND (FIN)
Projection = EPSG:2393 Finland UCS
.................
'''

#GEOGRAPHY_NAME = 'FIN_adm3__EPSG2393_KKJ_FUCS'    
#HEXSIZE = 40000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 4

#GEOGRAPHY_NAME = 'FIN_adm4__EPSG2393_KKJ_FUCS'    
#HEXSIZE = 15000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 3


'''
.................
FRANCE (FR)
Projection = EPSG_27584_NTF_FRANCE_IV
.................
'''

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
GREECE (GRC)
Projection = EPSG:2100 GGR87 Greek Grid
.................
'''
#
#GEOGRAPHY_NAME = 'GRC_adm2__EPSG2100_GGRS87_Greek_Grid'    
#HEXSIZE = 1
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3

#GEOGRAPHY_NAME = 'GRC_adm3__EPSG2100_GGRS87_Greek_Grid'    
#HEXSIZE = 0.175
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 5
#                         
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
HUNGARY (HUN)
Projection = EPSG:23700 - HD72 EOV
.................
'''

#GEOGRAPHY_NAME = 'HUN_adm1__EPSG23700_HD72_EOV'          
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
#HEXSIZE =  57000
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
NORWAY (NO)
Projection = EPSG:4273 - NGO 1948
.................
'''

#GEOGRAPHY_NAME = 'NOR_adm1__EPSG4273_NGO_1948'          
#HEXSIZE = 1
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 4

#GEOGRAPHY_NAME = 'NOR_adm2__EPSG4273_NGO_1948'          
#HEXSIZE = 0.2
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 4

#GEOGRAPHY_NAME = 'NOR_adm3__EPSG4273_NGO_1948'          
#HEXSIZE = 0.01
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 4

                            
'''
.................
POLAND (POL)
Projection = EPSG:2180 ETRS89 Poland CS92
.................
'''

#GEOGRAPHY_NAME = 'POL_adm2__EPSG2180_ETRS89_Poland_CS92'          
#HEXSIZE = 22000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 4


'''
.................
RUSSIA (RU)
Projection = EPSG 102027 Asia North Lambert Conformal Conic
.................
'''

#GEOGRAPHY_NAME = 'RU_ne_10m_admin_1__EPSG_102027_Asia_North_LCC'  
#HEXSIZE = 100
#HEXSIZE = 180000
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


'''
.................
SOUTH AFRICA (ZA)
Projection = EPSG:4222 Cape
.................
'''
#GEOGRAPHY_NAME = 'ZAF_adm2_mainland'    
#HEXSIZE = 0.5
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3
