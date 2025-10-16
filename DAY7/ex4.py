# import os
# import inspect
# print('Current Directory:',os.getcwd())
# functions=inspect.getmembers(os,inspect.isbuiltin)
# print('All function in os module')
# for n, func in functions:
#     print(n)



#create a folder inside current directory using python
# import os
# cdir=os.getcwd()
# folder_name=input('Enter Folder Name to create: \t')
# folder_path=os.path.join(cdir,folder_name)
# if(os.path.exists(folder_path)):
#     print('Folder Already Exist')
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f'{folder_name} created at {folder_path}')



#rename a folder
#  os.rename(folder_name, "renamed_folder_)
#write code to rename a folder
# you will take folderName from user
# if it is exist, you will ask new name and rename it
import os
cdir=os.getcwd()
old_folder_name=input('Enter the exixting Folder Name to rename \t: \t')
folder_path=os.path.join(cdir,folder_name)
if(os.path.exists(old_folder_name)):
    new_folder_name=input("Enter new folder name \t:\t")
else:
     os.makedirs(folder_path,exist_ok=True)
     print(f'{folder_name} created at {folder_path}')

