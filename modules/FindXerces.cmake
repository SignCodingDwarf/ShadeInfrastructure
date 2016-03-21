# Taken from
# https://code.google.com/p/libcitygml/source/browse/trunk/CMakeModules/FindXerces.cmake?r=95

# - Try to find Xerces-C
# Once done this will define
#
# XERCESC_FOUND - system has Xerces-C
# XERCESC_INCLUDE - the Xerces-C include directory
# XERCESC_LIBRARY - Link these to use Xerces-C
# XERCESC_VERSION - Xerces-C found version

IF (XERCESC_INCLUDE AND XERCESC_LIBRARY)
# in cache already
SET(XERCESC_FIND_QUIETLY TRUE)
ENDIF (XERCESC_INCLUDE AND XERCESC_LIBRARY)

OPTION(XERCESC_STATIC "Set to ON to link your project with static library (instead of DLL)." ON)

IF (NOT ${XERCESC_WAS_STATIC} STREQUAL ${XERCESC_STATIC})
UNSET(XERCESC_LIBRARY CACHE)
UNSET(XERCESC_LIBRARY_DEBUG CACHE)
ENDIF (NOT ${XERCESC_WAS_STATIC} STREQUAL ${XERCESC_STATIC})

SET(XERCESC_WAS_STATIC ${XERCESC_STATIC} CACHE INTERNAL "" )

FIND_PATH(XERCESC_INCLUDE NAMES xercesc/util/XercesVersion.hpp
PATHS
$ENV{XERCESC_INCLUDE_DIR}
${XERCESC_INCLUDE_DIR}
/usr/local/include
/usr/include
)

IF (XERCESC_STATIC)
FIND_LIBRARY(XERCESC_LIBRARY NAMES xerces-c_static_3 xerces-c-3.1 xerces-c
PATHS
$ENV{XERCESC_LIBRARY_DIR}
${XERCESC_LIBRARY_DIR}
/usr/lib
/usr/local/lib
)
FIND_LIBRARY(XERCESC_LIBRARY_DEBUG NAMES xerces-c_static_3D xerces-c-3.1D
PATHS
$ENV{XERCESC_LIBRARY_DIR}
${XERCESC_LIBRARY_DIR}
/usr/lib
/usr/local/lib
)
ADD_DEFINITIONS( -DXERCES_STATIC_LIBRARY )
ELSE (XERCESC_STATIC)
FIND_LIBRARY(XERCESC_LIBRARY NAMES xerces-c_3
PATHS
$ENV{XERCESC_LIBRARY_DIR}
${XERCESC_LIBRARY_DIR}
)
FIND_LIBRARY(XERCESC_LIBRARY_DEBUG NAMES xerces-c_3D
PATHS
$ENV{XERCESC_LIBRARY_DIR}
${XERCESC_LIBRARY_DIR}
)
ENDIF (XERCESC_STATIC)

IF (XERCESC_INCLUDE AND XERCESC_LIBRARY)
SET(XERCESC_FOUND TRUE)
ELSE (XERCESC_INCLUDE AND XERCESC_LIBRARY)
SET(XERCESC_FOUND FALSE)
ENDIF (XERCESC_INCLUDE AND XERCESC_LIBRARY)

IF(XERCESC_FOUND)

FIND_PATH(XERCESC_XVERHPPPATH NAMES XercesVersion.hpp PATHS
${XERCESC_INCLUDE}
PATH_SUFFIXES xercesc/util)

IF ( ${XERCESC_XVERHPPPATH} STREQUAL XERCESC_XVERHPPPATH-NOTFOUND )
SET(XERCES_VERSION "0")
ELSE( ${XERCESC_XVERHPPPATH} STREQUAL XERCESC_XVERHPPPATH-NOTFOUND )
FILE(READ ${XERCESC_XVERHPPPATH}/XercesVersion.hpp XVERHPP)

STRING(REGEX MATCHALL "\n *#define XERCES_VERSION_MAJOR +[0-9]+" XVERMAJ
${XVERHPP})
STRING(REGEX MATCH "\n *#define XERCES_VERSION_MINOR +[0-9]+" XVERMIN
${XVERHPP})
STRING(REGEX MATCH "\n *#define XERCES_VERSION_REVISION +[0-9]+" XVERREV
${XVERHPP})

STRING(REGEX REPLACE "\n *#define XERCES_VERSION_MAJOR +" ""
XVERMAJ ${XVERMAJ})
STRING(REGEX REPLACE "\n *#define XERCES_VERSION_MINOR +" ""
XVERMIN ${XVERMIN})
STRING(REGEX REPLACE "\n *#define XERCES_VERSION_REVISION +" ""
XVERREV ${XVERREV})

SET(XERCESC_VERSION ${XVERMAJ}.${XVERMIN}.${XVERREV})

ENDIF ( ${XERCESC_XVERHPPPATH} STREQUAL XERCESC_XVERHPPPATH-NOTFOUND )

IF(NOT XERCESC_FIND_QUIETLY)
MESSAGE(STATUS "Found Xerces-C: ${XERCESC_LIBRARY}")
MESSAGE(STATUS " : ${XERCESC_INCLUDE}")
MESSAGE(STATUS " Version: ${XERCESC_VERSION}")
ENDIF(NOT XERCESC_FIND_QUIETLY)
ELSE(XERCESC_FOUND)
MESSAGE(FATAL_ERROR "Could not find Xerces-C !")
ENDIF(XERCESC_FOUND)

MARK_AS_ADVANCED(XERCESC_INCLUDE XERCESC_LIBRARY)
