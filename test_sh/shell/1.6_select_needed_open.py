import sys
import os
def FindOpen(rootdir,resultpath,needed_list_path,not_needed_list_path):
    lines=[]
    list_needed=[]
    list_not_needed=[]
    list_current_all=[]
    list_current_needed=[]
    list_current_not_needed=[]
    sum=0
    f1 = open(resultpath, 'w')

    with open(needed_list_path, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            string = line
            list_needed.append(string)
    list_needed=list(set(list_needed))
    with open(not_needed_list_path, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            string = line
            list_not_needed.append(string)
    list_not_needed=list(set(list_not_needed))


    with open(rootdir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            string = line
            if (string[-27:]!="(No such file or directory)"):
                             k=-1
                             k_start=0
                             flag=-1
            
                             for l in range(0,len(string)):
                                   if string[l]=='(':
                                         k=l
                                         flag=0
                                         #print(k)
                                         break
                             for l1 in range(0,len(string)):
                                    if ((string[l1].isspace())and(not(string[l1+1].isspace()))):
                                         k_start=l1
                                         #if flag==0:
                                         #print(l1)
                                         break
                             if ( (flag==0) and (string[k_start+1].isalpha()) ):
                                    string_to_be_judged=string[k_start+1:k]
                                    list_current_all.append(string_to_be_judged)
                                    if string_to_be_judged in list_needed:
                                              f1.writelines([string+"\n"])
                                    elif (string_to_be_judged in list_not_needed):
                                                                                    continue
                                    else :  
                                              flag_k1=0
                                              flag_k2=0
                                              flag_k3=0
                                              flag_k4=0
                                              flag_k5=0
                                              for l in range(0,len(string)):
                                                 if (flag_k1==1)and(flag_k2==1)and(flag_k3==1)and(flag_k5==1):
                                                                                                             break
                                                 else:
                                                    if (string[l]=='('):
                                                        flag_k1=1
                                                    elif (string[l]=='"'):
                                                          flag_k2=1
                                                    elif (string[l]=='/'):
                                                                                                flag_k3=1
                                                    #elif (string[l]=='"'):
                                                     #                                                flag_k4=1
                                                    elif (string[l]==')'):
                                                                                                          flag_k5=1
                                                    else:
                                                           continue

                                              if (flag_k1==1)and(flag_k2==1)and(flag_k3==1)and(flag_k5==1):
                                                              flag_file1=1
                                                              flag_file2=1
                                                              k_file=-1
                                                              k_file2=-1
                                                              for l in range(0,len(string)):
                                                                              if (string[l]=='"')and(flag_file1==1):
                                                                                                               k_file=l
                                                                                                               flag_file1=0
                                                                              if (string[l] == '"') and (k_file!=l) and (flag_file2 == 1):
                                                                                                                                k_file2 = l
                                                                                                                                flag_file2 = 0
                                                                              if (flag_file1==0)and(flag_file2==0):
                                                                                                         break
                                                              if ((string[k_file+1:k_file+3]!='./')and(string[k_file+1:k_file+4]!='../')):

                                                                           string_file_test=string[k_file+1:k_file2]
                                                                         
                                                                           if os.path.exists(string_file_test):
                                                                                                              #print(string_to_be_judged+' ')
                                                                                                              list_needed.append(string_to_be_judged)
                                                                                                              list_current_needed.append(string_to_be_judged)
                                                                                                              f1.writelines([string+"\n"])

                                                 
            else:
                continue 
    for each in list_current_all:
      if ((not(each in list_current_needed))and(not(each in list_not_needed))):
                                           list_not_needed.append(each)
                                           list_current_not_needed.append(each)
    f2 = open(needed_list_path, 'a+')
    f3 = open(not_needed_list_path, 'a+')
    list_current_needed=list(set(list_current_needed))
    list_current_not_needed=list(set(list_current_not_needed))

    for each in list_current_not_needed:
                                       f3.writelines([each+"\n"])
    for each in list_current_needed:
                                       f2.writelines([each+"\n"])

   


workdir=sys.argv[1]
startpath=workdir+'/test_sh/txt/1_strace_output.txt'
resultpath=workdir+'/test_sh/txt/2_select_open.txt'
needed_list_path=workdir+'/test_sh/txt/needed_list.txt'
not_needed_list_path=workdir+'/test_sh/txt/not_needed_list.txt'
FindOpen(startpath,resultpath,needed_list_path,not_needed_list_path)
