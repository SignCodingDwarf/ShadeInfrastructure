#!/bin/bash

# file : listTools.sh
# author : SignC0dingDw@rf
# version : 0.1
# date : 24 July 2018
# Functions to create and manage tools list

###
# Copyright (c) 2018 SignC0dingDw@rf. All rights reserved
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
# Copywrong (w) 2018 SignC0dingDw@rf. All profits reserved.
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

##!
# @brief List available development tools to standard output
# @return 0
##
ListDevTools()
{
    local devTools="$(ls ${SHADE_LOCATION}Tools/)"

    echo -e "${devTools}"
    return 0
}

##!
# @brief List available user tools to standard output
# @return 0
##
ListUserTools()
{
    local userTools="$(ls tools/)"

    echo -e "${userTools}"
    return 0
}

##!
# @brief Check if a given command is in tool list
# @param 1 : Tool list
# @param 2 : Command to check
# @return 0 if command is in tool list, 1 otherwise
#
# From https://stackoverflow.com/questions/8063228/how-do-i-check-if-a-variable-exists-in-a-list-in-bash
#
##
IsInToolList()
{
  local list="$1"
  local command="$2"
  if [[ $list =~ (^|[[:space:]])"$command"($|[[:space:]]) ]] ; then
    return 0
  else
    return 1
  fi
}

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
