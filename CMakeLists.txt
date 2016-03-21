# Description :
# Main CMAKE file of the application

# Input Variables :
# COMPILER_CHANGED : set to true to use a different CXX compiler from the default compiler set to false to use default compiler (Variable used by FindCompilerSelect module)
# COMPILER_FILE : compiler to use instead of default CXX compiler. Used only if COMPILER_CHANGED is set to true (Variable used by CXXCompilerSelect module)
# RELEASE_BUILD : set to true to build application in release mode (Variable used by SetUpConfigurationFlags)
# USER_DEBUG : set to true to enable user debug operations (Variable used by SetUpConfigurationFlags)
# USE_4 : set to true to use directly QT4, set to false to use QT5 (Variable used by FindQtContent module)
# QT5_PATH : set the path to Qt5Config.cmake (Variable used by FindQtContent module)

cmake_minimum_required(VERSION 2.6)

#message(STATUS ${USE_4})
#message(STATUS ${QT5_PATH})

### CMAKE Configuration ###
# ADD modules
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/modules")

# CHECK that Operating System is Linux (to change/remove to allow compilation on other OS)
include(OSisLinux REQUIRED)

#############################################################################

### Project Configuration ###
# Project Name
set(PROJECT_NAME "Test")

# Select generation type : library or executable. Set to true to generate library
set(GENERATE_LIBRARY false) # DO NOT MODIFY !!!!!!!!

# External Library use variables
set(USE_XERCES false CACHE BOOL "Set to true to enable the use of Xerces Library")
set(USE_QT false CACHE BOOL "Set to true to enable the use of Qt Library")
# ... Extend with other libraires
MARK_AS_ADVANCED(GENERATE_LIBRARY USE_XERCES USE_QT) # All use variables are left to advanced users (to extend with other libraries

# Location of generated program or library
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_LIST_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_CURRENT_LIST_DIR})

#############################################################################

### Compiler Configuration ###
include(CXXCompilerSelect REQUIRED)

#############################################################################
#############################################################################

### Project Creation ###
project(${PROJECT_NAME})

#############################################################################

### Compile Flags Set up ###
include(SetUpConfigurationFlags REQUIRED) # Change or extend module 

#############################################################################

### External Libraries Setup ###
# Xerces Setup
if(USE_XERCES)
	find_package(Xerces)
	if(NOT XERCESC_FOUND)
		message(FATAL_ERROR "You must install Xerces") 
	else()
		list(APPEND ALL_LIBRARIES ${XERCESC_LIBRARY}) #If Xercesc is found, append it to library list	
	endif()
endif()

# Qt Setup
if(USE_QT)
	find_package(QtContent)
	include_directories(${QT_INCLUDES})
	add_definitions(${QT_DEFINITIONS})
	list(APPEND ALL_LIBRARIES ${QT_LIBRARY}) #If Qt is found, append it to library list
endif()


### Application specific libraries ###
# Add your other libraries here

#############################################################################

### Application Files Setup ###
# Locate all source files
file(

	GLOB_RECURSE

	source_files

	src/*.cpp

	src/*.c

)

# Add all header files
include_directories(include)

# Locate all header files
file(

	GLOB_RECURSE

	header_files

	include/*.h

	include/*.hpp

)

# List headers to install files
if(GENERATE_LIBRARY)
	set(header_install ${header_files})

	file(

		GLOB_RECURSE

		no_install

		include/common_defines.h

	)

	list(REMOVE_ITEM header_install ${no_install}) # We don't want to install the files that may change from one lib/app to another.
	MESSAGE(STATUS ${header_install})
endif()

#############################################################################

### Application Generation ###

if(GENERATE_LIBRARY)
	# Generate static library
	add_library(

		${PROJECT_NAME}_static

		STATIC

		${source_files}

		${header_files}

	)

	# Generate dynamic library
	add_library(

		${PROJECT_NAME}

		SHARED

		${source_files}

		${header_files}
	)
else()
	# Creating Executable
	add_executable(

		${PROJECT_NAME}

		${source_files}

		${header_files}
	)
endif()

# Adding Libraries to executable
target_link_libraries(

	${PROJECT_NAME}

	${ALL_LIBRARIES}
)

if(GENERATE_LIBRARY)
# Static Library Name change (so that both libraries share the same name)
set_target_properties(${PROJECT_NAME}_static PROPERTIES OUTPUT_NAME ${PROJECT_NAME})

# Specify compilation language
if(NOT source_files) # If no source files found, indicate programming language
set_target_properties(${PROJECT_NAME} PROPERTIES LINKER_LANGUAGE CXX)
set_target_properties(${PROJECT_NAME}_static PROPERTIES LINKER_LANGUAGE CXX)
endif()

# Define install directories
install(TARGETS ${PROJECT_NAME}_static ${PROJECT_NAME} LIBRARY DESTINATION lib/${PROJECT_NAME} ARCHIVE DESTINATION lib/${PROJECT_NAME})
install(FILES ${header_install} DESTINATION include/${PROJECT_NAME})
endif()

#############################################################################

#  ______________________________
# |                              |
# |    ______________________    |       
# |   |                      |   |
# |   |         sign         |   |
# |   |        coding        |   |
# |   |        dw@rf         |   |
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
#               |  |
#               |__|
