#!/usr/bin/env python
""" Module unleasher
A Module in charge of unleashing the ShadeInfrastructure to the battlefield.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

Simple usage example:

	from unleasher import Unleasher

	shu = Unleasher(usegui = False, project_name = "Dummy", description = "A Dummy Project", directory="/home/Moria", dependencies="", ressourcesPath="/usr/local/share/")
	shu.process()
"""

__version__ = "0.1.0"

__all__ = ["Unleasher"]

__copyright__ = """
Copyright (c) 2017 SignC0dingDw@rf. All rights reserved

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
Copywrong (w) 2017 SignC0dingDw@rf. All profits reserved.

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
import re
import os

try:
	import wxpython
	guiAvailable = True
except ImportError:
	guiAvailable = False
	print "GUI module wxpython unavailable. Disabling GUI use"

class Unleasher:
	def __init__(self, usegui, project_name, description, directory, dependencies, resourcesPath):
		self._project_name = project_name
		self._description = description
		if not directory is None :
			self._directory = os.path.abspath(directory)
		else :
			self._directory = None
		self._dependencies = dependencies
		self._pattern = re.compile("^[A-Za-z][A-Z0-9a-z_.+-]*$") # At least one character which is a letter and then as many letters, numbers, _, ., + or - as you want (^ is for anchor at start and $ for anchor at end ensuring whole string must match pattern)
		self._resourcesPath = resourcesPath
		self._errorMsg = ''
		self._checkParameters()

		self._usegui = guiAvailable and (usegui or not self._nameValid or not self._directoryExists)

	def unleash(self):
		if self._usegui:
			self._rungui()
 		elif self._errorMsg:
			self._displayError()
		else:	
			print "Processing"
#			self._createDestinationFolder()
#			self._copyToDestination()
#			self._writeProjectName()
#			self._writeProjectDescription()
#			self._writeRessourcesLocation()
#			self._writeProjectDependencies()

	def _checkParameters(self):
		self._checkName()
		self._checkDirectory()

	def _checkName(self):
		self._nameValid = not self._project_name is None and not self._pattern.match(self._project_name) is None
		if not self._nameValid:
			self._errorMsg = "\nThe project name %s is invalid, YOU MORON.\nYou must use a name starting with a letter and containing letters, numbers, or special characters _ . + - only.\n" % self._project_name 

	def _checkDirectory(self):
		self._directoryExists = not self._directory is None and os.path.isdir(self._directory)
		if not self._directoryExists:
			self._errorMsg = "%s\nBLITHERING IDIOT, the directory %s doesn't even exist.\nHOW HARD CAN IT BE TO INSTALL TO AN EXISTING FOLDER ?\n" % (self._errorMsg, self._directory)  

	def _rungui(self):
		print "USE GUI"

	def _displayError(self):
		print "\033[1;31m%s\033[0m" % self._errorMsg

	def print_status(self):
		print "********** Unleasher **********"
		print "usegui :",self._usegui
		print "name :",self._project_name, "   is valid ? ", self._nameValid
		print "description :",self._description
		print "directory :",self._directory, "   exists ? ", self._directoryExists
		print "dependencies :",self._dependencies
		print "resourcesPath :", self._resourcesPath
		print "*******************************"

	def _createDestinationFolder(self):
		folder = ""
		try:
        		os.makedirs(folder)
    		except OSError as exception:
        		return False
		return True

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
