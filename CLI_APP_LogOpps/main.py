import sys
import os
import re
from pathlib import Path
from datetime import datetime

allowed_lvls: set[str] = {"INFO", "ERROR", "WARN"}
start_dt = datetime(1970, 1, 1, 1)
end_dt = datetime(2077, 1, 1, 1)


def parcing_func(raw_line, start_dt, end_dt):
    clean_line = raw_line.strip()
    if not clean_line:
        return None
    pattern = r"^(?P<timestamp>.*?)\s*\|\s*(?P<level>.*?)\s*\|\s*(?P<service>.*?)\s*\|\s*(?P<meta>.*?)\s*\|\s*(?P<message>.*)$"
    match = re.match(pattern, clean_line)
    if match:
        data = match.groupdict()
        try:
            dt_from_log = datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None
        if start_dt <= dt_from_log <= end_dt:
            meta_str = data["meta"]
            pattern = r"(\w+)=([^ ]+)"
            data["meta"] = dict(re.findall(pattern, meta_str))
            data["dt"] = dt_from_log
            return data
    return None


def business_logic(file_path):
    pass


def main(input_path, start_dt, end_dt):
    count = 0
    for path in file_list:
        try:
            with open(path, "r", encoding="UTF-8") as file:
                for line in file:
                    data = parcing_func(line, start_dt, end_dt)
                    if data:
                        count += 1
        except PermissionError:
            print("You don't have rights to open this file")
            sys.exit(1)
    return count


issue_lvl = None
if len(sys.argv) >= 2:
    file_path = sys.argv[1]
    input_path = Path(sys.argv[1])
    if os.path.exists(input_path):
        if os.path.isfile(input_path):
            file_list = [input_path]
            if not file_list:
                print("File list is empty")
                sys.exit(1)
        elif os.path.isdir(input_path):
            file_list = list(Path(input_path).glob("*.txt"))
            if not file_list.endswith("*txt"):
                print("This is not text file")
        else:
            print("This path and file doesnt exist, please, use main.py logs.txt")
    else:
        print("This path doesn't exist, please, use main.py logs.txt")
        sys.exit(1)
else:
    print("Invalid quantity of files. Please, use: python main.py logs.txt")
    sys.exit(1)
if len(sys.argv) >= 3:
    issue_lvl = sys.argv[2]
    if issue_lvl not in allowed_lvls:
        print(f"This {issue_lvl} is not listed in these logs")
        print(f"List of allowed issues: {allowed_lvls}")
        sys.exit(1)


if __name__ == "__main__":
    main(input_path, start_dt, end_dt)
