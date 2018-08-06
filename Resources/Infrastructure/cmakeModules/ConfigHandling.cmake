# Description :
# Define utilitaries to handle configuration files

# Input Variables :
# INFRA_MOD_PATH : path to infrasctructure modules

# Once done this will define :

##!
# @brief Store value of a given configuration field into the associated variable
# @param confFile : File containing field
# @param field : Field from which value should be obtained
# @param outputVariable : Variable where result will be stored
##
function(readConfField confFile field outputVariable)
    execute_process(COMMAND bash -c "${INFRA_MOD_PATH}/GetConfField ${confFile} ${field}" OUTPUT_VARIABLE OUT_TMP)
    set(${outputVariable} ${OUT_TMP} PARENT_SCOPE)
endfunction(readConfField)

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
