#!/usr/bin/env python

""" Module infrastructureupdater
A module extending the optparse module to allow a better formatting of option parser help on linux terminal.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

Simple usage example:
	from infrastructureupdater import InfrastructureUpdater

	upd = InfrastructureUpdater(verbose = True)
	upd.update()
"""

__version__ = "1.1.0"

__all__ = ["InfrastructureUpdater"]

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
from subprocess import call

class InfrastructureUpdater:
    def __init__(self, verbose, errorFormat="\033[1;31m", statusFormat="\033[1;32m"):
        ## Update behavior
        self._verbose = verbose
        self._source = "".join([os.environ['SHADE_LOCATION'], "Infrastructure/*"])
        self._destination = os.getcwd()
        ## Styling
        self._noFormat = "\033[0m"
        self._errorFormat = errorFormat
        self._statusFormat = statusFormat
        ## Messaging
        self._errorMsg = ''
        self._statusMsg = ''

    def print_status(self):
        print "********** InfrastructureUpdater **********"
        print "verbose :",self._verbose
        print "source :", self._source
        print "destination :", self._destination
        print "*******************************************"

    def update(self):
        called_prog = self._buildProgramString()
        if(self._verbose):            
            print "Calling Program : ", called_prog
        try:
            call(called_prog, shell=True)
            return 0
        except OSError as e:
            self._errorMsg = "Command call failed with error\n%s" % e
            self._displayError()
            return 1
        except ValueError as e:
            self._errorMsg = "Popen call failed with error\n%s" % e
            self._displayError()
            return 1

    def _displayError(self):
        print "%s%s%s" % (self._errorFormat, self._errorMsg, self._noFormat)

    def _displayStatus(self):
        print "%s%s%s" % (self._statusFormat, self._statusMsg, self._noFormat)

    def _buildProgramString(self):
        program = "rsync"
        arguments = " ".join(self._buildArgumentList())
        return " ".join([program, arguments])

    def _buildArgumentList(self):
        if(self._verbose):
            argument_list=["-v"]
        else:
            argument_list=[]
        argument_list.extend(["-r", "-u", self._source, self._destination])
        return argument_list

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
