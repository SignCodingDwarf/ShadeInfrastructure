#!/usr/bin/env python

""" Module dwfoptparse
A module extending the optparse module to allow a better formatting of option parser help on linux terminal.

By SignC0dingDw@rf <dwarfcieofchaos@gmail.com>

More on https://github.com/SignCodingDwarf/DwfPython/wiki

Simple usage example:

   from dwfoptparse import DwfOptionParser
   from dwfoptparse import DwfHelpFormatter

   dwfFormatter = DwfHelpFormatter()
   parser = DwfOptionParser(formatter = dwfFormatter)
   parser.add_option("-a", "--axe", dest="goblin",
                     help="axe a goblin's face", metavar="GOBLIN_FACE")
   parser.add_option("-r", "--rich",
                     action="store_true", dest="you", default=False,
                     help="get rich (only if you are a dwarf)")

   (options, args) = parser.parse_args()
"""

__version__ = "1.0.0"

__all__ = ["DwfHelpFormatter",
	   "DwfOptionParser"]

__copyright__ = """
Copyright (c) 2017 SignC0dingDw@rf. All rights reserved

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
from optparse import OptionParser
from optparse import OptionContainer
from optparse import IndentedHelpFormatter
import sys
import platform
import textwrap

class DwfHelpFormatter (IndentedHelpFormatter):
	"""
	Format help and allow it to be colored for a more user friendly output on linux Console.

	Allow to define and enable or disable help coloration for linux console. Colors are defined using the 16 colors escape sequences.
	See http://misc.flogisoft.com/bash/tip_colors_and_formatting#colors for more details.
	Colors sequences are automatically escaped if output is not linux terminal or if color use is disabled in constructor by setting useColors 		to False. 

	Inherits from IndentedHelpFormatter.
	"""
	def __init__(self, max_help_position=30, useColors=True, usageColor="\033[1;34m", headingColor="\033[1;33m", descriptionColor="\033[1;31m", optionsColor="\033[1;32m", epilogColor="\033[1;31m",):
		"""
		Constructor of the DwfHelpFormatter class.
		@param self : the object pointer.
		@param max_help_position : starting column of the help text. Default is 30.
		@param useColors : enable or disable the use of color formats. Default is True.
		@param usageColor : color of the command usage text.
		@param headingColor : color of the group heading text.
		@param descriptionColor : color of the command description text.
		@param optionsColor : color of the options.
		@param epilogColor : color of the help epilog text.

		Constructor of the DwfHelpFormatter class used to set formatting of help text and enable or disable this formatting.
		"""
		IndentedHelpFormatter.__init__(self, indent_increment=0, max_help_position=max_help_position, width=None, short_first=True)
		self._isLinuxKSL = False # Know if linux konsole
		self._useColors = useColors # Use console color str if available
		self._usageColor = usageColor
		self._descriptionColor = descriptionColor
		self._headingColor = headingColor
		self._optionsColor = optionsColor
		self._epilogColor = epilogColor
		self._noColor = "\033[0m"
		self.option_raw_strings = {}
		self._short_opt_fmt = "%s [%s]"
		self._long_opt_fmt = "%s=[%s]"


	def setLinuxKSL(self, isLinuxKSL):
		"""
		Set if linux console is used as output.
		@param self : the object pointer.
		@param isLinuxKSL : is linux consule used as output.

		Set if linux console is used as output. This method is normally used within the DwfOptionParser class. However, if you use the standard OptionParser class, you can set it before passing formatter to class constructor.
		"""
		self._isLinuxKSL = isLinuxKSL

	def format_usage(self, usage):
		"""
		Format usage displayed text.
		@param self : the object pointer.
		@param usage : usage text.

		Format usage text being displayed using print_help() and print_usage() methods.
		Usage text is displayed as :
		
		Usage

		 <usage>

		"""
		result = ["Usage\n\n"]
		if self._isLinuxKSL and self._useColors:
			result.append(self._usageColor);
		result.append(" %s\n");
		if self._isLinuxKSL and self._useColors:
			result.append(self._noColor);
		return ("".join(result)) % usage

	def format_description(self, description):
		"""
		Format description displayed text.
		@param self : the object pointer.
		@param description : description text.

		Format description text being displayed using print_help() method. This redefinition of format_description() allows to display description with formatting and to use line feed character to display text on multiple lines. 
		"""
		if description:
			if self._isLinuxKSL and self._useColors:
				return self._descriptionColor + description + self._noColor + "\n"
			else:			
				return description + "\n"
		else:
			return ""

	def format_epilog(self, epilog):
		"""
		Format epilog displayed text.
		@param self : the object pointer.
		@param epilog : epilog text.

		Format epilog text being displayed using print_help() method. This redefinition of format_epilog() allows to display epilog with formatting and to use line feed character to display text on multiple lines. 
		"""
		if epilog:
			if self._isLinuxKSL and self._useColors:
				return "\n" + self._epilogColor + epilog + self._noColor + "\n"
			else:			
				return "\n" + epilog + "\n"
		else:
			return ""

	def format_heading(self, heading):
		"""
		Format group heading displayed text.
		@param self : the object pointer.
		@param heading : heading group name.

		Format heading name of option groups displayed using print_help() method.
		Heading text is displayed as :

		----- <heading> -----
		"""
		result = []
		if self._isLinuxKSL and self._useColors:
			result.append(self._headingColor);
		result.append("----- %s -----\n")
		if self._isLinuxKSL and self._useColors:
			result.append(self._noColor);		
	        return "".join(result) % heading

	def store_option_strings(self, parser):
		"""
		List all options and their help strings.
		@param self : the object pointer.
		@param parser : option parser.

		Produce the list of option and help text for all options. They are stored both as full string with formatting and as raw strings without because formatting strings would lead to wrong size and position computation. 
		"""
		self.indent()
		max_len = 0
		for opt in parser.option_list:
			strings, raw = self.format_option_strings(opt)			
			self.option_strings[opt] = strings
			self.option_raw_strings[opt] = raw
			max_len = max(max_len, len(raw) + self.current_indent)
		self.indent()
		for group in parser.option_groups:
			for opt in group.option_list:
				strings, raw = self.format_option_strings(opt)
				self.option_strings[opt] = strings
				self.option_raw_strings[opt] = raw
				max_len = max(max_len, len(raw) + self.current_indent)
		self.dedent()
		self.dedent()
		self.help_position = min(max_len + 2, self.max_help_position)
		self.help_width = self.width - self.help_position

    	def format_option(self, option):
		"""
		Format option and help displayed text.
		@param self : the object pointer.
		@param option : options and help text.

		Format option ans displayed text. Very similar to formatting of motherclass IndentedHelpFormatter except that it uses raw option strings size to compute help text position.
		"""
		result = []
		opts = self.option_strings[option]
		raw = self.option_raw_strings[option]
		opt_width = self.help_position - self.current_indent - 2
		if len(raw) > opt_width:
		    opts = "%*s%s\n" % (self.current_indent, "", opts)
		    indent_first = self.help_position
		else:                       # start help on same line as opts
		    opts = "%*s%s" % (self.current_indent, "", opts)
		    indent_first = self.help_position-len(raw)
		result.append(opts)
		if option.help:
		    help_text = self.expand_default(option)
		    help_lines = textwrap.wrap(help_text, self.help_width)
		    result.append("%*s%s\n" % (indent_first, "", help_lines[0]))
		    result.extend(["%*s%s\n" % (self.help_position, "", line)
		                   for line in help_lines[1:]])
		elif opts[-1] != "\n":
		    result.append("\n")
		return "".join(result)

	def format_option_strings(self, option):
		"""
		Format a list of option strings and metavariables.
		@param self : the object pointer.
		@param option : list of alternatives for each given option.	

		Return two list of option strings & metavariables separated by or. The first one contains option list formatted for linux console and the second one as raw text for an easier option string length estimation.
		"""
		if option.takes_value():
			metavar = option.metavar or option.dest.upper()
			short_opts_raw = [self._short_opt_fmt % (sopt, metavar)
				  for sopt in option._short_opts]
			long_opts_raw = [self._long_opt_fmt % (lopt, metavar)
				  for lopt in option._long_opts]
		else:
			short_opts_raw = option._short_opts
			long_opts_raw = option._long_opts

		if self._isLinuxKSL and self._useColors:
			form = "".join([self._optionsColor, "%s", self._noColor])
			short_opts = [form % soptr for soptr in short_opts_raw]
			long_opts = [form % loptr for loptr in long_opts_raw]
		else:
			short_opts = short_opts_raw
			long_opts = long_opts_raw

		if self.short_first:
			raw = short_opts_raw + long_opts_raw
			opts = short_opts + long_opts
		else:
			raw = long_opts_raw + short_opts_raw
			opts = long_opts + short_opts

		return " or ".join(opts), " or ".join(raw)

###################################################################################################################################

class DwfOptionParser(OptionParser):
	"""
	Modified parser to allow a better formatting of output.

	Allow to sligthly modify the display of help as well as notify the DwfHelpFormatter if output is displayed to linux console or not.
	Otherthe same functionnalities than the standard OptionParser class. The only difference apart on formatting management is that constructor only accepts usage, version, description, epilog and formatter parameters.	

	Inherits from OptionParser.
	"""
	def __init__(self,
                 usage=None,
                 version=None,
                 description=None,
                 formatter=None,
                 epilog=None):
		"""
		Constructor of the DwfOptionParser class.
		@param self : the object pointer.
		@param usage : usage string. Default is "%prog [options]".
		@param version : program version. Default is None and --version option creates an error.
		@param description : program description. Default is None and no help description is displayed.
		@param formatter : formatter allowing to control how help string is displayed. Default is IndentedHelpFormatter.
		@param epilog : help epilog. Default is None and no help epilog is displayed.

		Constructor of the DwfOptionParser class used to manage command line options.
		"""
		OptionParser.__init__(
		self, usage=usage, version=version, description=description,formatter=formatter,epilog=epilog)

	def print_help(self, file=None):
		"""
		Print program help.
		@param self : the object pointer.
		@param file : flux to which write data. Default is linux console (stdout)	

		Modified version of the OptionParser program help print function. Adds especially the notice to the DwfHelpFormatter class of whether linux console is used.
		"""
		if file is None:
		    file = sys.stdout
		    if isinstance(self.formatter, DwfHelpFormatter): 
		    	self.formatter.setLinuxKSL(platform.system() == "Linux")
		encoding = self._get_encoding(file)
		file.write(self.format_help().encode(encoding, "replace"))

	def format_option_help(self, formatter=None):
		"""
		Format help displayed.
		@param self : the object pointer.
		@param formatter : formatter allowing to control how help string is displayed. Default is the formatter set at object construction.

		Modified version of the OptionParser help formatting function to make it compatible with Dwarven help styling.
		"""
		if formatter is None:
			formatter = self.formatter
		formatter.store_option_strings(self)
		result = ["Options:\n"]
		result.append(formatter.format_heading("General Options"))
		formatter.indent()
		if self.option_list:
			result.append(OptionContainer.format_option_help(self, formatter))
		    	result.append("\n")
		for group in self.option_groups:
		    	result.append(group.format_help(formatter))
		    	result.append("\n")
		formatter.dedent()
		# Drop the last "\n", or the header if no options or option groups:
		return "".join(result[:-1])

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
