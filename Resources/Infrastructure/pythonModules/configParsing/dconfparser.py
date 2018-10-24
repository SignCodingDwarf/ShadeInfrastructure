#!/usr/bin/env python

""" Module dconfparser
A module containing an object used to parse dconf configuration files

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

Simple usage example:

   from dconfparser import DconfParser

   parser = DconfParser()
   if parser.parseContent("some_dconf_file.dconf") == 0:
       fieldDict = parser.getFileContent()
"""

__version__ = "1.0.0"

__all__ = ["DconfParser"]

__copyright__ = """
Copyright (c) 2018 SignC0dingDw@rf. All rights reserved

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


This program is based on work from Gregory P. Ward under the following license :

Copyright (c) 2001-2006 Gregory P. Ward.  All rights reserved.
Copyright (c) 2002-2006 Python Software Foundation.  All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

  * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

  * Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

  * Neither the name of the author nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
import string
import re

## Local import
fileLocation = os.path.dirname(os.path.realpath(__file__)) # Path where this file is located
imp.load_source("abstractformatparser", "/".join([fileLocation,"abstractformatparser.py"]))
from abstractformatparser import AbstractFormatParser

## Module content
class DconfParser(AbstractFormatParser):
    """
    Class used to parse files formatted as dconf files.
   
    The dconf format is a very simple one in which a config field is declared as <field>=<value>. A value can spawn several lines as long as it does not contain "=" character. No comments are allowed in file.

    Inherits from AbstractFormatParser
    """
    def __init__(self):
        """
        Constructor of the DconfParser class.
        @param self : the object pointer.

        Constructor of the DconfParser class.
        """
        ## Inherited constructors
        AbstractFormatParser.__init__(self, ['.dconf'])

    def _parse(self, configurationFileName):
        """
        Parse configuration file.
        @param self : the object pointer.
        @param configurationFileName : name of the file to parse
        @return True if parsing went fine, False otherwise

        Abstract method must be redefined specifically for each format. Should populate the content dictionnary with file content. No need to reset content dictionnary to None in case of error since wrapping method parseContent already does this.
        """
        self._contentDic = {}
        if not os.path.getsize(configurationFileName) > 0: # Empty file
                return False
        try:
            parsedFile=open(configurationFileName, 'r')
        except IOError as e:
            print "Error opening file %s.\n %s" % (configurationFileName, e)		
            return False
        currentField=""
        lineNb=1
        for line in parsedFile:
            line=re.sub("\n","",line) # Remove new char at the end of the line
            line=re.sub("\s*=\s*","=",line) # Remove any whitespace char around =
            if "=" in line: # Line with new field
                data = line.split("=")
                if len(data) > 2:
                    print "Line", lineNb, "contains several =. Line content is :\n   ", line
                    parsedFile.close()
                    return False
                currentField=data[0]
                if currentField in self._contentDic:
                    self._contentDic[currentField].append(data[1])
                else:
                    self._contentDic[currentField] = [data[1]]
            else: # Continuation of previous field
                if currentField == "":
                    print "Line", lineNb, "value declared without associated field. Line content is :\n   ", line
                    parsedFile.close()
                    return False
                self._contentDic[currentField][-1] += "\n"+line        
            lineNb+=1
        parsedFile.close()
        return True

## Module Testing
if __name__ == "__main__":
    import sys  
    from tempfile import NamedTemporaryFile

    parser = DconfParser()

    ### Create test files
    try:
        testFiles=[NamedTemporaryFile(mode="w+", prefix="/tmp/", suffix=".dConF", bufsize=0, delete=True) for i in range(3)]
    except IOError as e:	
        print e	
        sys.exit(1)

    ### Populate them
    # File is OK
    testFiles[0].write("FieldA= value0\n")
    testFiles[0].write("FieldB=value1\n")
    testFiles[0].write("FieldC =value2 value3\n")
    testFiles[0].write("multilineEntry1\n")    
    testFiles[0].write("FieldB=     value4\n")
    testFiles[0].write("FieldB=42\n")
    testFiles[0].write("FieldA= value5\n")
    testFiles[0].write("multilineEntry2\n")
    testFiles[0].write("multilineEntry3")
    # Error : Multiple = in line
    testFiles[1].write("FieldA= value0\n")
    testFiles[1].write("FieldB=value1\n")
    testFiles[1].write("FieldC =value2=value3\n")
    testFiles[1].write("multilineEntry1\n")    
    # Error : Starts with no field
    testFiles[2].write("Beginning of file\n")
    testFiles[2].write("FieldA= value0\n")
    testFiles[2].write("FieldB=value1\n")
    testFiles[2].write("FieldA= value5\n")
    testFiles[2].write("multilineEntry2\n")
    testFiles[2].write("multilineEntry3")  

    ### File with content        
    assert parser.parseContent(testFiles[0].name) == 0
    assert parser.getFileContent() == {'FieldA': ['value0', 'value5\nmultilineEntry2\nmultilineEntry3'], 'FieldB': ['value1', 'value4', '42'], 'FieldC': ['value2 value3\nmultilineEntry1']}

    ### Files with error        
    assert parser.parseContent(testFiles[1].name) == 3 and parser.getFileContent() is None
    assert parser.parseContent(testFiles[2].name) == 3 and parser.getFileContent() is None
    
    ### And delete them 
    for testFile in testFiles:      
        testFile.close()

    print "OK"
    sys.exit(0)

