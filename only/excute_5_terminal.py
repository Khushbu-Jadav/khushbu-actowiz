import os

total_urls = 4145
parts = 5

chunk_size = (total_urls + parts - 1) // parts

python_path = r"C:\python practice\venv\Scripts\python.exe"
script_path = r"C:\python practice\only\only_page_save.py"

for i in range(parts):

    start = i * chunk_size
    end = min(start + chunk_size, total_urls)

    cmd = (
        f'start cmd /k ""{python_path}" "{script_path}" {start} {end}"'
    )

    os.system(cmd)

    print(f"Started: {start} -> {end}")