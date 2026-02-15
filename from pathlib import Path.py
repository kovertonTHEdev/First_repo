from pathlib import Path

# ============================================================
# 0. БАЗА ПРОЕКТА (папка, де лежить цей .py файл)
# ============================================================

BASE = Path(__file__).resolve().parent

TEST_FILE = BASE / "test.txt"
DOCS_DIR = BASE / "documents"
EXAMPLE_TXT = DOCS_DIR / "example.txt"
RAW_BIN = BASE / "raw_data.bin"

print("BASE =", BASE)
print("TEST_FILE =", TEST_FILE)
print("TEST_EXISTS =", TEST_FILE.exists())

print("DOCS_DIR =", DOCS_DIR)
print("EXAMPLE_TXT =", EXAMPLE_TXT)
print("EXAMPLE_EXISTS =", EXAMPLE_TXT.exists())

# ============================================================
# 1. Демонстрація: абсолютний і відносний шлях
# ============================================================

DOCS_DIR.mkdir(exist_ok=True)

print("\nABS EXAMPLE_TXT =", EXAMPLE_TXT.resolve())

# relative_to може кинути помилку, якщо шлях не "всередині" BASE
try:
    print("REL to BASE =", EXAMPLE_TXT.relative_to(BASE))  # documents/example.txt
except ValueError as e:
    print("REL to BASE -> ValueError:", e)

# ============================================================
# 2. Гарантуємо, що файли існують
# ============================================================

if not EXAMPLE_TXT.exists():
    EXAMPLE_TXT.write_text("Hello, world!\n", encoding="utf-8")

if not TEST_FILE.exists():
    TEST_FILE.write_text("first line\nsecond line\nthird line\n", encoding="utf-8")

# ----------------------------
# Тема 69: Робота з файлами
# ----------------------------

# ВАЖЛИВО: open() відкриває ФАЙЛ, а не папку.
# BASE — це папка, тому працюємо з TEST_FILE.

fh = open(TEST_FILE, "r", encoding="utf-8")
# операції над файлом
fh.close()  # Закривати файл обов'язково

###########################

fh = open(TEST_FILE, "w", encoding="utf-8")
symbols_written = fh.write("hello!")
print(symbols_written)  # 6
fh.close()

fh = open(TEST_FILE, "w+", encoding="utf-8")
fh.write("hello!")
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'
fh.close()

###########################

fh = open(TEST_FILE, "w", encoding="utf-8")
fh.write("hello!")
fh.close()

fh = open(TEST_FILE, "r", encoding="utf-8")
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)
fh.close()

###########################

fh = open(TEST_FILE, "w", encoding="utf-8")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open(TEST_FILE, "r", encoding="utf-8")
while True:
    line = fh.readline()
    if not line:
        break
    print(line.strip())
fh.close()

###########################

fh = open(TEST_FILE, "w", encoding="utf-8")
fh.write("first line\nsecond line\nthird line")  # \n залишається у рядках при читанні
fh.close()

fh = open(TEST_FILE, "r", encoding="utf-8")
lines = fh.readlines()
print(lines)
fh.close()

###########################

fh = open(TEST_FILE, "w", encoding="utf-8")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open(TEST_FILE, "r", encoding="utf-8")
lines = [el.strip() for el in fh.readlines()]  # strip прибирає \n
print(lines)
fh.close()

###########################

fh = open(TEST_FILE, "w+", encoding="utf-8")
fh.write("hello!")
fh.seek(1)  # курсор на другий символ
second = fh.read(1)
print(second)  # 'e'
fh.close()

###########################

fh = open(TEST_FILE, "w+", encoding="utf-8")
fh.write("hello!")

position = fh.tell()
print(position)  # 6

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3
fh.close()

# ----------------------------
# Тема 70: Менеджер контексту
# ----------------------------

fh = open(TEST_FILE, "w", encoding="utf-8")
try:
    # Виконання операцій з файлом
    fh.write("Some data")
finally:
    # Закриття файлу гарантує закриття навіть при помилці
    fh.close()

###########################
# альтернатива try/finally:

with open(TEST_FILE, "w", encoding="utf-8") as fh:
    fh.write("Some data")
# Файл автоматично закриється після виходу з with

###########################

with open(TEST_FILE, "w", encoding="utf-8") as fh:
    fh.write("first line\nsecond line\nthird line")

with open(TEST_FILE, "r", encoding="utf-8") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)

# ----------------------------
# Тема 71: Робота з нетекстовими файлами у Python
# ----------------------------

# Пишемо бінарний файл в BASE, щоб не залежати від поточної директорії запуску
with open(RAW_BIN, "wb") as fh:
    fh.write(b"Hello world!")

###########################

s = b"Hello!"
print(s[1])  # 101 (ASCII-код 'e')

###########################

byte_str = "some text".encode()
print(byte_str)

# ----------------------------
# Тема 72: Перетворення чисел у байт-рядки
# ----------------------------

numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)

###########################

for num in [127, 255, 156]:
    print(hex(num))

# ----------------------------
# Тема 73: Кодування рядків (ASCII, UTF-8, CP1251)
# ----------------------------

s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)

###########################

print(b"Hello world!".decode("utf-16"))  # буде "крякозябра", бо не те кодування

###########################

# Відкриття текстового файлу з явними вказівками UTF-8 кодування
with open(TEST_FILE, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# ----------------------------
# Тема 74: Масив байтів
# ----------------------------

byte_array = bytearray(b"Kill Bill")
byte_array[0] = ord("B")
byte_array[5] = ord("K")
print(byte_array)

###########################

byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))
print(byte_array)

# Decode:
byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)

# ----------------------------
# Тема 75: Порівняння рядків
# ----------------------------

string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else:
    print("Рядки різні")

# Метод casefold():

german_word = "straße"
search_word = "STRASSE"

lower_comparison = german_word.lower() == search_word.lower()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}")  # False
print(f"Порівняння з casefold(): {casefold_comparison}")  # True

# ----------------------------
# Тема 76: Робота з архівами
# ----------------------------
# (порожньо)

# ----------------------------
# Тема 77: Основи модуля pathlib
# ----------------------------

from pathlib import PurePath

p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)  # Name: simple.jpg
print("Suffix:", p.suffix)  # Suffix: .jpg
print("Parent:", p.parent)  # Parent: \usr\bin

###########################

# Створюємо файл в BASE, щоб було стабільно
p2 = BASE / "example_local.txt"
p2.write_text("Hello, world!", encoding="utf-8")
print(p2.read_text(encoding="utf-8"))
print("Exists:", p2.exists())

# ----------------------------
# Тема 77: Створення шляхів
# ----------------------------

path_unix = Path("/usr/bin/python3")
path_windows = Path("C:/Users/Username/Documents/file.txt")

base_path = Path("/usr/bin")  # додаються додаткові частини
full_path = base_path / "subdir" / "script.py"
print(full_path)

# ----------------------------
# Тема 78: Відносні та абсолютні шляхи
# ----------------------------

relative_path = Path("documents/example.txt")
absolute_path = (BASE / relative_path).resolve()  # робимо адекватний абсолютний шлях
print(absolute_path)

# .relative_to() може кинути ValueError — ловимо
current_working_directory = DOCS_DIR  # тут логічно: documents
try:
    rel = absolute_path.relative_to(current_working_directory)
    print(rel)
except ValueError as e:
    print("relative_to -> ValueError:", e)

# ----------------------------
# Тема 79: Маніпуляція з компонентами шляху
# ----------------------------

original_path = Path("documents/example.txt")

# Зміна імені файлу .with_name
new_path = original_path.with_name("report.txt")
print(new_path)

# Зміна типу файлу .with_suffix()
new_path2 = original_path.with_suffix(".md")
print(new_path2)

###########################
# rename демонстрація: щоб не падати через "файл вже існує" — прибираємо ціль, якщо вона є

demo_file = BASE / "rename_me.txt"
demo_file.write_text("demo", encoding="utf-8")

renamed_file = demo_file.with_name("renamed_demo.txt")

# Якщо renamed_demo.txt вже існує — видаляємо, інакше Windows кине FileExistsError
if renamed_file.exists():
    renamed_file.unlink()

demo_file.rename(renamed_file)
print("Renamed:", renamed_file.exists())

# ----------------------------
# Тема 79: Читання та запис файлів
# ----------------------------

file_path_text = BASE / "example2.txt"
file_path_text.write_text("Привіт світ!", encoding="utf-8")

text = file_path_text.read_text(encoding="utf-8")  # ...та виводиться на екран.
print(text)

###########################
# write_bytes: щоб було видно результат, додаємо print і зворотнє читання

# Створення об'єкту Path для бінарного файлу
file_path_bin = BASE / "example.bin"

# Бінарні дані для запису
data = b"Python is great!"

# Запис байтів у файл
bytes_written = file_path_bin.write_bytes(data)

print("EXAMPLE.BIN =", file_path_bin)
print("BYTES_WRITTEN =", bytes_written)
print("READ_BYTES =", file_path_bin.read_bytes())


from pathlib import Path

# Створення об'єкту Path для бінарного файлу
file_path = BASE / "example.bin"

# Читання байтів з файлу
binary_data = file_path.read_bytes()
print(binary_data)  # b'Python is great!'


# ----------------------------
# Тема 80: Робота з директоріями
# ----------------------------
from pathlib import Path

# БАЗА ПРОЕКТА (папка, де лежить цей .py файл)
BASE = Path(__file__).resolve().parent

# Створення об'єкту Path для директорії (всередині проєкту)
directory = BASE / "picture"

# Якщо папки нема — щоб приклад не падав
directory.mkdir(exist_ok=True)

# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path.relative_to(BASE))


from pathlib import Path

BASE = Path(__file__).resolve().parent
directory = BASE / "new_folder"
directory.mkdir(parents=True, exist_ok=True)  # створення нової директорії


from pathlib import Path

BASE = Path(__file__).resolve().parent
directory = BASE / "new_folder"
directory.rmdir()  # видалення нової директорії


from pathlib import Path

BASE = Path(__file__).resolve().parent
path = BASE / "picture"

# Перевірка існування
if path.exists():
    print(f"{path} існує")  # picture існує


# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією")  # picture є директорією

# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")

# ----------------------------
# Тема 81: Переміщення та копіювання файлів
# ----------------------------
import shutil
from pathlib import Path

# Вихідний і цільовий шляхи (приклад)
BASE = Path(__file__).resolve().parent
source = BASE / "file.txt"
destination = BASE / "documents" / "file.txt"

# щоб приклад не падав, якщо файл вже переміщений раніше
if source.exists():
    shutil.move(source, destination)
else:
    print("SKIP MOVE: source not found ->", source)

# БАЗА ПРОЄКТУ (не називай це BASE, бо ти його десь нижче перезаписуєш)
# ----------------------------
# Тема 81: Переміщення та копіювання файлів
# ----------------------------
from pathlib import Path

BASE = Path(__file__).resolve().parent
file_txt = BASE / "file.txt"

file_txt.write_text("demo file\n", encoding="utf-8")  # создає файл.тхт кожен раз


BASE = Path(__file__).resolve().parent

file_path = BASE / "picture" / "bot-icon.png"

# Отримання розміру файла
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів")


from pathlib import Path
import time

BASE = Path(__file__).resolve().parent
file_path = BASE / "picture" / "bot-icon.png"

# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime

print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")


from pathlib import Path

BASE = Path(__file__).resolve().parent
# Створення об'єкту Path для файлу
file_path = BASE / "file.txt"

# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f"Файл {file_path} було видалено")
else:
    print(f"Файл {file_path} не існує")
