#!/usr/bin/env python3
# Author : Vishwas K Singh
# Email: vishwasks32@gmail.com
# Script to add noise to wavefiles

from scipy.io import wavfile
import numpy as np
import os
import math

# Make sure you set the right path there

try:
    #dir_name = str(input("Enter the name of audio data directory: "))
    # Read the file path
    dir_name = '/media/data/workspace-applications/kaldi-trunk/egs/digits1/digits_audio' 
    dir_list = os.walk(dir_name)
    for path, subdirs, files in dir_list:
        for filename in files:
            f = os.path.join(path, filename)
            fs, data = wavfile.read(f)
            
            signal_power = sum(abs(data)**2)/len(data)
            sgnal_power_db = 10 * math.log10(signal_power)
            
            print(f,fs)
            print('Signal Power', sgnal_power_db)

            
except IOError:
    print("File not found")
