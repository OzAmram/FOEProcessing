#!/bin/bash

set -x

cd FOEProcessing/
eval `scramv1 runtime -sh`
cmsRun pfnano_data_2016UL_OpenData.py inputFiles_load=EOS_files_split/JetHT_2016G_job${2}.txt 
python H5_maker_FOE.py -i nano_data2016.root -o JetHT_2016G_job${2}.h5 -j Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt 
xrdcp -f JetHT_2016G_job${2}.h5 ${1} 
