import os

# os.makedirs() : for creating multiple dirs
if (not os.path.exists("data")):
    os.mkdir("data")

#for making folders from day 1 to 100

for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")








