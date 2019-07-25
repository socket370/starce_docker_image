#!/bin/bash
ProgramHome='/home/wk/Desktop/teytest'
workscript='program_shell.sh'
workshell='/bin/bash'

workdir=`pwd`

collectdir="$workdir/test_collect"


./clear.sh
cd $ProgramHome
echo program running...
strace -e trace=all -f -F -o $workdir/test_sh/txt/1_strace_output.txt $workshell $ProgramHome/$workscript
echo collect dir list...
cd $workdir/test_sh/shell
$workdir/test_sh/shell/startall.sh $workdir $ProgramHome

echo copy waiting...


mkdir -p $collectdir
$workdir/test_sh/shell/copy.sh $collectdir

## Special Command for Wang Huaijin task, need only when python is executed.
#cp $workdir/ascii.py $workdir/test_collect/usr/lib/python3.5/encodings/

echo Collect Complete!!

# generate docker file

dockerfilename=$collectdir/dockerfile

echo 'From scratch' > $dockerfilename
echo 'COPY . /' >> $dockerfilename
echo "WORKDIR $ProgramHome" >> $dockerfilename
echo "ENV PATH $PATH" >> $dockerfilename
echo "ENV LD_LIBRARY_PATH=/usr/local/lib/x86_64-linux-gnu" >> $dockerfilename
echo "CMD [\"${workshell//' '/'","'}\",\"$ProgramHome/$workscript\"]" >> $dockerfilename


