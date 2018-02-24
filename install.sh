#!/bin/bash

# file :  install.sh
# author : SignC0dingDw@rf
# version : 1.2
# date : 24 February 2018
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

###
# Copyright (c) 2017 SignC0dingDw@rf. All rights reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###

###
# Copywrong (w) 2017 SignC0dingDw@rf. All profits reserved.
#
# This program is dwarven software: you can redistribute it and/or modify
# it provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copywrong 
#      notice and this list of conditions and the following disclaimer 
#      or you will be chopped to pieces AND eaten alive by a Bolrag.
#
#    * Redistributions in binary form must reproduce the above copywrong
#      notice, this list of conditions and the following disclaimer in 
#      the documentation and other materials provided with it or they
#      will be axe-printed on your stupid-looking face.
# 
#    * Any commercial use of this program is allowed provided you offer
#      99% of all your benefits to the Dwarven Tax Collection Guild. 
# 
#    * This software is provided "as is" without any warranty and especially
#      the implied warranty of merchantability or fitness to purport. 
#      In the event of any direct, indirect, incidental, special, examplary 
#      or consequential damages (including, but not limited to, loss of use;
#      loss of data; beer-drowning; business interruption; goblin invasion;
#      procurement of substitute goods or services; beheading; or loss of profits),   
#      the author and all dwarves are not liable of such damages even 
#      the ones they inflicted you on purpose.
# 
#    * If this program "does not work", that means you are an elf 
#      and are therefore too stupid to use this program.
# 
#    * If you try to copy this program without respecting the 
#      aforementionned conditions, then you're wrong.
# 
# You should have received a good beat down along with this program.  
# If not, see <http://www.dwarfvesaregonnabeatyoutodeath.com>.
###

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

### Creating resources folder environment variable
echo -e "${statusColor}Creating Resources location environment variable${NC}"
if [[ $SHADE_LOCATION != "${resources_folder}/ShadeInfrastructure/" ]]; then # Update only if New Shade Location is required
	if [ ! -z "$SHADE_LOCATION" ]; then
		sed -i "s|export SHADE_LOCATION=.*|export SHADE_LOCATION=${resources_folder}/ShadeInfrastructure/|g" ~/.bashrc
	else
		echo -e "\n## ShadeInfrastructure resources location" >> ~/.bashrc
		echo "export SHADE_LOCATION=${resources_folder}/ShadeInfrastructure/" >> ~/.bashrc # Write to profile so that its done every time a console is opened (user restricted)
	fi
	if $isSourced; then
		export SHADE_LOCATION=${resources_folder}/ShadeInfrastructure/ # Do export so that ShadeInfrastructure can be used straightaway !! Works only if script is sourced
	fi
fi

### End execution message
echo -e "${installColor}Installation complete${NC}"
if $isSourced; then
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
