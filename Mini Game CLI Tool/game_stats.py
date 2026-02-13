import sys
from pathlib import Path

if len(sys.argv) < 2: #1
    print("Usage: python game_stats.py <folder_path>")
    sys.exit(1)
if len(sys.argv) == 2:
    root_dir = Path(sys.argv[1]) #3
    if not root_dir.exists(): 
        print(f"This folder {root_dir} doesn't exist")
        sys.exit(1)
    if not root_dir.is_dir():
        print(f"This {root_dir} not a directory")
        sys.exit(1)
 
    print("Its good")