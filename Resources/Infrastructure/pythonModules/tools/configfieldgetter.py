#!/usr/bin/env python

""" Module configfieldgetter
A module allowing to print value of a field in a config file.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

Simple usage example:
	from configfieldgetter import ConfFieldGetter

	cfg = ConfFieldGetter(verbose = True, configFile = "confFile.dconf", configField = "field1")
	code = cfg.process()
"""

__version__ = "1.0.0"

__all__ = ["ConfigFieldGetter"]

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
imp.load_source("configparser", "/".join([fileLocation, "../configParsing", "configparser.py"]))
from abstracttool import AbstractTool
from configparser import ConfigParser

class ConfigFieldGetter(AbstractTool):
    def __init__(self, verbose, configFile, configField, separator, errorFormat="\033[1;31m", warningFormat="\033[1;33m", statusFormat="\033[1;32m"):
        ## Inherited constructors
        AbstractTool.__init__(self, verbose, errorFormat, warningFormat, statusFormat)
        ## Config file
        if not configFile is None :
            self._configFile = os.path.abspath(configFile)
        else :
            self._configFile = None
        ## Config field
        self._configField = configField
        ## Separator
        if not separator is None:
            self._separator = separator
        else:
            self._separator = os.environ.get('IFS', ';') # Default IFS is ; because \n may appear in case of multiline value
            if len(self._separator) > 1:
                self._separator=self._separator[0]

    def print_status(self):
        print "********** Version Setter **********"
        print "verbose  :",self._verbose
        print "config file    :",self._configFile
        print "field    :", self._configField
        print "separator    :", self._separator
        print "************************************"

    def process(self):
        if self._configFile == None:
            self._displayError("Configuration file is set to None.")
            return 5
        if self._configField == None:
            self._displayError("Configuration field is set to None.")
            return 6
        self._displayStatus("Parsing file : %s" % self._configFile) 
        parser = ConfigParser(self._configFile, True)
        self._displayStatus("Extracting Field : %s" % self._configField) 
        fieldDict = parser.extractFields([self._configField])
        if fieldDict[self._configField][1] == 1:
            self._displayError("YOU BLITHERING IDIOT !!\nThe file %s does not exist." % self._configFile)   
            return 1
        if fieldDict[self._configField][1] == 2:
            self._displayError("YOU MORON !!\nThe file %s has the wrong extension." % self._configFile)   
            return 2
        if fieldDict[self._configField][1] == 3:
            self._displayError("STUPID IDIOT !!\nThe file %s could not be parsed." % self._configFile)   
            return 3      
        if fieldDict[self._configField][1] == 4:
            self._displayWarning("The field %s does not exist in file %s." % (self._configField, self._configFile)) 
            sys.stdout.write("") # Print an empty string without endline char  
            return 4
        for value in fieldDict[self._configField][0][0:-1]:
            sys.stdout.write("%s%s" % (value, self._separator))
        sys.stdout.write("%s" % (fieldDict[self._configField][0][-1]))
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
