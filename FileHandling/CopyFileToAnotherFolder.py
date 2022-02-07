import shutil
import os
files = ['C:\\Users\\HP Notebook\\Documents\\sample1.txt']
dest_folder = 'C:\\Users\\HP Notebook\\Documents\\sampleFolder'
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)
for file in files:
    shutil.copy(file, dest_folder+'\\sample.txt')