#!/usr/bin/env python

""" Module versionsetter
A module allowing to set project version.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

Simple usage example:
	from versionsetter import VersionSetter

	vst = VersionSetter(verbose = True, version = [1, 2, 3])
	code = vst.process()
"""

__version__ = "1.2.0"

__all__ = ["VersionSetter"]

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

## Local import
resourcesPath = os.environ['SHADE_LOCATION']
imp.load_source("abstracttool", "".join([resourcesPath,"Infrastructure/pythonModules/tools/","abstracttool.py"]))
imp.load_source("configparser", "".join([resourcesPath,"Infrastructure/pythonModules/configParsing/","configparser.py"]))
imp.load_source("parsingerror", "".join([resourcesPath,"Infrastructure/pythonModules/configParsing/","parsingerror.py"]))
from abstracttool import AbstractTool
from configparser import ConfigParser
import parsingerror

class VersionSetter(AbstractTool):
    def __init__(self, verbose, version, errorFormat="\033[1;31m", warningFormat="\033[1;33m", statusFormat="\033[1;32m"):
        ## Inherited constructors
        AbstractTool.__init__(self, verbose, errorFormat, warningFormat, statusFormat)
        ## Version details
        if len(version) != 3:
            self._versionValid = False
            self._displayError("Invalid number of arguments expected %s, received %s\n" % (3, len(version)))
        else:
            try: # We check the arguments are valid
                self._major = int(version[0])
                self._minor = int(version[1])
                self._revision = int(version[2])
                self._versionValid = True
            except ValueError:
                self._versionValid = False
                self._displayError("Error in converting %s, %s and %s arguments to integer" % (version[0], version[1], version[2]))
        ### Current Version
        self._currentMajor = 0
        self._currentMinor = 0
        self._currentRevision = 0
        ### Working Directory
        self._cwd = os.getcwd()

    def print_status(self):
        print "********** Version Setter **********"
        print "verbose  :",self._verbose
        print "valid    :",self._versionValid
        if self._versionValid:
            print "major    :", self._major
            print "minor    :", self._minor
            print "revision :", self._revision
        print "************************************"

    def process(self):
        if not self._versionValid:
            return 1
        if not self._configFolderExists():
            return 2
        if self._versionFileExists():
            self._parseCurrentVersion() ## Otherwise all set to 0 by init
        if not self._isVersionNumberSuperior():
            return 3
        if not self._updateVersion():        
            return 4
        return 0

    def _configFolderExists(self):
        configFolder = "/".join([self._cwd, "config"])
        self._displayStatus("Checking Existence of config Folder : %s" % configFolder)
        if os.path.isdir(configFolder):
            self._displayStatus("The config folder %s exists." % configFolder)
            return True
        else:
            self._displayError("The config folder %s does not exist." % configFolder)
            return False

    def _versionFileExists(self):
        versionFile = "/".join([self._cwd, "config", "version.dconf"])
        self._displayStatus("Checking if version file %s exist" % versionFile)
        if os.path.isfile(versionFile):
            self._displayStatus("The version file %s exists." % versionFile)
            return True
        else:
            self._displayStatus("The version file has not yet been created.")
            return False

    def _parseCurrentVersion(self):
        parser = ConfigParser("/".join([self._cwd, "config", "version.dconf"]))
        try:
            versionDict = parser.extractFields(["major","minor","revision"])
        except parsingerror.ParsingError as e:
            self._displayWarning(e) 
        else:
            if not versionDict["major"] is None:
                try:
                    self._currentMajor=int(versionDict["major"][0])
                except ValueError:
                    pass # We do nothing if conversion fails and version stays to 0   
            if not versionDict["minor"] is None:
                try:
                    self._currentMinor=int(versionDict["minor"][0])
                except ValueError:
                    pass # We do nothing if conversion fails and version stays to 0   
            if not versionDict["revision"] is None:
                try:
                    self._currentRevision=int(versionDict["revision"][0])
                except ValueError:
                    pass # We do nothing if conversion fails and version stays to 0   
        self._displayStatus("Current Project Version is : %s.%s.%s" % (self._currentMajor, self._currentMinor, self._currentRevision))

    def _isVersionNumberSuperior(self):
        if self._major > self._currentMajor or (self._major == self._currentMajor and self._minor > self._currentMinor) or (self._major == self._currentMajor and self._minor == self._currentMinor and self._revision > self._currentRevision):
            self._displayStatus("Upgrading project version from %s.%s.%s" % (self._currentMajor, self._currentMinor, self._currentRevision))
            self._displayStatus("to %s.%s.%s" % (self._major, self._minor, self._revision))
            return True
        elif self._major == self._currentMajor and self._minor == self._currentMinor and self._revision == self._currentRevision:
            self._displayWarning("Requested version %s.%s.%s is identical to current version.\nUpdating nonetheless" % (self._major, self._minor, self._revision))
            return True
        else:
            self._displayError("Requested version %s.%s.%s" % (self._major, self._minor, self._revision))     
            self._displayError("is inferior to current version %s.%s.%s" % (self._currentMajor, self._currentMinor, self._currentRevision))
            self._displayError("Update Rejected")           
            return False

    def _updateVersion(self):
        try:
            destination=open("/".join([self._cwd, "config", "version.dconf"]), "w")
        except IOError as e:		
            self._displayError("Cannot open file %s.\nOpening failed with error\n%s" % ("/".join([self._cwd, "config", "version.dconf"]), e))
            return False
        destination.write("major=%s\n" % self._major)
        destination.write("minor=%s\n" % self._minor)
        destination.write("revision=%s\n" % self._revision)
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
