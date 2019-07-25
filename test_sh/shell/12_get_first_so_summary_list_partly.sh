#!/bin/bash
for line in `cat ../txt/8_Summary_output_without_proc.txt`;
do
var1=".so"
result=$(echo $line | grep "$var1")
if [[ "$result" != "" ]]
then
echo "${line}" >> ../txt/13_so_list.txt;
fi
done
for line in `cat ../txt/12_ldd_executable_list_start_with_gang.txt`;
do
echo "${line}" >> ../txt/13_so_list.txt;
done
sort ../txt/13_so_list.txt | uniq > ../txt/13.5_first_so_summary_list_partly.txt
