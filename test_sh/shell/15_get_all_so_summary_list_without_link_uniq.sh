#!/bin/bash
cd ../txt
k=0
for line in `cat 15.5_first_so_summary_list_last.txt`;
do
 var[k]=$line
 let k=k+1 
done



k1=0
while [ "${var[k1]}" != "" ]
do

	true > 16a_ldd_so_parta.txt
        true > 16b_ldd_so_partb.txt
	true > 16c_ldd_so_partc.txt
	echo $(ldd ${var[k1]}) > 16a_ldd_so_parta.txt
	for line in `cat 16a_ldd_so_parta.txt`; do echo "${line}" >> 16b_ldd_so_partb.txt; done
	for line in `cat 16b_ldd_so_partb.txt`;
	do
		if [ "${line:0:1}" == "/"  ]
		then
			echo "${line}" >> 16c_ldd_so_partc.txt;
		fi
	done
	for line in `cat 16c_ldd_so_partc.txt`;
	do
	    flag=0	
            for((i=0;i<k;i++))
	    do
              if [ "${var[i]}" == "$line" ]
	      then
	        flag=1
		break
	      fi 
	    done
	    if [ "$flag" == "0" ] 
	    then
		    var[k]=$line
		    let k++
	    fi
	done
	let k1++
done
for((i=0;i<k;i++))
do
	echo ${var[i]} >> 16_all_so_summary_list_partly.txt
done
cat 16_all_so_summary_list_partly.txt | while read line
do
	var1=$line
	fvar1=${var1%/*}
	var2=$(ls -l $var1)
	var3=${var2##*[   ]}
	echo $line >> 16.5_all_so_summary_list_without_link.txt
	if [ "$var3" != "$var1"  ]
	then
		     if [ "${var3:0:1}" != "/"  ]
			             then
					               echo ${fvar1}/${var3} >> 16.5_all_so_summary_list_without_link.txt
						               else
								                 echo $var3 >> 16.5_all_so_summary_list_without_link.txt
										      fi
									      fi
								      done
								      sort 16.5_all_so_summary_list_without_link.txt | uniq > 16.6_all_so_summary_list_without_link_uniq.txt
cd ../shell

