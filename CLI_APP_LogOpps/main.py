import sys
import os

allowed_lvls: set[str] = {"INFO", "ERROR", "WARN"}


def parcing_func():
    pass


def business_logic(file_path):
    pass


def main():
    pass


if len(sys.argv) >= 2:
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print("File not found. Use <file name>")
        sys.exit(1)
else:
    print("Invalid Path. Please, use: python main.py logs.txt")
    sys.exit(1)
if len(sys.argv) >= 3:
    issue_lvl = sys.argv[2]
    if issue_lvl not in allowed_lvls:
        print(f"This {issue_lvl} is not listed in these logs")
        print(f"List of allowed issues: {allowed_lvls}")
        sys.exit(1)


if __name__ == "__main__":
    main(file_path, issue_lvl)
