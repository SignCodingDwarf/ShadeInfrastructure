#!/usr/bin/env python
""" Module unleasher
A Module in charge of unleashing the ShadeInfrastructure to the battlefield.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

Simple usage example:

	from unleasher import Unleasher

	shu = Unleasher(usegui = False, project_name = "Dummy", description = "A Dummy Project", directory="/home/Moria", dependencies="", ressourcesPath="/usr/local/share/")
	code = shu.process()
"""

__version__ = "0.6.0"

__all__ = ["Unleasher"]

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
import re
import os
import errno
import distutils.dir_util
import shutil
import imp

try:
	import wxpython
	guiAvailable = True
except ImportError:
	guiAvailable = False
	print "GUI module wxpython unavailable. Disabling GUI use"

## Local import
resourcesPath = os.environ['SHADE_LOCATION']
imp.load_source("abstracttool", "".join([resourcesPath,"PythonModules/","abstracttool.py"]))
from abstracttool import AbstractTool

class Unleasher(AbstractTool):
    def __init__(self, usegui, project_name, description, directory, dependencies, verbose, resourcesPath, errorFormat="\033[1;31m", warningFormat="\033[1;33m", statusFormat="\033[1;32m"):
        ## Inherited constructors
        AbstractTool.__init__(self, verbose, errorFormat, warningFormat, statusFormat)
        ## Project Definition
        self._project_name = project_name
        self._description = description
        if not directory is None :
            self._directory = os.path.abspath(directory)
        else :
            self._directory = None
        self._dependencies = dependencies
        ## Installation Parameters
        self._resourcesPath = resourcesPath
        ## Check Errors
        self._parametersValid = self._checkParameters()		
        ## Execution assembled variables
        self._usegui = guiAvailable and (usegui or not self._parametersValid)
        self._installDirectory="%s/%s/" % (self._directory,self._project_name)

    def process(self):
        if self._usegui:
            return self._rungui()
        elif not self._parametersValid:
            return 1
        else:	
            if not self._createDestinationFolder():
                # No clean up here because we don't know why it exists and don't want to suppress previous code or projects
                return 2 # Exiting on error

            if not self._copyToDestination():
                self._removeDestinationFolder() # Clean up because installation failed
                return 3 # Exiting on error

            if not self._writeProjectConfig():
                self._removeDestinationFolder() # Clean up because installation failed
                return 4 # Exiting on error	

        self._displayStatus("\nDone")			
        return 0

    def print_status(self):
        print "********** Unleasher **********"
        print "usegui :",self._usegui
        print "validity :",self._parametersValid
        print "name :",self._project_name
        print "description :",self._description
        print "directory :",self._directory
        print "dependencies :",self._dependencies
        print "verbose :",self._verbose
        print "resourcesPath :", self._resourcesPath
        print "installDirectory :", self._installDirectory
        print "*******************************"

    def _checkParameters(self):
	    return self._checkName() and self._checkDirectory()

    def _checkName(self):
        pattern = re.compile("^[A-Za-z][A-Z0-9a-z_.+-]*$") # At least one character which is a letter and then as many letters, numbers, _, ., + or - as you want (^ is for anchor at start and $ for anchor at end ensuring whole string must match pattern)
        nameValid = not self._project_name is None and not pattern.match(self._project_name) is None
        if not nameValid:
            self._displayError("\nThe project name %s is invalid, YOU MORON.\nYou must use a name starting with a letter and containing letters, numbers, or special characters _ . + - only.\n" % self._project_name) 
        return nameValid

    def _checkDirectory(self):
        directoryExists = not self._directory is None and os.path.isdir(self._directory)
        if not directoryExists:
            self._displayError("\nBLITHERING IDIOT, the directory %s doesn't even exist.\nHOW HARD CAN IT BE TO INSTALL TO AN EXISTING FOLDER ?\n" % self._directory)
        return directoryExists  

    def _rungui(self):
        print "USE GUI"
        return 0

    def _createDestinationFolder(self):
        self._displayStatus("Creating Destination Folder")
        try:
            os.makedirs(self._installDirectory)
        except OSError as e:
            self._displayError("STUPID IDIOT, cannot create %s directory.\nCreation failed with error\n%s" % (self._installDirectory, e))
            return False
        return True

    def _removeDestinationFolder(self):
		self._displayStatus("Clean up")
		try:
			shutil.rmtree(self._installDirectory)
		except:
			pass		

    def _copyToDestination(self):
		self._displayStatus("Copying infrastructure to destination")
		src = "%s%s" % (self._resourcesPath, "Infrastructure/")
		try:
			distutils.dir_util.copy_tree(src, self._installDirectory)
		except distutils.dir_util.DistutilsFileError as e: 
			self._displayError("Cannot copy files to %s directory, YOU MORON.\nCopy failed with error\n%s" % (self._installDirectory, e))
			return False	
		return True

    def _writeProjectConfig(self):
        self._displayStatus("Creating project.dconf file")
        fields = {"name":self._project_name, "description":self._description, "logo":''}
        try:
            destination=open("%s%s" % (self._installDirectory,"config/project.dconf"), "w")
        except IOError as e:		
            self._displayError("Cannot open file %s%s, YOU BLITHERING IDIOT.\nOpening failed with error\n%s" % (self._installDirectory,"config/project.dconf", e))
            return False
        for field,value in fields.iteritems():
            destination.write("%s=%s\n" % (field,value))
        destination.close()
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
