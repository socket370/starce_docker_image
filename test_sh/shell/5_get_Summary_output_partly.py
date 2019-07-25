#import re
import sys

def FindOpen(rootdir,resultpath):
    lines=[]
    sum=0
    f1 = open(resultpath, 'w')

    with open(rootdir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            string = line

            if string[0:1]=='/':
             lines.append(string)

    for each in lines:
       sum=sum+1
       f1.writelines([each+"\n"])
    #print(sum)

def FindOpen2(rootdir,resultpath2):
    lines=[]
    sum=0
    f1 = open(resultpath2, 'w')

    with open(rootdir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            string = line
            if string[0:1]!="/":
             lines.append(string)
            if string[0:5]=='chdir':
             lines.append(string)
            if string[0:2]=='./':
             lines.append(string)
            if string[0:3]=='../':
             lines.append(string)

    for each in lines:
       sum=sum+1
       f1.writelines([each+"\n"])
    #print(sum)

#workdir='/home/unix-lc/Desktop/auto_collect2/test4_sh'
#pattern = re.compile('workdir=(.*)')
#input = open('../../test_start.sh','r')
#L = input.readlines()
#workdir=pattern.findall(L[2])[0]
workdir=sys.argv[1]
startpath=workdir+'/test_sh/txt/5_select_between.txt'
resultpath=workdir+'/test_sh/txt/6_Summary_output_partly.txt'
resultpath2=workdir+'/test_sh/txt/5.1_Special_treatment.txt'
FindOpen(startpath,resultpath)
FindOpen2(startpath,resultpath2)
