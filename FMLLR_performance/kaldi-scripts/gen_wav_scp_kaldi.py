#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to generate wav.scp file for kaldi
# Note: generate seperate files for train and test folders
# Usage : python3 gen_wav_scp_kaldi.py
# Input : path to audio data folder train, test
# Output : wav.scp file in current directory
#          once you generate it cut paste o required directories, else it will be replaced the second time

import os
import sys

f_name = open('wav.scp', 'w+')
if len(sys.argv) < 2:
    sys.exit('Usage: %s data_directory' % sys.argv[0])

try:
    dir_name = str(sys.argv[1])
    dir_list = os.walk(dir_name)
    for path, subdirs, files in dir_list:
        for filename in files:
            f = os.path.join(path, filename)
            spkr_name = f.split('/')
            start_str = spkr_name[len(spkr_name)-2]
            end_str_with_ext = spkr_name[len(spkr_name)-1]
            end_str_wo_ext = end_str_with_ext[:len(end_str_with_ext)-4]
            final_str = start_str+'_'+end_str_wo_ext+ ' '+f
            f_name.write(final_str+'\n')



    f_name.close()
except IOError:
    print("Specified folder does not exist!!")
