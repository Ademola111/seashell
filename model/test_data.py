
from distutils.file_util import copy_file
from os import listdir, makedirs
import random
src_dir='train/'
sub_dirs=['train/','test/']
labeldirs=[]
prev_name=None
for file in sorted(listdir(src_dir)):
    file_name=file.split('.')
    if file_name[0]!=prev_name:
        prev_name=file_name[0]
        labeldirs.append(file_name[0])
print(labeldirs)
dataset_home='dataset/'
for sub_dir in sub_dirs:
    for labeldir in labeldirs:
        newdir=dataset_home+sub_dir+labeldir
        makedirs(newdir,exist_ok=True)
    
random.seed(1)
val_ratio=0.20
src_dir='train/'
for file in listdir(src_dir):
    src=src_dir+'/'+file
    dest_dir='train/'
    if random.random()<val_ratio:
        dest_dir='test/'
    file_name=file.split('.')
    dst=dataset_home+dest_dir+file_name[0]+'/'+file
    copy_file(src,dst)