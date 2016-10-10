#!/bin/bash

# file : createModule.sh
# author : SignCodingDwarf
# version : 1.0
# date : 06 October 2016
# Definition of interface management variables and functions

### Global variables
# Interface output
user_input="" # Data gathered from the interface
interface_status=-1 # Status of interface execution

# Progress Bar
progress_bar_status=-1 # Status of the progress bar
progress_pipe="progress.pipe" # File to which redirect progress bar updates for monitoring by zenity
tail_pid="tail_pid.txt" # File that will contain the PID of the tail process to kill it at clean up

### Functions
##!
# @brief Create the graphical interface and set up variable containing its output
# @param 1 : Separator between output data as a string
#
# Creates a Zenity based interface for the CMake library finder generator. 
# The user_input variable is set with the content entered by the user.
# The interface_status variable is set with the return code of the interface.
#
##
createZenityInterface() {
	user_input=$(
		zenity  --forms --title="CMake library  finder module generator" \
			--text="Enter information on the library" \
			--separator=$1 \
			--add-entry="Library Name" \
			--add-entry="Include file" \
			--add-entry="Include suffixes"
			# --add-entry="Location" #\
	)
	interface_status=$? # Get the interface status
}

##!
# @brief Reacts to the status of a Zenity interface
# @param 1 : Interface status as an integer
# @param 2 : Display color for status messages.
# @param 3 : Display color for error messages.
#
# Decide of the action to perform depending on the status of a zenity interface.
# If user selected OK, continue execution.
# If user canceled, apllication exits with error code 0.
# If error occured, display error and exit with error code 1.
#
##	
zenityInterfaceStatus() {
	case $1 in
	    0) # User selected OK
		echo "$2Library data set up ${NC}"
		;;
	    1) # User selected cancel
		echo "$2Module creation was cancelled"
		echo "Exiting ${NC}"
		exit 0
		;;
	    5) #Timeout
		echo "$3Timeout on the dialog box"
		echo "Exiting ${NC}"
		exit 1
		;;
	    *) # Unknown error
		echo "$3An unknown error occured"
		echo "Exiting ${NC}"
		exit 1
		;;
	esac
}

##!
# @brief Creates a process independent Zenity progress bar and the pipe file used to update progress.
#
# Creates a Zenity progress bar. The bar is created in an independent process so that main script is not blocked by progress display.
# The function also creates or empties the file  defined by the progress_pipe variable which is used to update data of the progress bar.
# The content of the tail_pid file is set to the current pid of the tail process used to update progress bar so that process can be killed at clean up.
# Finally variable progress_bar_status is updated with the progress bar status.
#
##
createZenityProgressBar() {
	# Create pipe file if it does not exist or empty it otherwise
	if [ -f ${progress_pipe} ]; then
		: > ${progress_pipe}
	else
		touch ${progress_pipe}
	fi
# Use tail to monitor file updates and pipe them to the progress bar
	(
		tail -f ${progress_pipe} & echo $! > ${tail_pid}
	) | zenity  --progress \
		    --title="File Generation" \
  		    --percentage=0 \
		    --text="Starting ..." \
		    --auto-close & # Progress bar is closed when progress reaches 100% and is running in a separate process

	progress_bar_status=$? # Get status of progress bar
}

##!
# @brief Updates the progress bar
# @param 1 : Percentage of progress as an unsigned integer between 0 and 100.
# @param 2 : Text to display, optionnal parameter.
# @param 3 : Text color for warning, optionnal parameter, default is yellow.
#
# Updates the progress bar with the desired text and percentage or displays a warning if progress bar is not running.
# Updates displayed text only if the second function parameter is not empty.
# Progress value is clamped in range [0 100] and warning is displayed if clamping occurs. 
#
##	
updateZenityProgressBar() {
# Set warning color
	if [ -z "$3" ]; then
		local color='\033[1;33m' # Default color is yellow
	else
		local color=$3
	fi

# If progress bar not running : display warning
	if [ "$progress_bar_status" -ne 0 ]; then
		echo "${color}WARNING : the progress bar is down ${NC}"
	else
# Otherwise update progress bar
		if [ ! -z "$2" ]; then # Text updated only if text is not empty 
			echo "# ${2}" >> ${progress_pipe}
		fi
# Clamp progress values between 0 and 100
		if [ "${1}" -lt 0 ]; then
			echo "${color}WARNING : progress value ${1} is clamped to 0 ${NC}"
			local progress=0
		elif [ "${1}" -gt 100 ]; then
			echo "${color}WARNING : progress value ${1} is clamped to 100 ${NC}"
			local progress=100
		else
			local progress=$1			
		fi
		echo "${progress}" >> ${progress_pipe}
	fi
}

##!
# @brief Clean up Zenity progress bar related data, processes and files at the end of execution.
#
# This function :
# - Kills the tail process used to update progress bar
# - Deletes the progress_pipe file used to write updates of progress bar content
# - Deletes the file storing the pid of the tail process
#
##	
cleanupZenityProgressBar() {
	read -r pid < ${tail_pid}
	kill $pid
	rm ${progress_pipe}
	rm ${tail_pid}
}


