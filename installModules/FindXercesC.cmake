# Description :
# Find Xerces-C library content

# Input Variables :
# XERCESC_INCLUDE_DIR : set the path to Xerces-C include directory if it is not standard
# XERCESC_LIBRARY_DIR : set the path to Xerces-C library if it is not standard
# XERCESC_USE_STATIC : set to true to favor use of static library and false to use dynamic library

# This module will define :
# XERCESC_FOUND : set to true if Xerces-C was found
# XERCESC_INCLUDE : set the path to the Xerces-C include directory
# XERCESC_LIBRARY : set the path to the Xerces-C library
# XERCESC_VERSION : set the Xerces-C version number
# XERCESC_STATIC : set to true if static library is used and to false if dynamic library is used

### Start Message ###
message(STATUS "Locating Xerces-C library")

#############################################################################

### Check if data is already stored in cache ###
if(DEFINED XERCESC_INCLUDE AND DEFINED XERCESC_LIBRARY)
	set(XERCESC_FIND_QUIETLY true)
else()
	set(XERCESC_FIND_QUIETLY false)
endif()

#############################################################################

#  ______________________________ 
# |                              |
# |    ______________________    |
# |   |                      |   |
# |   |         Sign         |   |
# |   |        C0ding        |   |
# |   |        Dw@rf         |   |
# |   |         1.0          |   |
# |   |______________________|   |
# |                              |
# |______________________________|
#               |  |
#               |  |
#               |  |
#               |  |
#               |  |
#               |  |
#               |  |
#               |  |
#               |  |
#               |  |
#               |__|
