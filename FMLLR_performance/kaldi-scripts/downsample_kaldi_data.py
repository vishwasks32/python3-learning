#!/usr/bin/env python3
#
# Autnor: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to downsample the wavefiles
# Depends On : downsample.py 

import os

# We need the source directory and destination directory
#
src_pth = "/media/data1/workspace-applications/kaldi-trunk/egs/digits2/digits_audio"
dst_pth = "/media/data/workspace-applications/dwnsmpled_data/"
down_smple_pth = "/media/data/workspace-applications/SSRC-master/ssrc"
try:
    dir_name = src_pth
    dir_list = os.walk(dir_name)
    for path, sub_dirs, files in dir_list:
        for filename in files:
            #print(path)
            pth_fil = path.split('/')
            #print(dst_pth+pth_fil[7]+'/'+pth_fil[8]+'/'+pth_fil[9])
            new_path = dst_pth+pth_fil[7]+'/'+pth_fil[8]+'/'+pth_fil[9]
            if not os.path.exists(new_path):
                print("Path does not exist, Creating path")
                os.makedirs(new_path)
            else:
                print("Path exists")

            f = os.path.join(path, filename)
            print("Source file: %s"%f)
            fil_nme = f.split('/')
            nw_file = dst_pth+fil_nme[7]+'/'+fil_nme[8]+'/'+fil_nme[9]+'/'+fil_nme[10]
            print("Destination file: %s"%dst_pth+fil_nme[8]+'/'+fil_nme[9]+'/'+fil_nme[10])
            
            # We will downsample command here 
            dwn_smple_cmd = down_smple_pth+' --rate 8000 '+ f + ' ' + nw_file
            print(dwn_smple_cmd)
            sucess_flg = os.system(dwn_smple_cmd)
            if sucess_flg != 0:
                print("File Cannot be converted")
            else:
                print("File Conversion successful")



except IOError:
    print("File not found!")
