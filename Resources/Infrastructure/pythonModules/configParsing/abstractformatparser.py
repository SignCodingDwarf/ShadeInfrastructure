#!/usr/bin/env python

""" Module abstractformatparser
A module defining the base structure of all format parsing classes.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

A parser build according to this class will be initialized to precise the expected file extensions associated with the format. 

Then it will extract all fields in the file and will give access to them in a dictionnary associating field tags with the associated values ordered by extraction.
"""

__version__ = "1.0.0"

__all__ = ["AbstractFormatParser"]

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
import abc
import string
import os

## Module content
class AbstractFormatParser:
    """
    Interface class for all format parsers

    Provides common methods used by all classes. The format specific operations are performed in the _parse method which must be redefined by every class inheriting this one.

    Abstract class.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, extensionList):
        """
        Constructor of the AbstractFormatParser class.
        @param self : the object pointer.
        @param extensionList : The list of file extensions associated with the format the class can parse. Extension testing is not case sensitive and must start with a dot.

        Constructor of the AbstractFormatParser class.
        """
        ## Extension
        self._extensionList = [self._formatExt(extension) for extension in extensionList]
        ## Content self._contentDic = None (will value None till parseContent has not been called or if it was not successfull)
        self._contentDic = None

    def getFileContent(self):
        """
        Get content of the last parsed file.
        @param self : the object pointer.
        @return The dictionnary containing the content of the last parsed file or None if either no file was parsed or parsing failed.
        """
        return self._contentDic

    def parseContent(self, configurationFileName):
        """
        Extract all fields contained in a configuration file
        @param self : the object pointer.
        @param configurationFileName : name of the file to parse
        @return A code indicating what happened during parsing

        Parse a configuration and populate the content map with fields associated with their values. The function can return one of the following codes depending on how parsing took place : <br>
        - 0 : The file could be parsed <br>
        - 1 : File does not exist <br>
        - 2 : Wrong file extension <br>
        - 3 : File could not be parsed or contain format errors. <br>
        If the return code is not 0, the content dictionnary will be reset to None
        """
        self._contentDic = None
        if not os.path.isfile(configurationFileName):
            return 1
        if not self._getFileExtension(configurationFileName) in self._extensionList:
            return 2
        if not self._parse(configurationFileName):
            self._contentDic = None # Reset to None in case of error because we have no guarantee on map state
            return 3
        return 0

    def _formatExt(self, extension):
        """
        Format extension as starting with a dot and containing only upper characters.
        @param self : the object pointer.
        @param extension : name of the file to parse
        @return The formatted extension
        """
        extension = extension.upper() # All characters as upper char
        if extension[0] == ".":
            return extension
        else:
            return "." + extension

    def _getFileExtension(self, configurationFileName):
        """
        Get the extension of the configuration file.
        @param self : the object pointer.
        @param configurationFileName : name of the file to parse
        @return The extension starting with a dot and with upper characters. Empty string if file has no extension.
        """
        dotIndex = string.rfind(configurationFileName, ".")
        if dotIndex == -1:
            return ""        
        return configurationFileName[dotIndex:].upper()

    @abc.abstractmethod
    def _parse(self, configurationFileName):
        """
        Parse configuration file.
        @param self : the object pointer.
        @param configurationFileName : name of the file to parse
        @return True if parsing went fine, False otherwise

        Abstract method must be redefined specifically for each format. Should populate the content dictionnary with file content. No need to reset content dictionnary to None in case of error since wrapping method parseContent already does this.
        """
        return

## Module Testing
if __name__ == "__main__":
    import sys  
    from tempfile import NamedTemporaryFile

    class TestParser(AbstractFormatParser):
        def __init__(self):
            AbstractFormatParser.__init__(self, [".tmp", "toTo"])
            print "Supported extensions : ", self._extensionList 

        def _parse(self, configurationFileName): # A very basic parsing for test purport. It is not really robust
            self._contentDic = {}            
            if not os.path.getsize(configurationFileName) > 0: # Empty file
                return False
            try:
                parsedFile=open(configurationFileName, 'r')
            except IOError as e:		
                return False            
            for line in parsedFile:
                values=line.replace("\n", "").split(" ")
                self._contentDic[values[0]]=values[1]
            parsedFile.close()
            return True

    parser = TestParser()
    assert parser.getFileContent() is None
    assert parser.parseContent("/tmp/this_file_does_not_even_exist") == 1 and parser.getFileContent() is None

    ### Create a few test files
    testFileExtensions=[".tmp", ".TotO", "", ".KO"]
    try:
        testFiles=[ NamedTemporaryFile(mode="w+", prefix="/tmp/", suffix=extension, bufsize=0, delete=True) for extension in testFileExtensions ]
    except IOError as e:	
        print e	
        sys.exit(1)

    ### Populate them
    testFiles[0].write("FieldA value0\n")
    testFiles[0].write("FieldB value1\n")
    testFiles[0].write("FieldC value2\n")

    ### Wrong extensions
    assert parser.parseContent(testFiles[2].name) == 2 and parser.getFileContent() is None
    assert parser.parseContent(testFiles[3].name) == 2 and parser.getFileContent() is None

    ### File with content        
    assert parser.parseContent(testFiles[0].name) == 0 and parser.getFileContent() == {'FieldA':'value0','FieldB':'value1','FieldC':'value2'} 
    
    ### Parse error due to empty file
    assert parser.parseContent(testFiles[1].name) == 3 and parser.getFileContent() is None

    ### And delete them 
    for testFile in testFiles:      
        testFile.close()

    sys.exit(0)
