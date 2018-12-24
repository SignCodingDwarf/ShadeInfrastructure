# Description :
# Loads project version information

# Input Variables :
# VERBOSE : Indicates if STATUS messages should be displayed
# CONFIG_PATH : Path to the folder containing configuration files

# Once done this will define :
# VERSION_MAJOR : major version number
# VERSION_MINOR : minor version number
# VERSION_REVISION : revision version number
# PROJECT_VERSION_LOADED : flag indicating that the project version loading module has already been loaded

if(NOT DEFINED PROJECT_VERSION_LOADED)

    include("${CMAKE_CURRENT_LIST_DIR}/MessageDisplay.cmake" REQUIRED)
    include("${CMAKE_CURRENT_LIST_DIR}/ConfigHandling.cmake" REQUIRED)

    displayMessage(STATUS "Loading Project version")

    # Major
    readConfField("${CONFIG_PATH}/version.dconf" "major" VERSION_MAJOR)

    # Minor
    readConfField("${CONFIG_PATH}/version.dconf" "minor" VERSION_MINOR)

    # Revision
    readConfField("${CONFIG_PATH}/version.dconf" "revision" VERSION_REVISION)
    displayMessage(STATUS "Project Version : ${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_REVISION}")

    set(PROJECT_VERSION_LOADED TRUE)

endif()

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
