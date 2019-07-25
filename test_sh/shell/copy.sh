#!/bin/bash

workdir=$1
for line in $(cat ../txt/17_all_so_summary_list_last.txt)
do
 cp --parents  $line $workdir
done
