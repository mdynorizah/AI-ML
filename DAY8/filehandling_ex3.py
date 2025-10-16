import os
#file_path= r'/Users/norizahbintimdyunus/nmy/DAY8/ourfile/ourfiles'
filepath=os.getcwd()
filename=input('Enter File Name to Create File: \t')
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath, 'r')
    content=file.read()
    print('File Content as follows')
    print(content)
    file.close()
else:
    print(f'No such file {filename} exist')