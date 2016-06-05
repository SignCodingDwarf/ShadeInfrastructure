# ShadeInfrastructure
A CMake based infrastructure for library or executable compilation on Linux

Comprehensive development infrastructure allowing to release libraries and executable in a homogeneous and efficient way

## TODO

Improve FindQt module

## Modifications History

### April 10 2016

Modified doc/.DoxyDoc file :
- Changed working and code directories to local directories
- Code contained in test directory is now ignored when generating documentation

### April 16 2016

Modified CMakeLists.txt file : 
- Remove display message of header_install
- Remove validity check of Xerces since it is performed in the dedicated module
- Added GENERATE\_DYNAMIC\_LIBRARY variable to handle the case of using a static library for compilation (because then, a dynamic library could not be used)

Updated and commented FindXerces.cmake and especially modified handling of XERCESC\_STATIC variable and of path locations. Also added a more informative error message.

### April 17 2016
Modified FindXerces.cmake :
- Modified the management and use of XERCESC\_FIND\_QUIETLY
- Corrected a bug of variable XERCESC\_WAS\_STATIC not stored in cache

### June 04 2016
Modified SetUpConfigurationFlags.cmake and common_defines.h :
- Added management of USE\_AUTO\_LOOPS preprocessor flag to enable/disable use of C++11 range based loop syntax
