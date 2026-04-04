import os

#nJobs = 1309
#inputList =  "2016H.txt"
nJobs = 3165
inputList =  "file_lists/CMS_mc_RunIISummer20UL16MiniAODv2_TTToSemiLeptonic.txt"
label = "CMS_mc_RunIISummer20UL16MiniAODv2_TTToSemiLeptonic_job%i"

odir = "EOS_files_split/"

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


