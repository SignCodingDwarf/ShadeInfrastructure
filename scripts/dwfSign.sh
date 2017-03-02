#!/bin/bash

# file : dwfSign.sh
# author : SignC0dingDw@rf
# version : 1.0
# date : 15 November 2016
# Bash file signature functions

### Functions
##!
# @brief Dwarven stone carving function
# @param 1 : Stone to carve
# @param 2 : Dwarven language
# @return Alive and poor if you're rich, dead and rich otherwise
#
# Bring lots of GOLD or DIE !!!
#
##
DwfSign1_0() {
	if [[ -z "${DWF_MAGIC}" ]]; then
		echo -e "\033[1;33mYou who wish to enter our mines \nShall bear the number of the Dwarves.\033[0m" # This is just because I am a bit absent-minded so I need to get remerbered to define it on a new PC.
		return 666 # The Dwarves shall wreak chaos upon you
	fi
# I am STONE
	if [ ! -z "$1" ] && [ -e $1 ]; then 
		local comment_char=$([[ -z "$2" ]] && echo '#' || echo $2)
		local magic=$(echo "scale=3;w=${DWF_MAGIC}-666/(4*a(1))/${DWF_MAGIC}*${DWF_MAGIC}/7;scale=0;w/1" | bc -l)  		
		local str="${comment_char}"
		local ref=$(echo "scale=3;w=${magic}*4*a(1)-4*a(1);scale=0;w/1" | bc -l)
		for ((i=0; $magic-$i; i++)); do
			str="${comment_char}"
			str+="\0"
			str+=$(echo "scale=3;w=666/${magic}*a(1)-7;scale=0;w/1" | bc -l)
			str+="\0"
			str+=$(echo "scale=3;w=666/(4*a(1))/7+${magic}-${magic}/(7+4*a(1))+(${i}>666/${magic}/${magic}-${magic}*${magic}/7/4/a(1))*(${magic}*${magic}+${magic}+7/4/a(1));scale=0;w/1" | bc -l)
			for((j=1 ; $ref-$j ; j++)); do
				str+="\0"
				str+=$(echo "scale=0;i=(${i}%(${magic}-${magic}/${magic}))*(((${i}-7+666/${magic}/${magic})%(666/${magic}/${magic}+${magic}/7)!=0)+(${j}<666/7/7-7-${magic}/7)+(${j}>666/7/7*${magic}/7+666/${magic}/${magic}+${magic}/7));scale=3;w=(${j}<4*a(1)*${i})*(${i}*${j}==7*${magic}+${magic}/${magic}-7+${magic}-7)*(666/7-a(666)+7*a(666))+(${i}>=(3))*(${i}<(${magic}-7/4*a(1)-a(1)))*((${j}==${magic}-7)+(${j}==${magic}+${magic}+${magic}-7+${magic}/${magic}))*(${magic}*7+666/${magic}-4*a(1))+666/7+${magic}*${magic}*4*a(1)/666+7+${magic}*4*a(1)-i/(i+${magic}/666/${magic})*(666/7+${magic}/7/a(1))+(${i}*${j}==7*(${magic}-7)+(${magic}-7)*7)*(${j}-${i}==7+7-${magic}+7)*(${j}*7-${i}-${magic})+(${j}==7+666/(${magic}*${magic}-${magic}+666/666))*(${i}*${j}>=666/${magic})*(${j}*${i}<666/7/7*7-666/7/7)*(7*7-a(1)+11-a(1)+${i})-(${j}==${magic}-7+${magic})*(${i}<7)*(${i}*${j}>${magic}*7)*(${j}*(7-${magic}))+(${j}-${i}==7)*(${i}+${i}==${j})*(${j}+${i})+((${i}*${j} == ${magic}+7+${magic}+${magic}+7*(${magic}-7))+(${i}*${j}==7+666-7*${magic}*7-7*7))*(${magic}*${magic}-${j}/(4*a(1))+a(${magic}/7))+((${i}*${j}==7*7+${magic})+(${i}*${j}==${magic}*${magic}-7*${i}-${magic}+${i}))*(${j}-${i}==${magic})*(a(1)+${magic}*(${j}-${i})-${magic}+a(1))+((${i}*${i}==${j})*(${j}*${i}==${magic}*7*${magic}-666+${magic}-7-${magic}*${magic})+(${i}/${j}==(${magic}-7+${magic}/${magic})/(${magic}+7)))*(-7+${magic}*${magic}-7)+(${j}==${magic}-7+${magic})*(${i}+${j}==${magic}+${magic})*(${j}+${i}/7)+((${i}==7)+(${j}==7+7))*(${j}-${i}==9)*(${magic}+7+4*a(1)-a(${i}/${magic}))+(${i}*${j}==7*${magic}+7)*(${j}-7==7)*(${magic}*${magic}+7-a(7/${magic}))+(${j}*${i}==7*7+${magic}-7+7*7)*(${j}-${i}==${magic})*(666/7+${magic})+(${j}==${magic}+${magic}-${i})*(${i}==7-666/666)*(${magic}*${magic}+a(${magic}/7));scale=0;w/1" | bc -l) 
			done
			str+="\0"
			str+=$(echo "scale=3;w=666/(4*a(1))/7+${magic}-${magic}/(7+4*a(1))+(${i}>666/${magic}/${magic}-${magic}*${magic}/7/4/a(1))*(${magic}*${magic}+${magic}+7/4/a(1));scale=0;w/1" | bc -l) 
			echo -e $str >> $1
		done
		ref=$(echo "scale=3;w=${magic}+${magic}/(4*a(1))+4*a(1)*666/(${magic}*${magic})/${magic}*${magic}/(7*4*a(1));scale=0;w/1" | bc -l)
		for ((i=0 ; $magic-$i ; i++)); do
			str="${comment_char}"
			str+="\0"
			str+=$(echo "scale=3;w=666/(7*4*a(1))+${magic}-${magic}*${magic}*7/666;scale=0;w/1" | bc -l)
			for ((j=1 ; $ref-$j ; j++)); do
				str+=${str: -4}
			done
			str+="\\"
			str+=$(echo "scale=3;w=${magic}*${magic}/(7*4*a(1))-666/(${magic}*${magic});scale=0;w/1" | bc -l)
			str+=$(echo "scale=3;w=${magic}*${magic}+7*4*a(1)*7+7*4*a(1)-${magic}/${magic}-${magic}*${magic};scale=0;w/1" | bc -l)
			str+="\0"
			str+=$(echo "scale=3;w=${magic}*4*a(1)+7*a(1)+${i}/${magic}/${magic}/${magic}/7*${magic}^3*7/${magic}*(121-4*a(1)-4*a(1));scale=0;w/1" | bc -l)
			str+=${str: $(echo "scale=3;w=-${magic}/7*4*a(1)-${i}/${magic}/${magic}/${magic}/7*${magic}^3*7/${magic};scale=0;w/1" | bc -l)}
			str+="\0"
			str+=$(echo "scale=3;w=(${magic}-4*a(1))*7*4*a(1)+7*4*a(1)/${magic};scale=0;w/1" | bc -l) 
			echo -e $str >> $1
		done	
		return 0 
	else
		echo -e "\033[1;33mIf you're bold \nGimmie your gold.\033[0m"
		return 1 # The dwarves want gold to carve stones
	fi
}
