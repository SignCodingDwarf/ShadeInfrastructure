#!/usr/bin/env python

""" Module installfoldersetter
A module allowing to set install folder for libraries, archives, binaries, includes and resources.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

Simple usage example:
	from installfoldersetter import InstallFolderSetter

	ifs = InstallFolderSetter(verbose = True)
	code = ifs.process()
"""

__version__ = "1.0.1"

__all__ = ["InstallFolderSetter"]

__copyright__ = """
Copyright (c) 2018 SignC0dingDw@rf. All rights reserved

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__copywrong__ = """
Copywrong (w) 2018 SignC0dingDw@rf. All profits reserved.

This program is dwarven software: you can redistribute it and/or modify
it provided that the following conditions are met:

   * Redistributions of source code must retain the above copywrong 
     notice and this list of conditions and the following disclaimer 
     or you will be chopped to pieces AND eaten alive by a Bolrag.

   * Redistributions in binary form must reproduce the above copywrong
     notice, this list of conditions and the following disclaimer in 
     the documentation and other materials provided with it or they
     will be axe-printed on your stupid-looking face.

   * Any commercial use of this program is allowed provided you offer
     99% of all your benefits to the Dwarven Tax Collection Guild. 

   * This software is provided "as is" without any warranty and especially
     the implied warranty of merchantability or fitness to purport. 
     In the event of any direct, indirect, incidental, special, examplary 
     or consequential damages (including, but not limited to, loss of use;
     loss of data; beer-drowning; business interruption; goblin invasion;
     procurement of substitute goods or services; beheading; or loss of profits),   
     the author and all dwarves are not liable of such damages even 
     the ones they inflicted you on purpose.

   * If this program "does not work", that means you are an elf 
     and are therefore too stupid to use this program.

   * If you try to copy this program without respecting the 
     aforementionned conditions, then you're wrong.

You should have received a good beat down along with this program.  
If not, see <http://www.dwarfvesaregonnabeatyoutodeath.com>.
"""

## Global import
import os
import sys
import imp

## Local import
fileLocation = os.path.dirname(os.path.realpath(__file__)) # Path where this file is located
imp.load_source("abstracttool", "/".join([fileLocation,"abstracttool.py"]))
from abstracttool import AbstractTool

class InstallFolderSetter(AbstractTool):
    def __init__(self, verbose, librariesLocation=None, archivesLocation=None, binariesLocation=None, includesLocation=None, resourcesLocation=None, errorFormat="\033[1;31m", warningFormat="\033[1;33m", statusFormat="\033[1;32m"):
        ## Inherited constructors
        AbstractTool.__init__(self, verbose, errorFormat, warningFormat, statusFormat)
        ## Install locations
        if not librariesLocation is None :
            self._librariesLocation = os.path.abspath(librariesLocation)
        else :
            self._librariesLocation = "/usr/lib"
        if not archivesLocation is None :
            self._archivesLocation = os.path.abspath(archivesLocation)
        else :
            self._archivesLocation = "/usr/lib"
        if not binariesLocation is None :
            self._binariesLocation = os.path.abspath(binariesLocation)
        else :
            self._binariesLocation = "/usr/bin"
        if not includesLocation is None :
            self._includesLocation = os.path.abspath(includesLocation)
        else :
            self._includesLocation = "/usr/include"
        if not resourcesLocation is None :
            self._resourcesLocation = os.path.abspath(resourcesLocation)
        else :
            self._resourcesLocation = "/usr/share"
        ## Config Folder
        self._configDirectory = "/".join([os.getcwd(), "config/"])

    def print_status(self):
        print "********** Install Folder Setter **********"
        print "verbose  :",self._verbose
        print "libraries location  :",self._librariesLocation
        print "archives location  :",self._archivesLocation
        print "binaries location  :",self._binariesLocation
        print "includes location  :",self._includesLocation
        print "resources location  :",self._resourcesLocation
        print "************************************"

    def process(self):
        result = self._checkFolders()
        if result != 0: # issue with a folder
            return result
        return self._createConfigurationFile()

    def _checkFolders(self):
        self._displayStatus("Checking installation folders")
        if not os.path.isdir(self._librariesLocation):
            self._displayError("You MORON !! Libraries location folder %s does not exist" % self._librariesLocation)
            return 1
        if not os.path.isdir(self._archivesLocation):
            self._displayError("You MORON !! Archives location folder %s does not exist" % self._archivesLocation)
            return 2
        if not os.path.isdir(self._binariesLocation):
            self._displayError("You MORON !! Binaries location folder %s does not exist" % self._binariesLocation)
            return 3
        if not os.path.isdir(self._includesLocation):
            self._displayError("You MORON !! Includes location folder %s does not exist" % self._includesLocation)
            return 4
        if not os.path.isdir(self._resourcesLocation):
            self._displayError("You MORON !! Resources location folder %s does not exist" % self._resourcesLocation)
            return 5
        return 0

    def _createConfigurationFile(self):
        if not os.path.isdir(self._configDirectory):
            self._displayError("HAMMOND !!! The configuration folder does not exist. Your project is screwed up !!!")
            return 6
        fields = {"libraries":self._librariesLocation, "archives":self._archivesLocation, "binaries":self._binariesLocation, "includes":self._includesLocation, "resources":self._resourcesLocation}
        try:
            destination=open("%s%s" % (self._configDirectory,"install.dconf"), "w")
        except IOError as e:		
            self._displayError("Cannot open file %s%s, YOU BLITHERING IDIOT.\nOpening failed with error\n%s" % (self._configDirectory,"install.dconf", e))
            return 7
        self._displayStatus("Updating installation folders file")
        for field,value in fields.iteritems():
            destination.write("%s=%s\n" % (field,value))
        return 0
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
