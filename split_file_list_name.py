import os
from parse import parse

#nJobs = 1309
#inputList =  "2016H.txt"
#nJobs = 1236
#inputList =  "2016G.txt"
#nJobs = 500
#inputList =  "QCD_Pt600.txt"
inputList =  "file_lists/Zprime_files_PSweight.txt"

odir = "EOS_files_split/"
label = "Zprime_PSweight_job%i"

fin = open(inputList)

f_list = fin.readlines()

num_lines = len(f_list)

batch_num = 0
m_cur = 700


flist = []
for f in f_list:
    if("root" not in f): continue
    m_str = "_M%i_W%i_" % (m_cur, m_cur // 100)
    print(f)
    if(m_str in f):
        flist.append(f)
    else:
        #write out this batch
        out_file = open(odir + (label % batch_num) + ".txt", "w")
        for line in flist:
            out_file.write(line)

        out_file.close()

        flist =[]
        batch_num +=1

        #find new M
        while(m_cur < 5000):
            m_cur += 100
            m_str_new = "_M%i_W%i_" % (m_cur, m_cur // 100)
            if(m_str_new in f):
                print("new %i, batch %i" % (m_cur, batch_num))
                break


