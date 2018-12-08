#!/usr/bin/env python

""" Module configchecker
A module allowing to check current configuration state and initialize config with default value if not set.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

Simple usage example:
	from configchecker import ConfigChecker

	cfgc = ConfigChecker()
	code = cfgc.process()
"""

__version__ = "0.0.2"

__all__ = ["ConfigChecker"]

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
fileLocation = os.path.dirname(os.path.realpath(__file__)) # Path where this file is located
imp.load_source("abstracttool", "/".join([fileLocation,"abstracttool.py"]))
imp.load_source("configparser", "/".join([fileLocation, "../configParsing", "configparser.py"]))
imp.load_source("parsingerror", "/".join([fileLocation, "../configParsing", "parsingerror.py"]))
from abstracttool import AbstractTool
from configparser import ConfigParser
import parsingerror
try:
    resourcesPath = os.environ['SHADE_LOCATION']
    imp.load_source("versionsetter", "".join([resourcesPath,"PythonModules/tools/","versionsetter.py"]))
    from versionsetter import VersionSetter
    versionsetterAvailable = True
except Exception as e:
    versionsetterAvailable = False
    print "versionsetter Tool unavailable :"
    print e
try:
    imp.load_source("installfoldersetter", "/".join([fileLocation,"installfoldersetter.py"]))
    from installfoldersetter import InstallFolderSetter
    installfoldersetterAvailable = True
except Exception as e:
    installfoldersetterAvailable = False
    print "installfoldersetter Tool unavailable :"
    print e

class ConfigChecker(AbstractTool):
    def __init__(self, verbose, errorFormat="\033[1;31m", warningFormat="\033[1;33m", statusFormat="\033[1;32m"):
        ## Inherited constructors
        AbstractTool.__init__(self, verbose, errorFormat, warningFormat, statusFormat)
        ## Configuration directory
        self._configDirectory = "/".join([os.getcwd(), "config/"])
        ## Local storage for installation folders
        self._folders = {"librariesLocation":None, "archivesLocation":None, "binariesLocation":None, "includesLocation":None, "resourcesLocation":None}

    def print_status(self):
        print "********** Config Checker **********"
        print "Config Directory    :",self._configDirectory

    def process(self):
        if not os.path.isdir(self._configDirectory):
            self._displayError("BLITHERING IDIOT!! The configuration directory %s does not even exist. You project is screwed up!" % self._configDirectory)
            return 1
        if not self._checkProject():
            return 2
        if not self._checkVersion():
            if not self._initializeVersion():
                return 3
        if not self._checkInstallFolders():
            if not self._initializeInstallFolders():
                return 4
        self._displayStatus("Project configuration is valid")
        return 0

    def _checkProject(self):
        projectFile = "".join([self._configDirectory, "project.dconf"])
        parser = ConfigParser(projectFile, False)
        try:
            fieldDict = parser.extractFields(["name", "logo", "description"])
        except parsingerror.ParsingError as e:
            self._displayError(e)
            return False
        else: 
            if fieldDict["name"] is None or not fieldDict["name"][0]:
                self._displayError("YOU MORON, your project has no name. You are DOOOOOOMED !!!!")
                return False
            if fieldDict["description"] is None or not fieldDict["description"][0]:    
                self._displayError("HAMMOND !! Where's the project description ? A project can't have no description !!!!")
                return False
            return True

    def _checkVersion(self):
        versionFile = "".join([self._configDirectory, "version.dconf"])
        parser = ConfigParser(versionFile, False)
        try:
            fieldDict = parser.extractFields(["major", "minor", "revision"])
        except parsingerror.ParsingError as e:
            self._displayError(e)
            return False
        else: 
            if fieldDict["major"] is None:
                self._displayWarning("The project has no major version")
                return False
            else:
                try:
                    currentMajor=int(fieldDict["major"][0])
                except ValueError:
                    self._displayWarning("The major field %s is not an integer" % fieldDict["major"][0]) 
                    return False
            if fieldDict["minor"] is None:
                self._displayWarning("The project has no minor version")
                return False
            else:
                try:
                    currentMinor=int(fieldDict["minor"][0])
                except ValueError:
                    self._displayWarning("The minor field %s is not an integer" % fieldDict["minor"][0]) 
                    return False
            if fieldDict["revision"] is None:
                self._displayWarning("The project has no revision version")
                return False
            else:
                try:
                    currentRevision=int(fieldDict["revision"][0])
                except ValueError:
                    self._displayWarning("The revision field %s is not an integer" % fieldDict["revision"][0]) 
                    return False
            return True

    def _initializeVersion(self):
        if not versionsetterAvailable:
            self._displayError("versionsetter tool unavailable. Cannot correct error on module version")
            return False
        versionFile = "".join([self._configDirectory, "version.dconf"])
        if os.path.isfile(versionFile):
            os.remove(versionFile) # Delete the file so that we get sure version is 0.0.0 otherwise file would not be updated
    	vst = VersionSetter(verbose = self._verbose, version = [0, 0, 1])
    	code = vst.process()
        if code == 0:
            return True
        else:   
            self._displayError("Version setting failed with error : %d" % code)
            return False

    def _checkInstallFolders(self):
        confOk = True
        installFile = "".join([self._configDirectory, "install.dconf"])
        parser = ConfigParser(installFile, False)
        try:
            fieldDict = parser.extractFields(["libraries", "archives", "binaries", "includes", "resources"])
        except parsingerror.ParsingError as e:
            self._displayError(e)
            return False
        else: 
            if fieldDict["libraries"] is None:
                self._displayWarning("The project has no libraries install folder")
                confOk = False
            else:
                if not os.path.isdir(fieldDict["libraries"][0]):
                    self._displayWarning("The libraries install folder %s does not exist." % fieldDict["libraries"][0]) 
                    confOk = False
                else:
                    self._folders["librariesLocation"]=fieldDict["libraries"][0]
            if fieldDict["archives"] is None:
                self._displayWarning("The project has no archives install folder")
                confOk = False
            else:
                if not os.path.isdir(fieldDict["archives"][0]):
                    self._displayWarning("The archives install folder %s does not exist." % fieldDict["archives"][0]) 
                    confOk = False
                else:
                    self._folders["archivesLocation"]=fieldDict["archives"][0]
            if fieldDict["binaries"] is None:
                self._displayWarning("The project has no binaries install folder")
                confOk = False
            else:
                if not os.path.isdir(fieldDict["binaries"][0]):
                    self._displayWarning("The binaries install folder %s does not exist." % fieldDict["binaries"][0]) 
                    confOk = False
                else:
                    self._folders["binariesLocation"]=fieldDict["binaries"][0]
            if fieldDict["includes"] is None:
                self._displayWarning("The project has no includes install folder")
                confOk = False
            else:
                if not os.path.isdir(fieldDict["includes"][0]):
                    self._displayWarning("The includes install folder %s does not exist." % fieldDict["includes"][0]) 
                    confOk = False
                else:
                    self._folders["includesLocation"]=fieldDict["includes"][0]
            if fieldDict["resources"] is None:
                self._displayWarning("The project has no resources install folder")
                confOk = False
            else:
                if not os.path.isdir(fieldDict["resources"][0]):
                    self._displayWarning("The resources install folder %s does not exist." % fieldDict["resources"][0]) 
                    confOk = False
                else:
                    self._folders["resourcesLocation"]=fieldDict["resources"][0]
            return confOk

    def _initializeInstallFolders(self):
        if not installfoldersetterAvailable:
            self._displayError("installfoldersetter tool unavailable. Cannot correct error on module install folders")
            return False
        installFile = "".join([self._configDirectory, "install.dconf"])
    	vst = InstallFolderSetter(verbose = self._verbose, **self._folders) # Tool provides default values for install folders
    	code = vst.process()
        if code == 0:
            return True
        else:   
            self._displayError("Install Folders setting failed with error : %d" % code)
            return False

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
