#!/bin/bash

# file : processCMakeStrings.sh
# author : SignCodingDwarf
# version : 1.0
# date : 11 October 2016
# Handle functions used to process strings dedicated to the CMake module generation

### Functions
##!
# @brief Convert the library name to the CMake module name
# @param 1 : Library name as a string
#
# Convert the library name to the CMake module name structured as Find<library>.cmake  
# <library> only contains characters [a-z] [A-Z] [0-9] and first character is a upper character 
# Return the module name on standard output
#
##
libraryToModule() {
	local lib 
	local name
	lib="Find"
	name=$(echo $1 | tr -cd "[:alnum:]") # Removes all characters except [a-z] [A-Z] [0-9] 
	name=$(tr '[:lower:]' '[:upper:]' <<< ${name:0:1})${name:1} # First character from lower to upper
	lib+=$name
	lib+=".cmake"
	echo $lib
}

##!
# @brief Convert the library name to the library-related part of variable names
# @param 1 : Library name as a string
#
# Convert the library name to the CMake library-related part of variable names  
# The part can only contain characters : [A-Z] [0-9]. Lower caracters are set to upper
# Return this name on standard output
#
##
libraryToVariableCore() {
	local name
	name=$(echo $1 | tr -cd "[:alnum:]") # Removes all characters except [a-z] [A-Z] [0-9] 
	name=$(echo $name | tr "[:lower:]" "[:upper:]")

	echo $name
}
