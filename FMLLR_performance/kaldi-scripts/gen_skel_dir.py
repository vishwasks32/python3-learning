#!/usr/bin/env python3
#
# Autor: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to generate the skeleton directories

import os
import sys


if len(sys.argv) <2:
    sys.exit("Usage: %s base_path"%sys.argv[0])

base_path = sys.argv[1]
os.system("mkdir -p "+base_path+"/digits_audio/test/vish")
os.system("mkdir -p "+base_path+"/digits_audio/train/anil")
os.system("mkdir -p "+base_path+"/digits_audio/train/basavaraj")
os.system("mkdir -p "+base_path+"/digits_audio/train/rakesh")
os.system("mkdir -p "+base_path+"/digits_audio/train/gopi")
os.system("mkdir -p "+base_path+"/digits_audio/train/rajeev")
os.system("mkdir -p "+base_path+"/digits_audio/train/santosh")
print("Skeleton created")
