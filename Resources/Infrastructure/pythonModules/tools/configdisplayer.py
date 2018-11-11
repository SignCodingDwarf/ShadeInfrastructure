#!/usr/bin/env python

""" Module configdisplayer
A module allowing to display project configuration.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

Simple usage example:
	from configdisplayer import ConfigDisplayer

	cfgd = ConfigDisplayer()
	code = cfgd.process()
"""

__version__ = "0.0.1"

__all__ = ["ConfigDisplayer"]

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
import imp
from subprocess import check_output

## Local import
fileLocation = os.path.dirname(os.path.realpath(__file__)) # Path where this file is located
imp.load_source("abstracttool", "/".join([fileLocation,"abstracttool.py"]))
imp.load_source("configparser", "/".join([fileLocation, "../configParsing", "configparser.py"]))
imp.load_source("parsingerror", "/".join([fileLocation, "../configParsing", "parsingerror.py"]))
from abstracttool import AbstractTool
from configparser import ConfigParser
import parsingerror

class ConfigDisplayer(AbstractTool):
    def __init__(self, sectionFormat="\033[1;32m", keyFormat="\033[1;33m", errorFormat="\033[1;31m", warningFormat="\033[1;33m", statusFormat="\033[1;32m"):
        ## Inherited constructors
        AbstractTool.__init__(self, True, errorFormat, warningFormat, statusFormat)
        ## Formatting
        self._sectionFormat = sectionFormat
        self._keyFormat = keyFormat
        ## Configuration directory
        self._configDirectory = "/".join([os.getcwd(), "config/"])

    def print_status(self):
        print "********** Config Displayer **********"
        print self._sectionFormat,"Section Display Color",self._noFormat
        print "Config Directory    :",self._configDirectory

    def process(self):
        if not os.path.isdir(self._configDirectory):
            self._displayError("BLITHERING IDIOT!! The configuration directory %s does not even exist. You project is screwed up!" % self._configDirectory)
            return 1
        if not self._displayProject():
            return 2
        self._displayVersion()
        return 0

    def _displayProject(self):
        projectFile = "".join([self._configDirectory, "project.dconf"])
        parser = ConfigParser(projectFile, False)
        try:
            fieldDict = parser.extractFields(["name", "logo", "description"])
        except parsingerror.ParsingError as e:
            self._displayError(e)
            return False
        else: 
            self._printSection("Project")
            if fieldDict["name"] is None:
                self._displayError("YOU MORON, your project has no name. You are DOOOOOOMED !!!!")
                return False
            else:
                self._printField("name", fieldDict["name"][0])
            if not fieldDict["description"] is None:
                self._printField("description", fieldDict["description"][0])
            if not fieldDict["logo"] is None:
                self._printField("logo", fieldDict["logo"][0])
            return True

    def _displayVersion(self):
        versionFile = "".join([self._configDirectory, "version.dconf"])
        parser = ConfigParser(versionFile, False)
        try:
            fieldDict = parser.extractFields(["major", "minor", "revision"])
        except parsingerror.ParsingError as e:
            pass # We ignore errors on version file
        else: 
            self._printSection("Version")
            if not fieldDict["major"] is None:
                self._printField("major", fieldDict["major"][0])
            if not fieldDict["minor"] is None:
                self._printField("minor", fieldDict["minor"][0])
            if not fieldDict["revision"] is None:
                self._printField("revision", fieldDict["revision"][0])
            return True


    def _printSection(self, section):
        print self._sectionFormat, "********** ", section, " **********", self._noFormat

    def _printField(self, key, value):
        print self._keyFormat, "", key, ":\t", self._noFormat, value

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
