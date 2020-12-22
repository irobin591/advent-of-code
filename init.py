# Roughly inspired by https://github.com/AlexeSimon/adventofcode/blob/master/init.py

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import os
import json
import requests

USER_AGENT = "Python AdventOfCode Generator (Dev)"

env = Environment(
    loader = FileSystemLoader(os.path.abspath('templates')),
    autoescape = select_autoescape(['py']),
)

with open(os.path.join(os.path.dirname(__file__), "config.json"), 'r') as config_file:
    config = json.load(config_file)

for year in range(config['years']['start'], config['years']['end']+1):
    year_dir = str(year)
    if not os.path.exists(os.path.join(year_dir)):
        os.mkdir(os.path.join(year_dir))
    
    for day in range(1,26):
        if year > config['latest']['year']:
            continue
        if year == config['latest']['year'] and day > config['latest']['day']:
            continue

        day_dir = "{:02d}".format(day)

        print("{}/{}".format(year_dir, day_dir))
        
        # Skip if folder already exists
        # if os.path.exists(os.path.join(year_dir, day_dir)):
        #     continue
        
        # Get Inputdata
        if not os.path.exists(os.path.join(year_dir, day_dir, "input.txt")):
            print("  Downloading Inputdata")
            req_input = requests.get(
                "https://adventofcode.com/{}/day/{}/input".format(year, day),
                cookies={"session": config['user_session_id']},
                # headers={"User-Agent": USER_AGENT},
            )
            if req_input.ok:
                # print(req_input.content.decode('utf-8'))
                os.mkdir(os.path.join(year_dir, day_dir))
                with open(os.path.join(year_dir, day_dir, "input.txt"), 'w') as outfile:
                    outfile.write(req_input.content.decode('utf-8'))
                    print("    Success")

            else:
                print("    DAY {}/{}: Not available yet (Errorcode: {})".format(year_dir, day_dir, req_input.status_code))
                continue
        
        # Create code.py file
        if not os.path.exists(os.path.join(year_dir, day_dir, "code.py")):
            print("  Creating Template")
            template = env.get_template("code.py")
            with open(os.path.join(year_dir, day_dir, "code.py"), 'w') as outfile:
                outfile.write(template.render(
                    YEAR=year_dir,
                    DAY=day_dir,
                    AUTHOR=config['author'],
                ))
                print("    Success")
