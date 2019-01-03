#!/usr/bin/env python

""" Module cleaner
A module allowing to clean project folder from temporary elements.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

Simple usage example:
	from cleaner import Cleaner

	cln = Cleaner()
	code = cln.process()
"""

__version__ = "0.1.0"

__all__ = ["Cleaner"]

__copyright__ = """
Copyright (c) 2019 SignC0dingDw@rf. All rights reserved

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
Copywrong (w) 2019 SignC0dingDw@rf. All profits reserved.

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
import shutil

## Local import
fileLocation = os.path.dirname(os.path.realpath(__file__)) # Path where this file is located
imp.load_source("abstracttool", "/".join([fileLocation,"abstracttool.py"]))
from abstracttool import AbstractTool

class Cleaner(AbstractTool):
    def __init__(self, verbose, errorFormat="\033[1;31m", warningFormat="\033[1;33m", statusFormat="\033[1;32m"):
        ## Inherited constructors
        AbstractTool.__init__(self, verbose, errorFormat, warningFormat, statusFormat)
        ## Working Directory
        self._workingDirectory = os.getcwd()
        ## Temporary folders
        temporaryFolders=["buildDir", "doc"]
        self._temporaryFolderPaths=["/".join([self._workingDirectory, folder]) for folder in temporaryFolders]

    def print_status(self):
        print "********** Cleaner **********"
        print "verbose  :",self._verbose
        print "working directory :",self._workingDirectory
        print "temporary folders :",self._temporaryFolderPaths
        print "*****************************"

    def process(self):
        for folder in self._temporaryFolderPaths:
            try:
                self._removeFolder(folder)
            except OSError:
                return 1
        return 0

    def _removeFolder(self, folder):
        self._displayStatus("Checking folder %s" % folder)
        if not os.path.isdir(folder):
            self._displayStatus("Folder %s absent. Nothing to be done" % folder)
        else:
            self._displayStatus("Removing folder %s" % folder)
            try:
                shutil.rmtree(folder)
            except OSError as e:
                self._displayError("%s" % e)
                raise # Rethrow exception

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
