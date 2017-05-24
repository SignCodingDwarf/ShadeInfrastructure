cmake_minimum_required(VERSION 2.6)

### CMAKE Configuration ###
# ADD modules
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/modules")

# CHECK that Operating System is Linux (to change/remove to allow compilation on other OS)
include(OSisLinux REQUIRED)

#############################################################################

### Project Definition ###
set(PROJECT_NAME "@NAME@")
set(PROJECT_DESCRIPTION "@DESCRIPTION@")
set(PROJECT_LOGO "@LOGO@")

### Project Version ###
set(VERSION_MAJOR 20)
set(VERSION_MINOR 10)
set(VERSION_REVISION 4)

set(PROJECT_VERSION ${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_REVISION})

#############################################################################

