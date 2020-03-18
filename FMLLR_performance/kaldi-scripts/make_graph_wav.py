#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# E-mail: vishwasks32@gmail.com
#
# Script to plot a wave file and save the graph

from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as pyplt
import sys

def make_graph(data,filename):
    pyplt.clf()
    pyplt.plot(data)
    pyplt.savefig(filename)


if __name__=='__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: %s source_file dest_filename' % sys.argv[0])


    data_fs, data = wavfile.read(str(sys.argv[1]))
    filename = str(sys.argv[2])

    make_graph(data, filename)




