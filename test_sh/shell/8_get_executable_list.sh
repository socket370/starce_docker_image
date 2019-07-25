#!/bin/bash
cat ../txt/8_Summary_output_without_proc.txt | while read line
do
var1=$line	
var2=$(file $line)
k=${#var1}
if [ "${var2:k+2:25}" == "ELF 64-bit LSB executable" ] || [ "${var2:k+2:28}" == "ELF 64-bit LSB shared object" ]
then
	echo $var1 >> ../txt/9_executable_list.txt
fi
done		  
