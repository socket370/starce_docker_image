#!/bin/bash
cat ../txt/9_executable_list.txt | while read line
do
	echo $(ldd $line) >> ../txt/10_ldd_executable.txt
done		  
