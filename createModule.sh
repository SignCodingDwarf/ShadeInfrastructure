#!/bin/bash

# file : createModule.sh
# author : SignCodingDwarf
# version : 1.0
# date : 2016
# Script allowing to generate a cmake find module for a library from a simple graphical interface

##### Declarations #####
### Global variables
# Colors
statusColor='\033[1;32m' #Status messages are printed in light green
warningColor='\033[1;33m' #Warning messages are printed in yellow
errorColor='\033[1;31m' #Error messages are printed in red
NC='\033[0m' # No Color

# Behavior variables
separator=";" # Separator between output variables of the interface

# Library definition variables
library_name="" # Name of the library 
include_base_file="" # Name and subdirectory of the include file used to locate the include directory of the library
include_suffix="" # Suffixes added to the base search paths for the include main directory
version_file="" # Name of the include file containing library version
version_suffix="" # Subdirectory of the include file containing library version
static_libraries="" # Possible names for the static library
dynamic_libraries="" # Possible names for the dynamic libraries
libraries_suffix="" # Suffixes added to the base search paths for the libraries location
reference_address="" # HTTP address where information on the library can be found
components_file="" # Name of the components definition and dependencies file

# File generation variables
file_name="" # Name of the file to create
upper_name="" # Library name as upper characters used for creating module related variable names
components_list="" # List of component (empty if no components)

### Include functions
# Interface management
. "scripts/zenityInterface.sh"

# Data post-processing
. "scripts/processStrings.sh"
. "scripts/processCMakeStrings.sh"

# File generation
. "scripts/generateCMakeFile.sh"

# File signature
#. "scripts/dwfSign.sh"

##### Script core #####
### Interface
createZenityInterface ${separator}
zenityInterfaceStatus $interface_status ${statusColor} ${errorColor}

### Start progress bar
createZenityProgressBar
sleep 0.5

### Parse User input
updateZenityProgressBar 0 "Parsing user input" 

library_name=$(toAlphaNumName "${user_input[0]}") # Convert to valid library name
include_base_file=${user_input[1]}
include_suffix=${user_input[2]}
version_file=${user_input[3]}
version_suffix=${user_input[4]}
static_libraries=${user_input[5]}
dynamic_libraries=${user_input[6]}
libraries_suffix=${user_input[7]}
reference_address=${user_input[8]}
components_file=${user_input[9]}

# Report
echo -e "${statusColor}Parsed Library Name : ${NC}$library_name"

updateZenityProgressBar 5

### Post-process data
updateZenityProgressBar 5 "Computing File Name"
file_name="./installModules/" # Location path
file_name+=$(libraryToModule $library_name) # File name

updateZenityProgressBar 10

updateZenityProgressBar 10 "Computing Variable names"
upper_name=$(libraryToVariableCore $library_name)

echo $file_name
echo $upper_name

sleep 0.1

### Generate file
updateZenityProgressBar 20 "Creating CMake file"
createCMakeFile $file_name

sleep 0.1

updateZenityProgressBar 30 "Writing module description"
writeDescription $file_name $library_name $upper_name true $components_list

updateZenityProgressBar 40 "Writing Start message"
writeStartMessage $file_name $library_name
#
#
#
#
#
#

updateZenityProgressBar 99 "Signing File"
#DwfSign1_0 $file_name

sleep 0.1

### CleanUp
cleanupZenityProgressBar

### Exit program
exit 0
