import os

#to rename existing folders : rename(src,dest)
for i in range(0,100):
    os.rename(f"data/Day{i+1}",f"data/tutorial{i+1}")