#!/bin/bash
cd ../txt
cat 14_file_so_command.txt | while read line
do
var1=$line
fvar1=${var1%/*}
var2=$(ls -l $var1)
var3=${var2##*[  ]}
echo $line >> 15_link_so_and_so_list.txt
if [ "$var3" != "$var1" ]
then
     if [ "${var3:0:1}" != "/" ]
	then		
          echo ${fvar1}/${var3} >> 15_link_so_and_so_list.txt
        else 
	  echo $var3 >> 15_link_so_and_so_list.txt
     fi
fi
done
sort 15_link_so_and_so_list.txt | uniq > 15.5_first_so_summary_list_last.txt
cd ../shell
