# Description :
# Define utilitaries to display user defined messages

# Input Variables :
# VERBOSE : Indicates if STATUS messages should be displayed

# Once done this will define :
# displayMessage : function to display applicative message with colors
# ESC_CHAR : escape character of linux console formats
# NO_FORMAT : string allowing to return to default format
# STATUS_FORMAT : string allowing to set format of STATUS messages
# WARNING_FORMAT : string allowing to set format of WARNING messages
# ERROR_FORMAT : string allowing to set format of ERRORS and DEPRECIATION messages

if(NOT WIN32) # Color formatting valid for all systems except Windoze
    string(ASCII 27 ESC_CHAR)
    set(NO_FORMAT "${ESC_CHAR}[0m")
    set(STATUS_FORMAT "${ESC_CHAR}[1;34m") # Light Blue
    set(WARNING_FORMAT "${ESC_CHAR}[1;33m") # Yellow
    set(ERROR_FORMAT "${ESC_CHAR}[1;31m") # Light Red
else() # At the moment does nothing on Windoze (never ever planned to be used with Windoze anyway)
    set(NO_FORMAT "")
    set(STATUS_FORMAT "")
    set(WARNING_FORMAT "")
    set(ERROR_FORMAT "")
endif()

##!
# @brief Display a message with coloration depending on level.
# @param level : Message level
# @param msg : Message to display
#
# Also allows to control display of STATUS messages depending of verbosity
# Based on https://stackoverflow.com/questions/18968979/how-to-get-colorized-output-with-cmake
#
##
function(displayMessage level msg)
    if(${level} STREQUAL STATUS)
        if(NOT VERBOSE) # STATUS MESSAGES ignored if VERBOSE not set
            return()
        endif()
        set(FORMAT "${STATUS_FORMAT}")
    elseif(${level} STREQUAL WARNING OR ${level} STREQUAL AUTHOR_WARNING)
        set(FORMAT "${WARNING_FORMAT}")
    elseif(${level} STREQUAL SEND_ERROR OR ${level} STREQUAL FATAL_ERROR OR ${level} STREQUAL DEPRECATION)
        set(FORMAT "${ERROR_FORMAT}")
    else() # Unknown message level => don't format
        set(FORMAT "")
    endif()

    message(${level} "${FORMAT}${msg}${NO_FORMAT}")
endfunction(displayMessage)

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
