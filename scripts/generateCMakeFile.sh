#!/bin/bash

# file : generateCMakeFile.sh
# author : SignCodingDwarf
# version : 1.0
# date : 24 October 2016
# Functions used to manage the creation of the CMake file

### Functions
##!
# @brief Creates the file if it does not exist or empties it otherwise
# @param 1 : File name as a string
#
# Checks if CMake file exists. If it does not, create it otherwise empties it.  
#
##
createCMakeFile() {
# Check if files exits
	if [ ! -f $1 ]; then 
# If no, create file
		touch $1
	else
# If yes, empty file
		: > $1
	fi
}

##!
# @brief Write separator
# @param 1 : File name as a string
#
# Write a series of # used as separators between the main sections of the module 
#
##
separator() {
	echo '' >> $1
	echo "#############################################################################" >> $1 
	echo '' >> $1
}

##!
# @brief Section title
# @param 1 : File name as a string
# @param 2 : Section title as a string
#
# Write a section (major divisions between actions in modules) as ### <Section Title> ###
#
##
sectionTitle() {
	echo "### ${2} ###" >> $1 
}

##!
# @brief Generates general module description
# @param 1 : File name as a string
# @param 2 : Library name as a string
#
# Generates the general description of a CMake module.
#
##
moduleDescription() {
	echo "# Description :" >> $1
	echo "# Find ${2} library content" >> $1 
	echo '' >> $1 # Line separator	
}

##!
# @brief Generates module inputs description
# @param 1 : File name as a string
# @param 2 : Library name as a string
# @param 3 : Variable base name as a string
# @param 4 : Availability of both types of libraries as a boolean
#
# Lists all module input variables names. Currently :
# - <VariableBase>_INCLUDE_DIR : additional include directory search locations
# - <VariableBase>_LIBRARY_DIR : additional library search locations
# - <VariableBase>_USE_STATIC : indicates if use of static library is preferred (only if both dynamic and static libraries are available)
#
##
moduleInputs() {
	echo "# Input Variables :" >> $1
	echo "# ${3}_INCLUDE_DIR : set the path to ${2} include directory if it is not standard" >> $1 
	echo "# ${3}_LIBRARY_DIR : set the path to ${2} library if it is not standard" >> $1 
	if $4; then
		echo "# ${3}_USE_STATIC : set to true to favor use of static library and false to use dynamic library" >> $1 
	fi
	echo '' >> $1 # Line separator		
}

libraryComponents() {
	: >> $1
}

##!
# @brief Generates module outputs description
# @param 1 : File name as a string
# @param 2 : Library name as a string
# @param 3 : Variable base name as a string
#
# Lists all module output variables names. Currently :
# - <VariableBase>_FOUND : indicating if library was found
# - <VariableBase>_INCLUDE : path to include directory
# - <VariableBase>_LIBRARY : path to library
# - <VariableBase>_VERSION : version number
# - <VariableBase>_STATIC : type of library used
#
##
moduleOutputs() {
	echo "# This module will define :" >> $1
	echo "# ${3}_FOUND : set to true if ${2} was found" >> $1 
	echo "# ${3}_INCLUDE : set the path to the ${2} include directory" >> $1 
	echo "# ${3}_LIBRARY : set the path to the ${2} library" >> $1 
	echo "# ${3}_VERSION : set the ${2} version number" >> $1 
	echo "# ${3}_STATIC : set to true if static library is used and to false if dynamic library is used" >> $1 
	echo '' >> $1 # Line separator		
}

##!
# @brief Generates the description of the module with list of inputs, outputs and required components 
# @param 1 : File name as a string
# @param 2 : Library name as a string
# @param 3 : Variable base name as a string
# @param 4 : Availability of both types of libraries as a boolean
# @param 5 : List of module components as an array of strings
# @return 0 if writing went fine, 1 if file did not exist, 2 if file is not empty
#
# Generates the description of the module with list of inputs, outputs and required components according to following structure :
# - General description
# - List of input variables (script variables that may be created elsewhere and that are used by the module)
# - List of components and their dependencies
# - List of outputs (variables created by the module and that can be used elsewhere)  
#
##
writeDescription() {
# Check if file exits
	if [ -f $1 ]; then 
# If yes, file must be empty
		if [ ! -s $1 ]; then
# Start by displaying the description
			moduleDescription $1 $2
			moduleInputs $1 $2 $3 $4
			libraryComponents $1 $2 $5
			moduleOutputs $1 $2 $3						

			return 0
		else
			return 2 # File is not empty
		fi
	else
		return 1 # File not created
	fi
}

##!
# @brief Generates module start message
# @param 1 : File name as a string
# @param 2 : Library name as a string
#
# Generates module start message indicating that module is run.
#
##
writeStartMessage() {
	sectionTitle $1 "Start Message"
	echo "message(STATUS \"Locating ${2} library\")" >> $1
	separator $1 
}

##!
# @brief Generates instructions to determine if library is found quietly
# @param 1 : File name as a string
# @param 2 : Variable base name as a string
#
# Generates instructions to determine if the library location is already stored in cache and thus no longer requires search.
#
##
writeFindQuiet() {
	sectionTitle $1 "Check if data is already stored in cache"
	echo "if(DEFINED ${2}_INCLUDE AND DEFINED ${2}_LIBRARY)" >> $1
	echo -e "\tset(${2}_FIND_QUIETLY true)" >> $1
	echo "else()" >> $1
	echo -e "\tset(${2}_FIND_QUIETLY false)" >> $1
	echo "endif()" >> $1

	separator $1 
}
