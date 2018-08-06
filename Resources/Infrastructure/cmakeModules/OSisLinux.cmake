# Description :
# Checks if the OS is linux

#https://cmake.org/cmake/help/v2.8.11/cmake.html#section_VariablesThatDescribetheSystem

# Input Variables :
# 

# Once done this will define :
# 

include(MessageDisplay REQUIRED)

displayMessage(STATUS "Checking Operating System")

if(NOT CMAKE_HOST_UNIX)

	displayMessage(STATUS "Windows User Detected")
	displayMessage(FATAL_ERROR "Hey Windows User, this project currently only supports Linux-based Operating Systems !!!")

else()
	if(CMAKE_HOST_APPLE)
		displayMessage(STATUS "Mac OSX User Detected")
		displayMessage(FATAL_ERROR "Hey Apple User, this project currently only supports Linux-based Operating Systems !!!")
	elseif(CMAKE_HOST_CYGWIN)
		displayMessage(STATUS "Cygwin User Detected")
		displayMessage(FATAL_ERROR "Hey Windows Cygwin User, this project currently only supports Linux-based Operating Systems !!!")
	else()
		displayMessage(STATUS "Linux User Detected, installation proceeding")
	endif()
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
