# Description :
# Loads installation folders

# Input Variables :
# VERBOSE : Indicates if STATUS messages should be displayed
# CONFIG_PATH : Path to the folder containing configuration files

# Once done this will define :
# INSTALL_FOLDER_LIBRARIES : path to libraries installation folder
# INSTALL_FOLDER_ARCHIVES : path to archives installation folder
# INSTALL_FOLDER_BINARIES : path to binaries installation folder
# INSTALL_FOLDER_INCLUDES : path to includes installation folder
# INSTALL_FOLDER_RESOURCES : path to resources installation folder
# INSTALL_FOLDER_LOADED : flag indicating that the project install folders loading module has already been loaded

if(NOT DEFINED INSTALL_FOLDER_LOADED)

    include("${CMAKE_CURRENT_LIST_DIR}/MessageDisplay.cmake" REQUIRED)
    include("${CMAKE_CURRENT_LIST_DIR}/ConfigHandling.cmake" REQUIRED)

    displayMessage(STATUS "Loading Project install folders")

    # Libraries installation folder
    readConfField("${CONFIG_PATH}/install.dconf" "libraries" INSTALL_FOLDER_LIBRARIES)
    displayMessage(STATUS "Libraries installation folder : ${INSTALL_FOLDER_LIBRARIES}")

    # Archives installation folder
    readConfField("${CONFIG_PATH}/install.dconf" "archives" INSTALL_FOLDER_ARCHIVES)
    displayMessage(STATUS "Archives installation folder : ${INSTALL_FOLDER_ARCHIVES}")

    # Binaries installation folder
    readConfField("${CONFIG_PATH}/install.dconf" "binaries" INSTALL_FOLDER_BINARIES)
    displayMessage(STATUS "Binaries installation folder : ${INSTALL_FOLDER_BINARIES}")

    # Includes installation folder
    readConfField("${CONFIG_PATH}/install.dconf" "includes" INSTALL_FOLDER_INCLUDES)
    displayMessage(STATUS "Includes installation folder : ${INSTALL_FOLDER_INCLUDES}")

    # Resources installation folder
    readConfField("${CONFIG_PATH}/install.dconf" "resources" INSTALL_FOLDER_RESOURCES)
    displayMessage(STATUS "Resources installation folder : ${INSTALL_FOLDER_RESOURCES}")

    set(INSTALL_FOLDER_LOADED TRUE)

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
