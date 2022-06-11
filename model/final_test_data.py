
from distutils.file_util import copy_file
from os import listdir, makedirs
import random
src_dir='train/'
labeldirs=[]
prev_name=None
for file in sorted(listdir(src_dir)):
    file_name=file.split('.')
    if file_name[0]!=prev_name:
        prev_name=file_name[0]
        labeldirs.append(file_name[0])
print(labeldirs)
dataset_home='finaldataset/'
for labeldir in labeldirs:
    newdir=dataset_home+labeldir
    makedirs(newdir,exist_ok=True)
    
src_dir='train/'
for file in listdir(src_dir):
    src=src_dir+'/'+file
    file_name=file.split('.')
    dst=dataset_home+file_name[0]+'/'+file
    copy_file(src,dst)