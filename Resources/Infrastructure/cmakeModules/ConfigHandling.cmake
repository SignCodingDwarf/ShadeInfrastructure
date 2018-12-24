# Description :
# Define utilitaries to handle configuration files

# Input Variables :

# Once done this will define :
# readConfField : function to load value of a configuration field into a given variable
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
