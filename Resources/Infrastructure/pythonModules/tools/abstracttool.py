#!/usr/bin/env python

## Future import must be at the beginning of the file
from __future__ import print_function

""" Module abstracttool
A Module defining the base structure of all infrastructure tools.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

A tool constructed following this class only needs to be configured via the objetc constructor and then call the process() method to do the job.

The process() mehtod shall return an error code which will be used as tool command return code.
"""

__version__ = "0.2.0"

__all__ = ["AbstractTool"]

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
import abc
import sys

## Module content
class AbstractTool:
    __metaclass__ = abc.ABCMeta

    def __init__(self, verbose, errorFormat="\033[1;31m", warningFormat="\033[1;33m", statusFormat="\033[1;32m"):
        ## Verbose Mode
        self._verbose = verbose
        ## Styling
        self._noFormat = "\033[0m"
        self._errorFormat = errorFormat
        self._warningFormat = warningFormat
        self._statusFormat = statusFormat

    @abc.abstractmethod
    def process(self):
        return

    def _displayError(self, msg):
        print("%s%s%s" % (self._errorFormat, msg, self._noFormat), file=sys.stderr)

    def _displayWarning(self, msg):
        print("%s%s%s" % (self._warningFormat, msg, self._noFormat), file=sys.stderr)

    def _displayStatus(self, msg):
        if self._verbose:
            print("%s%s%s" % (self._statusFormat, msg, self._noFormat), file=sys.stderr)

## Module Testing
if __name__ == "__main__":
    import sys

    class TestAT(AbstractTool):
        def __init__(self):      
            AbstractTool.__init__(self, True)
        
        def process(self):
            self._displayError("An elf")
            self._displayWarning("A hord of armed goblins")
            self._displayStatus("I'm drunk")
            return 0

    
    testObj = TestAT()
    code = testObj.process()

    sys.exit(code)

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

