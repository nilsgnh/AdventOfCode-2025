import os
import datetime
import requests
import json

day = datetime.datetime.now().day
folder_name = f"day{day}"#:02d
os.makedirs(folder_name, exist_ok=True)
solver_file_path = os.path.join(folder_name, f"slv_{day:02d}.py")
with open(solver_file_path, 'w') as solver_file:
    solver_file.write("")

input_file_path = os.path.join(folder_name, "input.txt")
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
session_cookie = config["session_cookie"]
url = f"https://adventofcode.com/2025/day/{day}/input"
cookies = {'session': session_cookie}
response = requests.get(url, cookies=cookies)
with open(input_file_path, 'w') as input_file:
    input_file.write(response.text)