#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to generate file lists for FaNT 

import os
import sys

in_list = open('in.list', 'w+')
out_list = open('out.list','w+')

if len(sys.argv) < 3:
    sys.exit('Usage: %s src_path dest_path' % sys.argv[0])
print("****Program Started****")
print("-----------------------")
print("In List Path: %s"%sys.argv[1])
print("Out List Path: %s"%sys.argv[2])
try:
    dir_name = str(sys.argv[1])
    new_dir = str(sys.argv[2])
    dir_list = os.walk(dir_name)
    for path, subdirs, files in dir_list:
        for filename in files:
            f = os.path.join(path, filename)

            pth_lst = f.split('/')
            new_f = new_dir+'/'+pth_lst[len(pth_lst)-4]+'/'+pth_lst[len(pth_lst)-3]+'/'+pth_lst[len(pth_lst)-2]+'/'+pth_lst[len(pth_lst)-1]

            in_list.write(f+'\n')
            out_list.write(new_f+'\n')



    in_list.close()
    out_list.close()
    print("List Creation Successful")

except IOError:
    print("Specified folder does not exist!!")
