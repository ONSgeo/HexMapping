'''
SCRIPT NAME: ONS Hexmap Automation Tool - INPUT GEOGRAPHIES
SCRIPT DESCRIPTION: A sample of tested DOMESTIC UK geographies for generation
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
# ===============================================================
#
' U N I T E D   K I N G D O M '
# Projection - EPSG:27700 - OSGB 1936 / British National Grid
#
# ===============================================================

'''
UK LOCAL AUTHORITIES, APRIL 2019 '
'''

'''
=========================================
For UNITED KINGDOM mapping
=========================================
'''

'''
### --------------------------------------------------------------------
# FIRST COMPRESSION - separately create E(s), E(n)+W, S & NI, then merge 
### --------------------------------------------------------------------
'''

''' ENGLAND AND WALES'''
#GEOGRAPHY_NAME = 'E_SOUTH_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'E_NORTH_W_LAD_Apr_2019_BFC'              
#
#HEXSIZE = 11000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 4    

''' SCOTLAND '''

#GEOGRAPHY_NAME = 'S_LAD_Apr_2019_BFC'              
#HEXSIZE = 11000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 1.8

''' NORTHERN IRELAND '''

#GEOGRAPHY_NAME = 'NI_LAD_Apr_2019_BFC'              
#HEXSIZE = 11000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 1.8                                 


'''
### ----------------
# SECOND COMPRESSION
### ----------------
'''

#GEOGRAPHY_NAME = 'UK_LAD_Apr_2019_BFC_11000_2_EWCF4_SNI_CF1pt8_FC0pt1'
#HEXSIZE = 11000
#HEXORIENTATION = 2 
#COMPRESSION_FACTOR = 4


'''
### ----------------
# THIRD COMPRESSION
### ----------------
'''

#GEOGRAPHY_NAME = 'UK_LAD_Apr_2019_BFC_11000_2_EWCF4_SNI_CF1pt8_FC0pt1_11000_2_CF4__FC_0'
#HEXSIZE = 11000
#HEXORIENTATION = 2 
#COMPRESSION_FACTOR = 4


'''
=========================================
For GREAT BRITAIN mapping
=========================================
'''

'''
### ----------------
# FIRST COMPRESSION
### ----------------
'''

''' ENGLAND AND WALES'''
#GEOGRAPHY_NAME = 'E_SOUTH_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'E_NORTH_W_LAD_Apr_2019_BFC'              
#
#HEXSIZE = 11000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 4    


''' SCOTLAND '''

#GEOGRAPHY_NAME = 'S_LAD_Apr_2019_BFC'              
#HEXSIZE = 11000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 1.8


                   
'''
### ----------------
# SECOND COMPRESSION
### ----------------
'''

#GEOGRAPHY_NAME = 'GB_LAD_Apr_2019_BFC_11000_2_EWCF4_S_CF1pt8_FC0pt1'
#HEXSIZE = 11000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 4 


'''
### ----------------
# THIRD COMPRESSION
### ----------------
'''

#GEOGRAPHY_NAME = 'GB_LAD_Apr_2019_BFC_11000_2_EWCF4_S_CF1pt8_FC0pt1_11000_2_CF4__FC_0'
#HEXSIZE = 11000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 4 



''' 
=========================================
# For ENGLAND and WALES
=========================================
'''

#GEOGRAPHY_NAME = 'E_SOUTH_LAD_Apr_2019_BFC'              
GEOGRAPHY_NAME = 'E_NORTH_W_LAD_Apr_2019_BFC'              

HEXSIZE = 11000
HEXORIENTATION = 2
COMPRESSION_FACTOR = 1.2    


'''
### ----------------
# SECOND COMPRESSION
### ----------------
'''

#GEOGRAPHY_NAME = 'EW_LAD_Apr_2019_BFC__11000_2__CF1.2___C_HXMP'              
#HEXSIZE = 11000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 2.5    


''' 
=========================================
# For JUST ENGLAND 
=========================================
'''

#GEOGRAPHY_NAME = 'E_SOUTH_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'E_NORTH_LAD_Apr_2019_BFC'   
           
#
#HEXSIZE = 11000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 4    

#GEOGRAPHY_NAME = 'E_NORTH_LAD_Apr_2019_BFC___9000_2__CF3___C_HXMP'


'''
### ----------------
# SECOND COMPRESSION
### ----------------
'''

#GEOGRAPHY_NAME = 'E_NS_LAD_Apr_2019_BFC_11000_2_CF4__FC_0pt1'              
#HEXSIZE = 11000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 6    


'''
=========================================
For UK mapping from REGIONS OF ENGLAND 
=========================================
'''

#HEXSIZE = 9000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 3


#GEOGRAPHY_NAME = 'E_NE_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'E_NW_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'E_YatH_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'E_EM_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'E_WM_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'E_EE_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'E_LN_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'E_SE_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'E_SW_LAD_Apr_2019_BFC'              

#GEOGRAPHY_NAME = 'W_LAD_Apr_2019_BFC'  
#GEOGRAPHY_NAME = 'S_LAD_Apr_2019_BFC'              
#GEOGRAPHY_NAME = 'NI_LAD_Apr_2019_BFC'              


'''
### ----------------
# SECOND COMPRESSION
### ----------------
'''

#GEOGRAPHY_NAME = 'E_NORTH_W_LAD_Apr_2019_BFC___9000_2__CF3___C_HXMP'
#GEOGRAPHY_NAME = 'E_SOUTH_LAD_Apr_2019_BFC___9000_2__CF3___C_HXMP'
#HEXSIZE = 9000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 4


'''
### ----------------
# THIRD COMPRESSION
### ----------------
'''

#GEOGRAPHY_NAME = 'EW_LAD_Apr_2019_BFC___9000_2__CF3___C_HXMP__9000_2__CF4___C_HXMP'
#HEXSIZE = 9000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 0.1
'''
### ----------------
# FOURTH COMPRESSION - STARTS TO GO WRONG HERE
### ----------------
'''
#GEOGRAPHY_NAME = 'UK_LAD_Apr_2019_BFC__7000_2__CF3___C_HEXMAP_adj__7000_2__CF3___C_HEXMAP__7000_2__CF3___C_HEXMAP'


'''
### ----------------
# FIFTH COMPRESSION
### ----------------
'''
#GEOGRAPHY_NAME = 'UK_LAD_Apr_2019_BFC__7000_2__CF3___C_HEXMAP_adj__7000_2__CF3___C_HEXMAP__7000_2__CF3___C_HEXMAP__7000_2__CF3___C_HEXMAP
#HEXSIZE = 7000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 3


'''
=========================================
WALES
=========================================
'''

# For Wales only map

#GEOGRAPHY_NAME = 'W_LAD_Apr_2019_BFC'              
#HEXSIZE = 15000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 1.3


'''
=========================================
# SCOTLAND
=========================================
'''

# For Scotland only map
#
#GEOGRAPHY_NAME = 'S_LAD_Apr_2019_BFC'              
#HEXSIZE = 25000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 1.2

'''
=========================================
NORTHERN IRELAND
=========================================                   
'''

# For Northern Ireland only map

#GEOGRAPHY_NAME = 'NI_LAD_Apr_2019_BFC'              
#HEXSIZE = 25000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 2.3


'''
=========================================                   
CENSUS GEOGRAPHIES
=========================================                   
'''

#GEOGRAPHY_NAME = 'EW_MSOA_Dec_2011_BGC'            
#HEXSIZE = 2500
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 2.5


#GEOGRAPHY_NAME = 'West_Midlands_MSOA_Dec_2011_BGC'
#HEXSIZE = 2000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 0.1
#COMPRESSION_FACTOR = 2.5

#GEOGRAPHY_NAME = 'City_of_London__OAs_BFC_Dec_2015'      
#HEXSIZE = 100
#HEXORIENTATION = 1 
#COMPRESSION_FACTOR = 2.5


'''
=========================================                   
HEALTH GEOGRAPHIES
=========================================                   
'''

#GEOGRAPHY_NAME = 'E_CCGs_Apr_2018_BGC'              
#HEXSIZE = 11000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3


'''
=========================================                   
EUROSTAT GEOGRAPHIES
=========================================                   
'''

#GEOGRAPHY_NAME = 'UK_NUTS2_Jan_2018_BGC'            
#HEXSIZE = 50000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3


#GEOGRAPHY_NAME = 'UK_NUTS3_Jan_2018_BGC'            
#HEXSIZE = 19000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 3


'''
=========================================                   
PARLIAMENTARY GEOGRAPHIES
=========================================                   
'''

#GEOGRAPHY_NAME = 'UK_Westminster_ParliCons_Dec_2017_BGC'
#HEXSIZE = 8000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 2


#GEOGRAPHY_NAME = 'WNA_Constituencies_Dec_2017_BGC'  
#HEXSIZE = 22000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 4


'''
=========================================                   
OTHER UK GEOGRAPHIES
=========================================                   
'''                            

#GEOGRAPHY_NAME = 'EW_Police_Force_Areas_Dec_2017_BGC'  
#HEXSIZE = 30000
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 4


#GEOGRAPHY_NAME = 'Ciotti_PU_MBIO2223_1617SP_GrabData_exposed_1mB'  
#GEOGRAPHY_NAME = 'Ciotti_PU_MBIO2223_1617SP_GrabData_exposed_1mB_sampleSums'
#HEXSIZE = 0.0002
#HEXORIENTATION = 1
#COMPRESSION_FACTOR = 3


#GEOGRAPHY_NAME = 'XYCiotti_BeachData_20110922_BNG'  
#HEXSIZE = 16000
#HEXORIENTATION = 2
#COMPRESSION_FACTOR = 2.5





