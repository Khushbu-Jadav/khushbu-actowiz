import os
#system method use for running operating system shell command from python
x=os.system("dir")

print(x)

os.system("notepad")

os.system("calc")

print(os.getcwd())
if (not os.path.exists("data")):
    os.mkdir("dir1")
os.chdir("/Users")
print(os.getcwd())