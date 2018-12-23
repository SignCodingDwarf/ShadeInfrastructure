# Description :
# Loads project configuration : name, description and logo 

# Input Variables :
# VERBOSE : Indicates if STATUS messages should be displayed
# CONFIG_PATH : Path to the folder containing configuration files

# Once done this will define :
# PROJECT_NAME : project name
# PROJECT_DESCRIPTION : project description
# PROJECT_LOGO : path to project logo image

include("${CMAKE_CURRENT_LIST_DIR}/MessageDisplay.cmake" REQUIRED)
include("${CMAKE_CURRENT_LIST_DIR}/ConfigHandling.cmake" REQUIRED)

displayMessage(STATUS "Loading Project configuration")

# Project Name
readConfField("${CONFIG_PATH}/project.dconf" "name" PROJECT_NAME)
displayMessage(STATUS "Project Name : ${PROJECT_NAME}")

# Project Description
readConfField("${CONFIG_PATH}/project.dconf" "description" PROJECT_DESCRIPTION)
displayMessage(STATUS "Project Description : ${PROJECT_DESCRIPTION}")

# Project Logo
readConfField("${CONFIG_PATH}/project.dconf" "logo" PROJECT_LOGO)
displayMessage(STATUS "Project Logo : ${PROJECT_LOGO}")