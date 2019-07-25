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
            #print(string)
            k=-1
            k2=-1
            flag1=1
            flag2=1
            flag3=0
            for l in range(0,len(string)):
              if (string[l:l+5]=="chdir"):
                  lines.append(string[l:])
                  flag1=0
                  flag2=0
                  flag3=1
              else:
                if (string[l]=='"')and(flag1==1):
                    k=l
                    flag1=0
                if (string[l] == '"') and (k!=l) and (flag2 == 1):
                    k2 = l
                    flag2 = 0

                if (flag1==0)and(flag2==0):
                    break
            #print(k)
            #print(k,k2)
            if (flag3==0):
             lines.append(string[k+1:k2])

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
startpath=workdir+'/test_sh/txt/3_clear_NoSuchFile.txt'
resultpath=workdir+'/test_sh/txt/5_select_between.txt'
FindOpen(startpath,resultpath)
