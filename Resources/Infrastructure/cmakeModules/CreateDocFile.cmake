# Description :
# Creates Documentation file from template

# Input Variables :
# VERBOSE : Indicates if STATUS messages should be displayed
# CONFIG_PATH : Path to the folder containing configuration files
# TEMPLATE_PATH : Path to the folder containing template files
# DOC_PATH : Location of the documentation folder (created in necessary)

# Once done this will define :
# CREATE_DOC_LOADED : flag indicating that the documentation file creation module has already been loaded

if(NOT DEFINED CREATE_DOC_LOADED)

    include("${CMAKE_CURRENT_LIST_DIR}/MessageDisplay.cmake" REQUIRED)
    include("${CMAKE_CURRENT_LIST_DIR}/LoadProjectConfig.cmake" REQUIRED)
    include("${CMAKE_CURRENT_LIST_DIR}/LoadProjectVersion.cmake" REQUIRED)

    displayMessage(STATUS "Creating Documentation file")

    configure_file(${TEMPLATE_PATH}/.DoxyDoc ${DOC_PATH}/.DoxyDoc @ONLY)

    set(CREATE_DOC_LOADED TRUE)

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
