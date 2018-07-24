#!/bin/bash

# file : listTools.sh
# author : SignC0dingDw@rf
# version : 0.1
# date : 24 July 2018
# Function to create and manage tools list

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
