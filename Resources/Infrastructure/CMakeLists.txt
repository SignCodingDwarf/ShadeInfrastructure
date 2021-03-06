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

### Path Variables Initialization ###
# Path to configuration files
get_filename_component(CONFIG_PATH "config" REALPATH BASE_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
displayMessage(STATUS "Configuration folder path : ${CONFIG_PATH}")

# Path to infrastructure modules
get_filename_component(INFRA_MOD_PATH "infrastructureModules" REALPATH BASE_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
displayMessage(STATUS "Infrastructure Modules path : ${INFRA_MOD_PATH}")

# Path to template files
get_filename_component(TEMPLATE_PATH "template" REALPATH BASE_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
displayMessage(STATUS "Template Modules path : ${TEMPLATE_PATH}")

# Path to doc folder
get_filename_component(DOC_PATH "doc" REALPATH BASE_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
displayMessage(STATUS "Documentation Location : ${DOC_PATH}")

#############################################################################

### Configuration Loading ###
# Project Description
include(LoadProjectConfig REQUIRED)

# Project Version 
include(LoadProjectVersion REQUIRED)

# Install Folders
include(LoadInstallFolders REQUIRED)

#############################################################################

### Project Definition ###
project(${PROJECT_NAME})

#############################################################################

### Generate template files ###
# Documentation
include(CreateDocFile REQUIRED)

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
