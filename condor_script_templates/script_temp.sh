#!/bin/bash

set -x

cd H5_maker/
eval `scramv1 runtime -sh`
cmsRun pfnano_mc_2016UL_OpenData.py inputFiles_load=EOS_files_split/QCDPt800_job${2}.txt 
python H5_maker.py -i nano_mc2016post.root -o QCDPt800_job${2}.h5 --sample_type MC 
xrdcp -f QCDPt800_job${2}.h5 ${1} 
