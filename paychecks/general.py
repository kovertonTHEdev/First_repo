from calculation_func import total_salary
from pathlib import Path
BASE = Path(__file__).resolve().parent
SALARIES_FILE = BASE / "salaries.txt"

total, average = total_salary(SALARIES_FILE)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")