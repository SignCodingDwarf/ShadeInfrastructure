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
file_name=""
upper_name=""

### Include functions
# Interface management
. "scripts/zenityInterface.sh"

# Data post-processing

# File generation
. "scripts/generateFile.sh"

##### Script core #####
### Interface
createZenityInterface ${separator}
zenityInterfaceStatus $interface_status ${statusColor} ${errorColor}

### Start progress bar
createZenityProgressBar
sleep 0.5

### Parse User input
updateZenityProgressBar 0 "Parsing user input" 

library_name=${user_input[0]}
include_base_file=${user_input[1]}
include_suffix=${user_input[2]}
version_file=${user_input[3]}
version_suffix=${user_input[4]}
static_libraries=${user_input[5]}
dynamic_libraries=${user_input[6]}
libraries_suffix=${user_input[7]}
reference_address=${user_input[8]}
components_file=${user_input[9]}

updateZenityProgressBar 5

### Post-process data


sleep 2

### Generate file
#createCMakeFile $file_name

#updateZenityProgressBar 10 "Coucou" ${warningColor}
#sleep 3
#updateZenityProgressBar 30 "Toto" ${warningColor}
#sleep 3
#updateZenityProgressBar 50
#sleep 1
#updateZenityProgressBar -23 "Aie" ${warningColor}
#sleep 3
#updateZenityProgressBar 99 "CouCoucou"
#sleep 2
#updateZenityProgressBar 153

### CleanUp
cleanupZenityProgressBar

### Exit program
exit 0
