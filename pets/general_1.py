from pathlib import Path
from cats_func import get_cats_info
BASE = Path(__file__).resolve().parent
CATS_FILE = BASE / "cats_file.txt"

cats_info = get_cats_info(CATS_FILE)
print(cats_info)
