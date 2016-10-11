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

# Library content
library_name=""
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

### Post-process data
updateZenityProgressBar 5 "Parsing user input" 
library_name=$user_input # To update with parsing

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
