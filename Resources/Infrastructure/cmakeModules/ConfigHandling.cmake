# Description :
# Define utilitaries to handle configuration files

# Input Variables :

# Once done this will define :
# readConfField : function to load value of a configuration field into a given variable
# extractFirstLine : function to extract first line of a multiline field value
# CONFIG_HANDLING_LOADED : flag indicating that the config handling module has already been loaded

if(NOT DEFINED CONFIG_HANDLING_LOADED)

    ##!
    # @brief Store value of a given configuration field into the associated variable
    # @param confFile : File containing field
    # @param field : Field from which value should be obtained
    # @param outputVariable : Variable where result will be stored
    ##
    function(readConfField confFile field outputVariable)
        execute_process(COMMAND bash -c "${CMAKE_CURRENT_SOURCE_DIR}/ShadeRun GetConfigField ${confFile} ${field}" OUTPUT_VARIABLE OUT_TMP)
        set(${outputVariable} ${OUT_TMP} PARENT_SCOPE)
    endfunction(readConfField)

    ##!
    # @brief Store into the associated variable the first line (i.e. all before first \n) of a string or the whole string if it only contains a line.
    # @param value : String on which extraction is to be performed
    # @param outputVariable : Variable where result will be stored
    ##
    function(extractFirstLine value outputVariable)
        string(FIND "${value}" "\n" POS)
        if(${POS} EQUAL -1)
            set(OUT_TMP "${value}")
        else()
            string(SUBSTRING "${value}" 0 ${POS} OUT_TMP)
        endif()
        set(${outputVariable} ${OUT_TMP} PARENT_SCOPE)
    endfunction(extractFirstLine)

    set(CONFIG_HANDLING_LOADED TRUE)

endif()

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
