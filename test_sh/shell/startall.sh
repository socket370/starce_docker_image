#!/bin/bash

workdir=$1
workdir2=$2
var1=$(python3 --version)

if [ "${var1:0:6}" == "Python" ] || [ "${var1:0:6}" == "python" ]
then
#python3 ./1_select_open.py $workdir
python3 ./1.6_select_needed_open.py $workdir
python3 ./2_clear_NoSuchFile.py $workdir
python3 ./4_select_between.py $workdir
python3 ./5_get_Summary_output_partly.py $workdir
python3 ./5.1_Special_treatment.py $workdir $workdir2
python3 ./6_get_Summary_output_last.py $workdir
python3 ./7_get_Summary_output_without_proc.py $workdir
else
#python ./1_select_open.py $workdir
python ./1.6_select_needed_open.py $workdir
python ./2_clear_NoSuchFile.py $workdir
python ./4_select_between.py $workdir
python ./5_get_Summary_output_partly.py $workdir
python ./5.1_Special_treatment.py $workdir $workdir2
python ./6_get_Summary_output_last.py $workdir
python ./7_get_Summary_output_without_proc.py $workdir
fi
./8_get_executable_list.sh
./9_run_ldd_executable.sh
./10_get_ldd_executable_list.sh
./11_get_ldd_executable_list_start_with_gang.sh
./12_get_first_so_summary_list_partly.sh
./13_file_so_command.sh
./14_get_first_so_summary_list_last.sh
./15_get_all_so_summary_list_without_link_uniq.sh
./16_get_all_so_summary_list_last.sh
