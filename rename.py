from distutils.file_util import copy_file
from os import listdir, mkdir


from os import makedirs
folder='train/'
makedirs(folder,exist_ok=True)
prev_name=None
file_no=1
src_dir='color_features'
shells=[]
for file in sorted(listdir(src_dir)):
    src=src_dir+'/'+file
    file_name=file.split('_')
    print(file_name,prev_name)
    if file_name[0]+'_'+file_name[1]!=prev_name:
        file_no=1
        prev_name=file_name[0]+'_'+file_name[1]
        print(prev_name)
        shells.append(prev_name)
    else:
        file_no+=1
    dest=folder+'/'+file_name[0]+'_'+file_name[1]+'.'+str(file_no)+'.jpg'
    copy_file(src,dest)
    
