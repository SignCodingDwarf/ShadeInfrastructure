#!/usr/bin/env python

""" Module configparser
A module containing an object used to parse configuration files according different formats

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

Simple usage example:

   from configparser import ConfigParser

   parser = ConfigParser("configFile.dconf")
   fieldsList = ["field1", "field2", "field3"]

   fieldDict = parser.extractFields(fieldsList)
"""

__version__ = "1.0.0"

__all__ = ["ConfigParser"]

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

## Local import
fileLocation = os.path.dirname(os.path.realpath(__file__)) # Path where this file is located
imp.load_source("dconfparser", "/".join([fileLocation,"dconfparser.py"]))
imp.load_source("abstractformatparser", "/".join([fileLocation,"abstractformatparser.py"]))
from dconfparser import DconfParser
from abstractformatparser import AbstractFormatParser

## Temporary here 
## TODO move to utils
## based on https://stackoverflow.com/questions/11461356/issubclass-returns-false-on-the-same-class-imported-from-different-paths
import inspect

def inherits_from(child, parent_name):
    if inspect.isclass(child) and inspect.isclass(parent_name):
        if inspect.getmro(parent_name)[0].__name__ in [c.__name__ for c in inspect.getmro(child)[1:]]:
            return True
    return False

## Module content
class ConfigParser:
    """
    Generic configuration file parser.

    Generic class used to parse configuration file. The syntax specific operations are provided by the formatParser constructor argument. Default if not specified uses the dwarven specific dconf format. Another argument allows to indicate what to do in case the configuration value is present multiple times. You can either list all values or simply return the first one.
    """
    def __init__(self, configFileName, multiEntryParse=False, formatParser=DconfParser()):
        """
        Constructor of the DwfOptionParser class.
        @param self : the object pointer.
        @param configFileName : Name of the file containing configuration fields.
        @param multiEntryParse : Set to true to concatenate all entries for a field. Default is false which only returns value associated with the first occurence of field
        @param formatParser : Parser associated with configuration file format. Default uses dwarven specific dconf format.

        Constructor of the ConfigParser class.
        """
        ## Configuration
        self._configFileName = configFileName
        self._multiEntryParse = multiEntryParse
        ## Set parser
        self._formatParser=formatParser
        if not inherits_from(type(self._formatParser),AbstractFormatParser):
            raise TypeError("Proposed parser is of type %s which does not inherit AbstractFormatParser" % type(self._formatParser))
            self._formatParser=None

    def extractFields(self, fieldList):
        """
        Extract value(s) associated with the provided field list.
        @param self : the object pointer.
        @param fieldList : The list of fields to extract.
        @return A dictionnary matching field with a pair <value list, exec code>. Returns None if list is empty or if parser is not working

        Extract from the configuration file the value(s) associated with a field list. <br>
        The output is returned as a dictionnary matching the field with a pair containing the string value(s) list and an exec code. <br>
        The value list can either be None (it is always matched with a non zero exec code to explain error reason), contain exactly one element (the first occurence of field encountered) if multiEntryParse is set to False and no error occured or contain one or more elements if multiEntryParse is set to True. <br>
        The exec code can have the following values : <br>
        - 0 : the field could be parsed <br>
        - 1 : configuration file does not exist <br>
        - 2 : file extension does not match the extension expected by format parser <br>
        - 3 : parser could not parse file <br>
        - 4 : provided field does not exist <br>
        """
        if fieldList is None or len(fieldList) == 0 or self._formatParser is None: 
            return None
        fieldDic = {field:(None,0) for field in fieldList} # fill dict with keys    
        parseCode = self._formatParser.parseContent(self._configFileName)
        if parseCode > 0:
            fieldDic = {key:(None,parseCode) for key in fieldDic.keys()} # Set content of all keys with error return code
        else:
            fileContent = self._formatParser.getFileContent()
            for key in fieldDic.keys():
                if key in fileContent.keys():
                    if self._multiEntryParse:
                        fieldDic[key]=(fileContent[key], 0)
                    else:
                        fieldDic[key]=([fileContent[key][0]], 0) # One element list
                else :
                        fieldDic[key]=(None, 4)
        return fieldDic

## Module Testing
if __name__ == "__main__":
    import sys
    from tempfile import NamedTemporaryFile

    ### Parser errors
    errorInit=False
    try:
        failingParser1 = ConfigParser("/tmp/test.dconf", True, dict())
    except TypeError as e:	
        print e
        errorInit=True	

    assert errorInit 

    errorInit=False
    try:
        failingParser2 = ConfigParser("/tmp/test.dconf")
    except TypeError as e:	
        print e
        errorInit=True	
    assert not errorInit
    assert failingParser2.extractFields([]) is None
    assert failingParser2.extractFields(None) is None
    assert failingParser2.extractFields(["FieldA","FieldB"]) == {'FieldA': (None, 1), 'FieldB': (None, 1)}

    ### Create test File
    try:
        testFiles=[NamedTemporaryFile(mode="w+", prefix="/tmp/", suffix=".dconf", bufsize=0, delete=True) for i in range(1)]
    except IOError as e:	
        print e	
        sys.exit(1)

    ### Create OK Parser with no multi entry
    errorInit=False
    try:
        noMultiParser = ConfigParser(testFiles[0].name)
    except TypeError as e:	
        print e
        errorInit=True	
    assert not errorInit
    assert noMultiParser.extractFields(["FieldA","FieldB"]) == {'FieldA': (None, 3), 'FieldB': (None, 3)}

    ### Populate it
    testFiles[0].write("FieldA= value0\n")
    testFiles[0].write("FieldB=value1\n")
    testFiles[0].write("FieldC =value2 value3\n")
    testFiles[0].write("multilineEntry1\n")    
    testFiles[0].write("FieldB=     value4\n")
    testFiles[0].write("FieldB=42\n")
    testFiles[0].write("FieldA= value6\n")
    testFiles[0].write("multilineEntry2\n")
    testFiles[0].write("multilineEntry3")

    ### Test Parsing
    assert  noMultiParser.extractFields(["FieldA","FieldB", "FieldC", "FieldD"]) == {'FieldA': (["value0"], 0), 'FieldB': (["value1"], 0), 'FieldC': (["value2 value3\nmultilineEntry1"], 0), 'FieldD': (None, 4)}

    ### Create OK Parser with multi entry
    errorInit=False
    try:
        multiParser = ConfigParser(testFiles[0].name, True)
    except TypeError as e:	
        print e
        errorInit=True	
    assert not errorInit

    assert  multiParser.extractFields(["FieldA", "FieldC", "FieldD"]) == {'FieldA': (["value0", "value6\nmultilineEntry2\nmultilineEntry3"], 0), 'FieldC': (["value2 value3\nmultilineEntry1"], 0), 'FieldD': (None, 4)}
    assert  multiParser.extractFields(["FieldB"]) == {'FieldB': (["value1", "value4", "42"], 0)}

    print "OK"
    sys.exit(0)
