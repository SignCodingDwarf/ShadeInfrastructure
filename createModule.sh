#!/bin/bash

# file : createModule.sh
# author : SignC0dingDw@rf
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
. "scripts/dwfSign.sh"

##### Script core #####
### Interface
createZenityInterface ${separator}
zenityInterfaceStatus $interface_status ${statusColor} ${errorColor}

### Start progress bar
createZenityProgressBar
sleep 0.2

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
components_file=${user_input[9]} # lcd extension : Library Components Definition 

# Report
echo -e "${statusColor}Parsed Library Name : ${NC}$library_name"

### Post-process data
updateZenityProgressBar 5 "Computing file name"
file_name="./installModules/" # Location path
file_name+=$(libraryToModule $library_name) # File name
sleep 0.1

updateZenityProgressBar 9 "Computing variable names"
upper_name=$(libraryToVariableCore $library_name)
sleep 0.1

updateZenityProgressBar 14 "Computing include base file name"
# extension .h ou .hpp
# charactères OK [a-z] [A-Z] [0-9] [_] [-] [. en position 1] hors extension
sleep 0.1

updateZenityProgressBar 18 "Computing include folder location suffix"
sleep 0.1

updateZenityProgressBar 22 "Computing version file name"
sleep 0.1

updateZenityProgressBar 27 "Computing static library name"
sleep 0.1

updateZenityProgressBar 32 "Computing dynamic library name"
sleep 0.1

updateZenityProgressBar 36 "Computing library location suffix"
sleep 0.1

updateZenityProgressBar 41 "Computing library documentation web address"
sleep 0.1

updateZenityProgressBar 45 "Computing list of library components and dependencies"
sleep 0.1

echo $file_name
echo $upper_name
sleep 0.1

### Generate file
updateZenityProgressBar 50 "Creating CMake file"
createCMakeFile $file_name
sleep 0.1

updateZenityProgressBar 54 "Writing module description"
writeDescription $file_name $library_name $upper_name true $components_list
sleep 0.1

updateZenityProgressBar 58 "Writing start message"
writeStartMessage $file_name $library_name
sleep 0.1

updateZenityProgressBar 63 "Writing cache definition checking"
writeFindQuiet $file_name $upper_name
sleep 0.1

updateZenityProgressBar 67 "Writing library compilation type checking"
sleep 0.1

updateZenityProgressBar 72 "Writing include folder localization"
sleep 0.1

updateZenityProgressBar 76 "Writing library file localization"
sleep 0.1

updateZenityProgressBar 81 "Writing find flag setting"
sleep 0.1

updateZenityProgressBar 85 "Writing library version setting"
sleep 0.1

updateZenityProgressBar 90 "Writing library informations and error messages display"
sleep 0.1

updateZenityProgressBar 95 "Signing File"
DwfSign1_0 $file_name

### CleanUp
cleanupZenityProgressBar

### Exit program
exit 0
