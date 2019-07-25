#import re
import sys

def FindOpen(rootdir,resultpath,workdir):
    lines=[]
    sum=0
    f1 = open(resultpath, 'w')

    currentdir=workdir
    with open(rootdir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            string = line
            l1=0
            l2=0
            if string[0:5]=='chdir':
              
               for l in range(0,len(string)):
                 if string[l:7]=='chdir("':
                      l1=l
                 if string[l:2]=='")':
                      l2=l
               currentdir=string[l1+7:l2-l1-6]
            else:
            	if string[0:2]=='./':
                  lines.append(currentdir+string[1:])
            	if string[0:1]!=".":
                  lines.append(currentdir+'/'+string)
            	if string[0:3]=='../':
                   k=3
                   while string[k:k+3]=='../':
                       k=k+3
                   num1=k/3
                   lines.append(changeCurrentDir(currentdir,num1)+string[k-1:])
                  
                  
    lines = list(set(lines))

    for each in lines:
        sum=sum+1
        f1.writelines([each+"\n"])
    #print(sum)
def changeCurrentDir(currentdir,num1):
     l=len(currentdir)-1
     k=0
     while (k<num1)and(l>0):
         if currentdir[l]=='/':
            k=k+1
         l=l-1
     return currentdir[0:l+1]

#workdir='/home/unix-lc/Desktop/auto_collect2/test4_sh'
#Porgramdir='/home/unix-lc/klee-float'
#Porgramdir2='/home/unix-lc/klee-float/cmake-build-debug/bin'
#Porgramdir3='/home/unix-lc'
#pattern = re.compile('workdir=(.*)')
#input = open('../../test_start.sh','r')
#L = input.readlines()
#workdir=pattern.findall(L[2])[0]
workdir=sys.argv[1]
startpath=workdir+'/test_sh/txt/5.1_Special_treatment.txt'
resultpath=workdir+'/test_sh/txt/5.2_Special_treatment_output.txt'
#pattern = re.compile('ProgramHome=(.*)')
#input = open('../../test_start.sh','r')
#L = input.readlines()
#workdir2=pattern.findall(L[1])[0]
workdir2=sys.argv[2]

FindOpen(startpath,resultpath,workdir2)
