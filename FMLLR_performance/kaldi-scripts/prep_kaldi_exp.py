#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to prepare a Kaldi experiment folder
# Note : It is assumed base folder and data folders are already created and present
#         in the base path

import os

# Change these two accrding to your needs
print('Setting PATHS for script..........')
base_path = "/media/data1/workspace-applications/kaldi-trunk/egs/digits21"
database_path = base_path+"/digits_audio"

data_dir = base_path + '/data'
data_test_dir = data_dir + '/test'
data_train_dir = data_dir + '/train'

print('BASE PATH: %s'%base_path)
print('DATABASE DIRECTORY: %s'%data_dir)
print('TEST DATA DIRECTORY: %s'%data_test_dir)
print('TRAIN DATA DIRECTORY: %s'%data_train_dir)

# first we need to create data directory
print('Creating DATA DIR......')
data_dir_cmd = 'mkdir -p '+data_test_dir+' '+data_train_dir
os.system(data_dir_cmd)

# Generate files for train directory
# Some of the files are assumed to be in current directory
print("*************GENERATING TRAINING DATA************************")
# spk2gender
print('Copying spk2gender_train to %s/spk2gender'%data_train_dir)
os.system('cp spk2gender_train '+data_train_dir+'/spk2gender')

# wav.scp
print("Generating wav.scp")
os.system('./gen_wav_scp_kaldi.py '+database_path+'/train')
os.system('./sort_gen_kaldi.py wav.scp')
os.system('cp wav.scp_new '+data_train_dir+'/wav.scp')
os.system('rm wav.scp wav.scp_new')

# text
print("Generating text")
os.system('./gen_text_kaldi.py '+database_path+'/train')
os.system('./sort_gen_kaldi.py text')
os.system('cp text_new '+data_train_dir+'/text')
os.system('rm text text_new')

# utt2spk
print("Generating utt2spk")
os.system('./gen_utt2spk_kaldi.py '+database_path+'/train')
os.system('./sort_gen_kaldi.py utt2spk')
os.system('cp utt2spk_new '+data_train_dir+'/utt2spk')
os.system('rm utt2spk utt2spk_new')


print("*************************************************************")
# Generate files for test directory
print("************************ GENERATING TEST DATA ***************")
# spk2gender_test
print('Copying spk2gender_test to %s/spk2gender'%data_test_dir)
os.system('cp spk2gender_test '+data_test_dir+'/spk2gender')

# wav.scp
print("Generating wav.scp")
os.system('./gen_wav_scp_kaldi.py '+database_path+'/test')
os.system('./sort_gen_kaldi.py wav.scp')
os.system('cp wav.scp_new '+data_test_dir+'/wav.scp')
os.system('rm wav.scp wav.scp_new')

# text
print("Generating text")
os.system('./gen_text_kaldi.py '+database_path+'/test')
os.system('./sort_gen_kaldi.py text')
os.system('cp text_new '+data_test_dir+'/text')
os.system('rm text text_new')

# utt2spk
print("Generating utt2spk")
os.system('./gen_utt2spk_kaldi.py '+database_path+'/test')
os.system('./sort_gen_kaldi.py utt2spk')
os.system('cp utt2spk_new '+data_test_dir+'/utt2spk')
os.system('rm utt2spk utt2spk_new')
print("*************************************************************")

# corpus.txt
os.system('mkdir -p '+data_dir+'/local')
print("Generating corpus.txt")
os.system('./gen_corpus_kaldi.py '+database_path)
os.system('./sort_gen_kaldi.py corpus.txt')
os.system('cp corpus.txt_new '+data_dir+'/local/corpus.txt')
os.system('rm corpus.txt corpus.txt_new')


# Now for language data, we assume you have dict directory in pwd
# We'll just copy there
os.system('mkdir -p '+data_dir+'/local/dict')
print('Copying dict directory to %s/local/dict'%data_dir)
os.system('cp dict/* '+data_dir+'/local/dict/')

# For scoring script we will copy from here
print('Copying local directory to %s/local'%base_path)
os.system('cp -r local '+base_path+'/')
print('Copying conf directory to %s/conf'%base_path)
os.system('cp -r conf '+base_path+'/')
print('Copying steps to %s/steps'%base_path)
os.system('cp -r steps '+base_path+'/')
print('Copying utils to %s/utils'%base_path)
os.system('cp -r utils '+base_path+'/')
print('Copying cmd.sh path.sh run.sh to %s/cmd.sh %s/path.sh %s/run.sh'%(base_path,base_path,base_path))
os.system('cp cmd.sh path.sh run.sh '+base_path+'/')
