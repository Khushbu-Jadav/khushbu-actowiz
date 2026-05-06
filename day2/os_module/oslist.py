import os

#list of folders in data folder
folders = os.listdir("data")

print(folders)

for folder in folders:
    print(folder)
    #list of files in particular folder
    print(os.listdir(f"data/{folder}"))