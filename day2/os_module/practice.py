import os
from datetime import datetime
import string

for ch in string.ascii_uppercase:
    if not os.path.exists(ch):
        os.mkdir(ch)

    for i in range(10):
        folder = f"{ch}/{ch.lower()}{i}"
        os.makedirs(folder, exist_ok=True)

        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        message = f"this file is created at {time}"

        for ext in ["txt", "html", "json"]:
            with open(f"{folder}/{ch}{i}.{ext}", "w") as f:
                f.write(message)

        print(message)














































# remove all directory
# for letter in string.ascii_uppercase:
#     if os.path.exists(letter):
#         os.rmdir(letter)
#         print(f"Deleted empty directory: {letter}")





