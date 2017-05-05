#!/bin/bash

# file :  install.sh
# author : SignC0dingDw@rf
# version : 1.0
# date : 05 May 2017
# ShadeInfrastructure installer

### command line arguments
#
# $1 : Install location of ShadeUnleasher (default is /usr/local/bin).
# $2 : Install location of Resources (default is /usr/local/share).
#
### Exit Code
#
# 0 : Execution succeeded
# 1 : Invalid ShadeUnleash installation folder
# 2 : Invalid Resources installation folder
# 3 : Error on copying ShadeUnleash
# 4 : Error on copying Resources
#

### Init
NC='\033[0m' # No Color
statusColor='\033[1;34m' # Status messages in light blue
installColor='\033[1;32m' # Installation complete in light green
errorColor='\033[1;31m' # Error messages in red

if [ "$0" = "$BASH_SOURCE" ]; then
	isSourced=false

else
	isSourced=true

fi

### ShadeUnleash install folder setup
echo -e "${statusColor}Initializing ShadeUnleash install location${NC}"
if [ ! -z "$1" ]; then
	if [ ! -e "$1" ]; then
		echo -e "${errorColor}Error : ShadeUnleash installation folder $1 does not exist${NC}"
		echo -e "${errorColor}Aborting${NC}"
		if $isSourced; then
			return 1
		else
			exit 1
		fi	
	else
		install_folder=$(readlink -f $1) # Relaive path to global path
	fi
else
	install_folder="/usr/local/bin"
fi

### Resources install folder setup
echo -e "${statusColor}Initializing Resources install location${NC}"
if [ ! -z "$2" ]; then
	if [ ! -e "$2" ]; then
		echo -e "${errorColor}Error : Resources installation folder $2 does not exist${NC}"
		echo -e "${errorColor}Aborting${NC}"
		if $isSourced; then
			return 2
		else
			exit 2
		fi	
	else
		resources_folder=$(readlink -f $2) # Relaive path to global path
	fi
else
	resources_folder="/usr/local/share"
fi

### Copying ShadeUnleash executable
echo -e "${statusColor}Copying ShadeUnleash executable to ${install_folder}${NC}"
sudo cp Exe/ShadeUnleash $install_folder
if (( $? > 0 )); then
	echo -e "${errorColor}Error : Impossible to copy ShadeUnleash file${NC}"
	echo -e "${errorColor}Try running sudo ./install.sh${NC}"
	echo -e "${errorColor}Aborting${NC}"
	if $isSourced; then
		return 3
	else
		exit 3
	fi	
fi

### Adding ShadeUnleash path to PATH
if [[ ":$PATH:" != *":$install_folder:"* ]]; then
	inPath=false
	echo -e "${statusColor}Adding ${install_folder} to PATH${NC}"
	echo -e "\n## Export ShadeUnleash folder" >> ~/.bashrc
	echo "export PATH=\"$install_folder:\${PATH}\"" >> ~/.bashrc # Write to profile so that its done every time a console is opened
	if $isSourced; then
		export PATH="$install_folder:${PATH}" # Do export so that ShadeUnleash can be used straightaway !! Works only if script is sourced
	fi
else
	inPath=true
fi

### Updating Resources location in ShadeUnleash
echo -e "${statusColor}Configuring ShadeUnleash file${NC}"
sudo sed -i "s|@RESOURCES@|${resources_folder}/ShadeInfrastructure/|g" ${install_folder}/ShadeUnleash # Here we can add the / after ${resources_folder} cause readlink always remove the trailing / in folder name

### Copying resources folder
echo -e "${statusColor}Copying Resources to ${resources_folder}${NC}"
if [ -d "${resources_folder}/ShadeInfrastructure/" ]; then
	sudo rm -r ${resources_folder}/ShadeInfrastructure/
fi
sudo mkdir ${resources_folder}/ShadeInfrastructure
sudo cp -a Resources/. ${resources_folder}/ShadeInfrastructure/
if (( $? > 0 )); then
	echo -e "${errorColor}Error : Impossible to copy Resources files${NC}"
	echo -e "${errorColor}Try running sudo ./install.sh${NC}"
	echo -e "${errorColor}Aborting${NC}"
	if $isSourced; then
		return 4
	else
		exit 4
	fi	
fi

echo -e "${installColor}Installation complete${NC}"
if $isSourced || $inPath; then
	echo -e "${installColor}You may now deploy ShadeInfrastructure running${NC}"
	echo -e "${installColor}ShadeUnleash${NC}"
	echo -e "${installColor}To see more details on how to use ShadeUnleash, run ${NC}"
	echo -e "${installColor}ShadeUnleash -h${NC}"
else
	echo -e "${installColor}To start using ShadeInfrastructure, please open a new terminal and run${NC}"
	echo -e "${installColor}ShadeUnleash${NC}"
	echo -e "${installColor}To see more details on how to use ShadeUnleash, run ${NC}"
	echo -e "${installColor}ShadeUnleash -h${NC}"
fi	

if $isSourced; then
	return 0
else
	exit 0
fi

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
