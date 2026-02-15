from pathlib import Path

BASE = Path(__file__).resolve().parent
SALARIES_FILE = BASE / "salaries.txt"
fh = open(SALARIES_FILE, "w", encoding="utf-8")
