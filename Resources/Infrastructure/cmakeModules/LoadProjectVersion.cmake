# Description :
# Loads project version information

# Input Variables :
# VERBOSE : Indicates if STATUS messages should be displayed
# CONFIG_PATH : Path to the folder containing configuration files

# Once done this will define :
# VERSION_MAJOR : major version number
# VERSION_MINOR : minor version number
# VERSION_REVISION : revision version number

include("${CMAKE_CURRENT_LIST_DIR}/MessageDisplay.cmake" REQUIRED)
include("${CMAKE_CURRENT_LIST_DIR}/ConfigHandling.cmake" REQUIRED)

displayMessage(STATUS "Loading Project configuration")

# Major
readConfField("${CONFIG_PATH}/version.dconf" "major" VERSION_MAJOR)

# Minor
readConfField("${CONFIG_PATH}/version.dconf" "minor" VERSION_MINOR)

# Revision
readConfField("${CONFIG_PATH}/version.dconf" "revision" VERSION_REVISION)
displayMessage(STATUS "Project Version : ${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_REVISION}")
