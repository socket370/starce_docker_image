#!/bin/bash
cd ../txt
cat 13.5_first_so_summary_list_partly.txt | while read line
do
	var1=$line
	var2=$(file $line)
	k=${#var1}
	if [ "${var2:k+2:28}" == "ELF 64-bit LSB shared object" ] || [ "${var2:k+2:16}" == "symbolic link to"  ]
	then
		        echo $var1 >> 14_file_so_command.txt
		fi
	done
cd ../shell

