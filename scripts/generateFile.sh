#!/bin/bash

# file : createModule.sh
# author : SignCodingDwarf
# version : 1.0
# date : 2016
# Definition of interface management variables and functions

createCMakeFile() {
# Check if files exits
	if [ ! -f $1 ]; then #if file does not exist
# If no, create file
		echo "$2Creating CMake module ${NC}"
		touch $1
		echo tralala >> $1
		echo abcd >> $1
	else
# If yes, empty file
		echo "$2Emptying CMake module content ${NC}"
		: > $1
	fi
}
