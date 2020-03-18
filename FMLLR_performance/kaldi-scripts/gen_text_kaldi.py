#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to generate test file for kaldi
# Note: generate seperate files for train and test folders
# Usage : python3 gen_text_kaldi.py
# Input : path to audio data folder train, test
# Output : text file in current directory
#          once you generate it cut paste o required directories, else it will be replaced the second time

import os
import sys

# First define the words common like for numbers 1:one, 2:two, ... so on.
# Since I have done for kannada, I generate transliterated text
# 1:o.ndu 2:eraDu 3:mUru 4:naalku 5:aidu 6:aaru 7:ELu 8:e.nTu 9:o.nbhattu 0:sonne
num_dict = {'0':'sonne', '1':'ondu', '2':'eradu', '3':'mooru', '4':'naalku', '5':'aidhu', '6':'aaru',\
            '7':'yelu', '8':'entu', '9':'ombattu'}
if len(sys.argv) < 2:
        sys.exit('Usage: %s database-name' % sys.argv[0])

f_name = open('text', 'w+')
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

            spken_nums = end_str_wo_ext.split('_')
            num_wrd_lst = []
            for num in spken_nums:
                num_wrd_lst.append(num_dict[num])
            num_str = ' '.join(num_wrd_lst)
            final_str = start_str+'_'+end_str_wo_ext+ ' '+ num_str
            f_name.write(final_str+'\n')



    f_name.close()
except IOError:
    print("Specified folder does not exist!!")
