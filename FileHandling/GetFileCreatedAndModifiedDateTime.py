import os, time

# File Created time
file_path = 'C:\\Users\\HP Notebook\\Documents\\sampleFolder\\sample.txt'
local_time = time.ctime(os.path.getctime(file_path))
print('File was created on (in local time): {0}'.format(local_time))
created_time = time.gmtime(os.path.getctime(file_path))
print('File was created on : {0}'.format(created_time))

# File modified time
local_modified = time.ctime(os.path.getmtime(file_path))
print('File was modified on (in local time): {0}'.format(local_modified))
modified_time = time.gmtime(os.path.getmtime(file_path))
print('File was modified on : {0}'.format(modified_time))

# File Created time of set of files
dire_path = 'C:\\Users\\HP Notebook\\Documents\\sampleFolder'
os.chdir(dire_path)
for file in os.listdir():
    print('this file was created at : ' + time.ctime(os.path.getctime(file)))
