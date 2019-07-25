#import re
import sys

def FindOpen(rootdir,resultpath):
    lines=[]
    f1 = open(resultpath, 'w')
    sum=0
    with open(rootdir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            string = line
            if (string[0:4]!="/dev") and (string[0:4]!="/etc") and (string[0:5]!="/proc") and (string[0:4]!="/sys"):
                lines.append(string)

    lines.sort()
    for each in lines:
        sum = sum + 1
        f1.writelines([each + "\n"])
    #print(sum)



#workdir='/home/unix-lc/Desktop/auto_collect2/test4_sh'
#pattern = re.compile('workdir=(.*)')
#input = open('../../test_start.sh','r')
#L = input.readlines()
#workdir=pattern.findall(L[2])[0]
workdir=sys.argv[1]
startpath=workdir+'/test_sh/txt/7_Summary_output_last.txt'
resultpath=workdir+'/test_sh/txt/8_Summary_output_without_proc.txt'
FindOpen(startpath,resultpath)
