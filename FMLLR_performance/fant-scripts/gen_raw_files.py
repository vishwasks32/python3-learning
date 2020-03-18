#!/usr/bin/env python3
# Author : Vishwas K Singh
# Email: vishwasks32@gmail.com
# Script to generate raw files from wavefiles

#It's assumed that skeleton dir is executed earlier 

from scipy.io import wavfile
import numpy as np
import os
import sys

if len(sys.argv) < 3:
    sys.exit('Usage: %s src_path dest_path'%sys.argv[0])

try:
    # Read the src path
    dir_name = str(sys.argv[1]) 
   
   # read dest path
    new_dir = str(sys.argv[2])

    dir_list = os.walk(dir_name)
    for path, subdirs, files in dir_list:
        for filename in files:
            f = os.path.join(path, filename)
            fs, data = wavfile.read(f)
            # Before write get new filename
            pth_list = f.split('/')
            file_str = pth_list[len(pth_list)-1].replace(".wav",".raw")
            new_f = new_dir+'/'+pth_list[len(pth_list)-3]+'/'+pth_list[len(pth_list)-2]+'/'+file_str #pth_list[len(pth_list)-1]
            print("Writing to: %s"%new_f)
            data.tofile(new_f)
            
except IOError:
    print("File not found")
