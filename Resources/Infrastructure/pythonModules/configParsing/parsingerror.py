#!/usr/bin/env python

""" Module parsingerror
A module containing exceptions that can be raised during parsing

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>
"""

__version__ = "1.0.0"

__all__ = ["ParsingError, FileError, ExtensionError, FormatError"]

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
## Module content
class ParsingError(RuntimeError):
    """
    Base class of all parsing exceptions

    Simply contains a string detailling error cause

    Inherits from RuntimeError
    """
    def __init__(self, message):
        """
        Constructor of the ParsingError class.
        @param self : the object pointer.
        @param message : Error message

        Constructor of the ParsingError class.
        """
        ## Inherited constructors
        RuntimeError.__init__(self, message)


class FileError(ParsingError):
    """
    Exception raised when there is an issue with configuration file that prevent its opening

    Typical errors this makes appear are that the file does not exist or that the user has not the appropriate rights on the file

    Inherits from ParsingError
    """
    def __init__(self, filePath, errorCause):
        """
        Constructor of the FileError class.
        @param self : the object pointer.
        @param filePath : Path to the configuration file
        @param errorCause : Message explaining what went wrong

        Constructor of the FileError class.
        """
        ## Inherited constructors
        ParsingError.__init__(self, "Opening %s file failed because of error:\n%s" % (filePath, errorCause))

class ExtensionError(ParsingError):
    """
    Exception raised when the extension of configuration file does not match the one expectedby parser

    Inherits from ParsingError
    """
    def __init__(self, filePath, extension, expectedExtensions):
        """
        Constructor of the ExtensionError class.
        @param self : the object pointer.
        @param filePath : Path to the configuration file
        @param extension : The extension extracted by parser
        @param expectedExtensions : The list of extensions accepted by parser

        Constructor of the ExtensionError class.
        """
        ## Inherited constructors
        ParsingError.__init__(self, "The configuration file %s has wrong extension %s. Supported file extensions are \n%s" % (filePath, extension, " ; ".join(expectedExtensions)))   

class FormatError(ParsingError):
    """
    Exception raised if parser detects errors in file formatting.

    Inherits from ParsingError
    """
    def __init__(self, filePath, errors):
        """
        Constructor of the ExtensionError class.
        @param self : the object pointer.
        @param filePath : Path to the configuration file
        @param errors : A list of detected errors

        Constructor of the FormatError class.
        """
        ## Inherited constructors
        ParsingError.__init__(self, "Parsing of file %s failed with errors:\n%s" % (filePath, "\n".join(errors)))   

## Module Testing
if __name__ == "__main__":
    try:
        raise FileError("/toto/tmp.dconf", "File does not exist")
    except FileError as e:
        print e

    print "******************************"

    try:
        raise ExtensionError("/toto/tmp.dcfg", ".dcfg", [".dconf"])
    except ExtensionError as e:
        print e

    print "******************************"

    try:
        raise ExtensionError("/toto/tmp.dcf", ".dcf", [".dconf", ".dconfig"])
    except ExtensionError as e:
        print e

    print "******************************"

    try:
        raise FormatError("/toto/tmp.dcf", ["Line 1 : Missing file Header", "Line 5 : Invalid field \"Elf\"", "Line 15 : Missing }"])
    except FormatError as e:
        print e

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
