/*!
 * @file common_defines.h
 * @brief Common Macros Definition
 * @author Sign Coding Dwarf
 * @version 1.0
 * @date 21 March 2016
 *
 * Definition of macros common to all designed applications
 *
 */

#ifndef COMMON_DEFINES
#define COMMON_DEFINES

///////////////////////////// Global defines

/*! 
* @def EXEC_SUCCESS
* @brief Execution of a function succeeded
*/
#ifndef EXEC_SUCCESS
#define EXEC_SUCCESS 0 
#endif

/*! 
* @def EXEC_FAILURE
* @brief Execution of a function failed
*/
#ifndef EXEC_FAILURE
#define EXEC_FAILURE 1
#endif

#ifndef DEBUG
/*! 
* @def DEBUG
* @brief Preprocessor to enable debug output
*
* DEBUG is used to perform debug mode specific operations. Set to 1 (default value) to enable and to 0 to disable. Change value in \a common_defines.h or as compiling preprocessor flag (recommended) : \a -DDEBUG=0 <br>
* This macro can be complemented/replaced by NDEBUG macro if needed
*
*/
#define DEBUG 1 // Default behavior is debug enabled
#endif


///////////////////////////// Check the use of features

#if __cplusplus >= 201103L // Compiler supports C++11
#ifndef USE_SHARED_POINTERS
/*! 
* @def USE_SHARED_POINTERS
* @brief Check if shared pointers can be used
*
*  Checking if shared pointers use is allowed is done with \#if USE_SHARED_POINTERS. By default this choice is determined by compiler support of C++11. However a different choice can be specified using compiling preprocessor flag : \a -DUSE_SHARED_POINTERS=\<value\>
*
*/
#define USE_SHARED_POINTERS 1
#endif

#else // Compiler does not support C++11

#ifndef USE_SHARED_POINTERS
#define USE_SHARED_POINTERS 0
#endif

#endif

#endif

//  ______________________________
// |                              |
// |    ______________________    |       
// |   |                      |   |
// |   |         sign         |   |
// |   |        coding        |   |
// |   |        dw@rf         |   |
// |   |         1.0          |   |
// |   |______________________|   |
// |                              |
// |______________________________|
//               |  |           
//               |  |             
//               |  |
//               |  |
//               |  |
//               |  |
//               |  |
//               |  |
//               |  |
//               |  |
//               |  |
//               |__|

