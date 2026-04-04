#!/bin/bash

set -x

cd FOEProcessing/
eval `scramv1 runtime -sh`
cmsRun pfnano_mc_2016UL_OpenData.py inputFiles_load=EOS_files_split/CMS_mc_RunIISummer20UL16MiniAODv2_TTToSemiLeptonic_job${2}.txt 
python H5_maker_FOE.py -i nano_mc2016post.root -o CMS_mc_RunIISummer20UL16MiniAODv2_TTToSemiLeptonic_job${2}.h5 --sample_type MC 
xrdcp -f CMS_mc_RunIISummer20UL16MiniAODv2_TTToSemiLeptonic_job${2}.h5 ${1} 
