#!/bin/bash
for line in `cat ../txt/10_ldd_executable.txt`; do echo "${line}" >> ../txt/11_ldd_executable_list.txt; done
