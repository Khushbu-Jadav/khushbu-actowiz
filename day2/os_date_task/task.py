import os
from datetime import datetime
import string
import shutil

#create directory
for letter in string.ascii_uppercase:
    if not os.path.exists(letter):
        os.mkdir(letter)

#create sub directory
    for number in range(10):
        folder = f"{letter}/{letter.lower()}{number}"
        os.makedirs(folder, exist_ok=True)

#get time & date
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        message = f"this file is created at {time}"

#create 3 file
        for ext in ["txt", "html", "json"]:
            file_path = f"{folder}/{letter}{number}.{ext}"
            with open(file_path, "w") as f:
                f.write(message)

# create destination folders
        html_folder = f"{folder}/HTML"
        txt_folder = f"{folder}/txt"
        json_folder = f"{folder}/Json"

        os.makedirs(html_folder, exist_ok=True)
        os.makedirs(txt_folder, exist_ok=True)
        os.makedirs(json_folder, exist_ok=True)

# move files using shutil
        shutil.move(f"{folder}/{letter}{number}.html", f"{html_folder}/{letter}{number}.html")
        shutil.move(f"{folder}/{letter}{number}.txt", f"{txt_folder}/{letter}{number}.txt")
        shutil.move(f"{folder}/{letter}{number}.json", f"{json_folder}/{letter}{number}.json")

        print(message)