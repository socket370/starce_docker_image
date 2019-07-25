#!/bin/bash
for line in `cat ../txt/11_ldd_executable_list.txt`;
do
if [ "${line:0:1}" == "/" ]
then
echo "${line}" >> ../txt/12_ldd_executable_list_start_with_gang.txt;
fi
done
