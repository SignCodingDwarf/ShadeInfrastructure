cmake_minimum_required(VERSION 3.0)

### CMAKE Configuration ###
# Verbosity
option(VERBOSE "Set to ON to display detailled execution information" OFF)

# ADD modules
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmakeModules")

# Include Application message management module
include(MessageDisplay REQUIRED)

# CHECK that Operating System is Linux (to change/remove to allow compilation on other OS)
include(OSisLinux REQUIRED)

#############################################################################

### General Variables Initialization ###
# Path to configuration files
get_filename_component(CONFIG_PATH "config" REALPATH BASE_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
displayMessage(STATUS "Configuration folder path : ${CONFIG_PATH}")

# Path to infrastructure modules
get_filename_component(INFRA_MOD_PATH "infrastructureModules" REALPATH BASE_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
displayMessage(STATUS "Infrastructure Modules path : ${INFRA_MOD_PATH}")

#############################################################################

### Utility module inclusion ###
# Configuration file management
include(ConfigHandling REQUIRED)

#############################################################################

### Project Configuration ###
# Project Name
readConfField("${CONFIG_PATH}/project.dconf" "name" PROJECT_NAME)
displayMessage(STATUS "Project Name : ${PROJECT_NAME}")

# Project Description
readConfField("${CONFIG_PATH}/project.dconf" "description" PROJECT_DESCRIPTION)
displayMessage(STATUS "Project Description : ${PROJECT_DESCRIPTION}")

# Project Logo
readConfField("${CONFIG_PATH}/project.dconf" "logo" PROJECT_LOGO)
displayMessage(STATUS "Project Logo : ${PROJECT_LOGO}")

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
