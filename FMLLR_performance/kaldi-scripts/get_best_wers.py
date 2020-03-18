#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to get and arrange best WER from files of experiments
# in kaldi to a file

import os
import time
import matplotlib.pyplot as plt

# Set the base kaldi experiment path
base_pth = "/media/data1/workspace-applications/kaldi-trunk/egs/"

# Set the experiment names with absolute paths
base_name = "digits"
exp_names = []
for i in range(1,22):
    exp_names.append(base_pth+base_name+str(i)+"/")


# We will have two cases mono and tri1 and its present in
exp_path_mono = "exp/mono/decode/scoring_kaldi/best_wer"
exp_path_tri1 = "exp/tri1/decode/scoring_kaldi/best_wer"

# We will get the best noise type, noise value, wer
# get noise type and noise value in README.txt in experiment path
# We dont know where in readme.txt hence we will compare
avbl_ntypes = ["clean","white","babble","factory","traffic","train"]
avbl_nvals = ["0db","3db","5db","10db","15db"]

file_nme = "kaldi_fin_results.txt"
print (time.strftime("%d/%m/%Y"))
hndle = open(file_nme, 'w+')
hndle.write("Date: "+time.strftime("%d/%m/%Y")+"\n")
und_lne = str("-"*70)
hndle.write(und_lne+"\n")
hndle.write("Noise_Type|SNR_Value|Mono_Training|Tri_Trainingi|Experiment_Name"+'\n')
hndle.write(und_lne+"\n")

babble_nse_mono = []
babble_nse_tri1 = []
babble_nse_nvals = []

white_nse_mono = []
white_nse_tri1 = []
white_nse_nvals = []

factory_nse_mono = []
factory_nse_tri1 = []
factory_nse_nvals = []

traffic_nse_mono = []
traffic_nse_tri1 = []
traffic_nse_nvals = []

train_nse_mono = []
train_nse_tri1 = []
train_nse_nvals = []

babble_dict = {}
traffic_dict = {}
train_dict ={}
white_dict={}
factory_dict={}

babble1_dict = {}
traffic1_dict = {}
train1_dict ={}
white1_dict={}
factory1_dict={}

for item in exp_names:

    # Read the readme file
    f_readme = item+"README.txt"
    f_hdle = open(f_readme)
    readme_rd = f_hdle.read().split(" ")
    ntype = [i for i in avbl_ntypes if i in readme_rd]
    #print(ntype[0])
    nval = [j for j in avbl_nvals if j in readme_rd]
    #print(nval[0])
    f_hdle.close()
    f_best_wer_mono = open(item + exp_path_mono)
    mono_wer = f_best_wer_mono.read().split(" ")[1]
    #print(mono_wer)
    f_best_wer_mono.close()
    f_best_wer_tri1 = open(item+ exp_path_tri1)
    tri1_wer = f_best_wer_tri1.read().split(" ")[1]
    #print(tri1_wer)
    f_best_wer_tri1.close()
    exp = item.split('/')[len(item.split('/'))-2]

    print(ntype[0]+'|'+nval[0]+'|'+mono_wer+'|'+tri1_wer+'|'+exp)
    hndle.write(ntype[0]+'|'+nval[0]+'|'+mono_wer+'|'+tri1_wer+'|'+exp+'\n')
    
hndle.close()


# for easy plotting based on the noise type we will sort them
# for every noise type we will plot noise val vs WER and save the figures
f_hd = open(file_nme)
f_rdat = f_hd.read().split('\n')
for stdat in f_rdat:
    if stdat.startswith('babble'):
        dat_lst = stdat.split('|')
        babble_dict[int(dat_lst[1].replace("db",""))] = float(dat_lst[2])
        babble1_dict[int(dat_lst[1].replace("db",""))] = float(dat_lst[3])
    elif stdat.startswith('white'):
        dat_lst = stdat.split('|')
        white_dict[int(dat_lst[1].replace("db",""))] = float(dat_lst[2])
        white1_dict[int(dat_lst[1].replace("db",""))] = float(dat_lst[3])
    elif stdat.startswith('factory'):
        dat_lst = stdat.split('|')
        factory_dict[int(dat_lst[1].replace("db",""))] = float(dat_lst[2])
        factory1_dict[int(dat_lst[1].replace("db",""))] = float(dat_lst[3])
    elif stdat.startswith('traffic'):
        dat_lst = stdat.split('|')
        traffic_dict[int(dat_lst[1].replace("db",""))] = float(dat_lst[2])
        traffic1_dict[int(dat_lst[1].replace("db",""))] = float(dat_lst[3])
    elif stdat.startswith('train'):
        dat_lst = stdat.split('|')
        train_dict[int(dat_lst[1].replace("db",""))] =  float(dat_lst[2])
        train1_dict[int(dat_lst[1].replace("db",""))] =  float(dat_lst[3])

f_hd.close()

print(babble_dict)
print(white_dict)
print(traffic_dict)
print(train_dict)
print(factory_dict)
print(babble1_dict)
print(white1_dict)
print(traffic1_dict)
print(train1_dict)
print(factory1_dict)
# We will sort according to the list
nvals = [3,5,10,15]
for itm in nvals:
    babble_nse_nvals.append(itm)
    babble_nse_mono.append(babble_dict[itm])
    white_nse_nvals.append(itm)
    white_nse_mono.append(white_dict[itm])
    factory_nse_nvals.append(itm)
    factory_nse_mono.append(factory_dict[itm])
    traffic_nse_nvals.append(itm)
    traffic_nse_mono.append(traffic_dict[itm])
    train_nse_nvals.append(itm)
    train_nse_mono.append(train_dict[itm])
    
    babble_nse_tri1.append(babble1_dict[itm])
    white_nse_tri1.append(white1_dict[itm])
    factory_nse_tri1.append(factory1_dict[itm])
    traffic_nse_tri1.append(traffic1_dict[itm])
    train_nse_tri1.append(train1_dict[itm])

# Plot the noise and save figure
# babble noise
plt.figure(1)
#plt.xticks(nvals)
plt.axis([0,20,0,100])
plt.plot(babble_nse_nvals,babble_nse_mono,'ro')
plt.plot(babble_nse_nvals,babble_nse_mono)
plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Analysis of Babble Noise at Various SNRs")
plt.savefig("Babble_nse_ana.png")
# White noise
plt.figure(2)
#plt.xticks(nvals)
plt.axis([0,20,0,100])
plt.plot(white_nse_nvals,white_nse_mono,'ro')
plt.plot(white_nse_nvals,white_nse_mono)
plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Analysis of White Noise at Various SNRs")
plt.savefig("White_nse_ana.png")
# Factory noise
plt.figure(3)
#plt.xticks(nvals)
plt.axis([0,20,0,100])
plt.plot(factory_nse_nvals,factory_nse_mono,'ro')
plt.plot(factory_nse_nvals,factory_nse_mono)
plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Analysis of Factory Noise at Various SNRs")
plt.savefig("Factory_nse_ana.png")
# Traffic noise
plt.figure(4)
#plt.xticks(nvals)
plt.axis([0,20,0,100])
plt.plot(traffic_nse_nvals,traffic_nse_mono,'ro')
plt.plot(traffic_nse_nvals,traffic_nse_mono)
plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Analysis of Traffic Noise at Various SNRs")
plt.savefig("Traffic_nse_ana.png")
# Train noise
plt.figure(5)
#plt.xticks(nvals)
plt.axis([0,20,0,100])
plt.plot(train_nse_nvals,train_nse_mono,'ro')
plt.plot(train_nse_nvals,train_nse_mono)
plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Analysis of Train Noise at Various SNRs")
plt.savefig("Train_nse_ana.png")
# Generate a combination plot
plt.figure(6)
plt.axis([0,20,0,100])
#plt.plot(babble_nse_nvals,babble_nse_mono,'ro')
plt.plot(babble_nse_nvals,babble_nse_mono)
#plt.plot(white_nse_nvals,white_nse_mono,'ro')
plt.plot(white_nse_nvals,white_nse_mono)
#plt.plot(factory_nse_nvals,factory_nse_mono,'ro')
plt.plot(factory_nse_nvals,factory_nse_mono)
#plt.plot(traffic_nse_nvals,traffic_nse_mono,'ro')
plt.plot(traffic_nse_nvals,traffic_nse_mono)
#plt.plot(train_nse_nvals,train_nse_mono,'ro')
plt.plot(train_nse_nvals,train_nse_mono)

plt.legend(['Babble Noise','White Noise','Factory Noise','Traffic Noise','Train Noise'])

plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Comparisions of Noises at Various SNRs")
plt.savefig("Comp_nse_mono_ana.png")

# Plot the noise and save figure
# babble noise
plt.figure(7)
#plt.xticks(nvals)
plt.axis([0,20,0,100])
plt.plot(babble_nse_nvals,babble_nse_tri1,'ro')
plt.plot(babble_nse_nvals,babble_nse_tri1)
plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Analysis of Babble Noise at Various SNRs")
plt.savefig("Babble_nse_tri1_ana.png")
# White noise
plt.figure(8)
#plt.xticks(nvals)
plt.axis([0,20,0,100])
plt.plot(white_nse_nvals,white_nse_tri1,'ro')
plt.plot(white_nse_nvals,white_nse_tri1)
plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Analysis of White Noise at Various SNRs")
plt.savefig("White_nse_tri1_ana.png")
# Factory noise
plt.figure(9)
#plt.xticks(nvals)
plt.axis([0,20,0,100])
plt.plot(factory_nse_nvals,factory_nse_tri1,'ro')
plt.plot(factory_nse_nvals,factory_nse_tri1)
plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Analysis of Factory Noise at Various SNRs")
plt.savefig("Factory_nse_tri1_ana.png")
# Traffic noise
plt.figure(10)
#plt.xticks(nvals)
plt.axis([0,20,0,100])
plt.plot(traffic_nse_nvals,traffic_nse_tri1,'ro')
plt.plot(traffic_nse_nvals,traffic_nse_tri1)
plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Analysis of Traffic Noise at Various SNRs")
plt.savefig("Traffic_nse_tri1_ana.png")
# Train noise
plt.figure(11)
#plt.xticks(nvals)
plt.axis([0,20,0,100])
plt.plot(train_nse_nvals,train_nse_tri1,'ro')
plt.plot(train_nse_nvals,train_nse_tri1)
plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Analysis of Train Noise at Various SNRs")
plt.savefig("Train_nse_tri1_ana.png")
# Generate a combination plot
plt.figure(12)
plt.axis([0,20,0,100])
#plt.plot(babble_nse_nvals,babble_nse_mono,'ro')
plt.plot(babble_nse_nvals,babble_nse_tri1)
#plt.plot(white_nse_nvals,white_nse_mono,'ro')
plt.plot(white_nse_nvals,white_nse_tri1)
#plt.plot(factory_nse_nvals,factory_nse_mono,'ro')
plt.plot(factory_nse_nvals,factory_nse_tri1)
#plt.plot(traffic_nse_nvals,traffic_nse_mono,'ro')
plt.plot(traffic_nse_nvals,traffic_nse_tri1)
#plt.plot(train_nse_nvals,train_nse_mono,'ro')
plt.plot(train_nse_nvals,train_nse_tri1)

plt.legend(['Babble Noise','White Noise','Factory Noise','Traffic Noise','Train Noise'])

plt.xlabel("SNR in dB")
plt.ylabel("WER in Percentage")
plt.title("Comparisions of Noises at Various SNRs")
plt.savefig("Comp_nse_tri1_ana.png")
