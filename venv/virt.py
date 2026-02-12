import sys
import os
from pathlib import Path

if len(sys.argv) < 2:
    print ("python hw03.py <доступ_до_директорії>")
    sys.exit(1)
if len(sys.argv) > 1:
    second_el = sys.argv[1]
    second_el_pathobj = Path(second_el)
    if not second_el_pathobj.exists():
        print("Цей путь не існує")
        sys.exit(1)
    if not second_el_pathobj.is_dir():
        print("Цієї директорії не існує")
        sys.exit(1) 

def function(path: Path, depth: int = 0):
    indent = " " * 4 * depth
    for file in path.iterdir():
        print(f"{indent}{file.name}")
        if file.is_dir():
            function(file, depth + 1)
    function(second_el_pathobj, 0)