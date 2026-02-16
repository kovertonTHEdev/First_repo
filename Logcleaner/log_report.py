import sys
from pathlib import Path

from reporter_func import get_report

BASE = Path(__file__).resolve().parent
REPORT_FILE = BASE / "report.txt"

if len(sys.argv) < 2:
    print("python log_report.py <доступ_до_директорії>")
    sys.exit(1)
str_path = sys.argv[1]
path_obj = Path(str_path) # конвертація строки в об'єкт path 

if not path_obj.exists():
    print("This path does not exist") # перевірка розташування
    sys.exit(1)
if not path_obj.is_file():
    print("This object is not file") # перевірка чи це файл
    sys.exit(1)

result = get_report(path_obj)
with open("report.txt", "w", encoding="UTF=8") as file:
    file.write(result)