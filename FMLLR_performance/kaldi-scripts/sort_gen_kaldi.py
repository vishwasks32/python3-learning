#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to sort utt2spk file for kaldi
# Note: generate seperate files for train and test folders
# Usage : python3 gen_utt2spk_kaldi.py
# Input : path to audio data folder train, test
# Output : utt2spk file in current directory
#          once you generate it cut paste o required directories, else it will be replaced the second time

import os
import sys

if len(sys.argv) < 2:
    sys.exit('Usage: %s data_directory'%sys.argv[0])

filename = str(sys.argv[1])
newfilename = filename +'_new'
try:
    f_name = open(filename, 'r')
    dat_lst = f_name.readlines()
    f_name.close()
    f_name = open(newfilename, 'w+')
    for x in sorted(dat_lst):
        f_name.write(x)
    f_name.close()

except IOError:
    print("Specified file does not exist!!")
