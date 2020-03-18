#!/usr/bin/env python3
# Author : Vishwas K Singh
# Email: vishwasks32@gmail.com
# Script to add noise using FaNT 

import os

# We have to set the parameters here
filter_tool ='/media/data/workspace-applications/fant-tool/filter_add_noise '
in_list_file =' -i in.list'
out_list_file =' -o out.list'
noise_file =' -n /media/data/workspace-applications/kaldi_datas/noise_dir/factory.raw'
filter_type =' -f g712'
desired_snr = ' -s 10'
log_file =' -e /media/data/workspace-applications/fant-tool/fant15_factory.log'

# First we'll create empty files for output
# Read the out_list_file
f_name = open(out_list_file.split(' ')[2])
dat = f_name.read().split('\n')
f_name.close()
for i in range(len(dat)-1):
    #print("Creating empty file %s"%dat[i])
    os.system('touch '+dat[i])

filter_cmd = filter_tool + in_list_file + out_list_file + filter_type + noise_file + desired_snr + log_file
os.system(filter_cmd)
print("Noise addition successful")

