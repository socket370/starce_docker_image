#!/bin/bash
cd ../txt
for line in `cat 16.6_all_so_summary_list_without_link_uniq.txt`;
do
	 echo $line >> 8_Summary_output_without_proc.txt
done
sort 8_Summary_output_without_proc.txt | uniq > 17_all_so_summary_list_last.txt
cd ../shell
