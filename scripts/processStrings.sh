#!/bin/bash

# file : processStrings.sh
# author : SignCodingDwarf
# version : 1.0
# date : 11 October 2016
# Handle functions used to process strings

### Functions
##!
# @brief Convert a given string to an alpha numeric string
# @param 1 : String to convert
#
# Convert a given string to an alpha numeric string with characters : [a-z] [A-Z] [0-9] - _ 
# Resulting string is displayed on standard output.
#
##
toAlphaNumName() {
	echo $(echo $1 | tr -cd "[:alnum:]-_") # Removes all characters except [a-z] [A-Z] [0-9] - _
}
