import os

#nJobs = 1309
#inputList =  "2016H.txt"
#nJobs = 1236
#inputList =  "2016G.txt"
#nJobs = 500
#inputList =  "QCD_Pt600.txt"
#nJobs = 1087
#inputList =  "file_lists/QCD_Pt300.txt"
#nJobs = 1067
#inputList =  "file_lists/QCD_Pt470.txt"
nJobs = 834
inputList =  "file_lists/QCD_Pt800.txt"

odir = "EOS_files_split/"
label = "QCDPt800_job%i"

fin = open(inputList)

f_list = fin.readlines()

num_lines = len(f_list)
batch_size = (num_lines//nJobs)
remainder = num_lines % nJobs

start = 0
end = 0


for i in range(nJobs):

    start = end
    end = start + batch_size if i < (nJobs-1) else num_lines
    if(i< remainder): end+=1
    #print(start, end)
    f_out = f_list[ start:end ]

    out_file = open(odir + (label %i) + ".txt", "w")
    for line in f_out:
        out_file.write(line)

    out_file.close()


