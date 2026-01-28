RUN_INPUT = False  # Если True — будут запрашиваться input() (ввод с клавиатуры). Если False — эти части пропускаются.


# ============================================================
# HOME TASK: Склейка имени и фамилии
# ============================================================

first_name = "Andrii"                 # строка с именем
last_name = "Nedoshivkin"             # строка с фамилией
full_name = first_name + " " + last_name  # склеиваем: имя + пробел + фамилия

print(full_name)                      # выводим полное имя


# ============================================================
# HOME TASK: Площадь комнаты (числа как float)
# ============================================================

length = 2.75                         # длина комнаты (число)
width = 1.75                          # ширина комнаты (число)
area = length * width                 # площадь = длина * ширина

show = (f"With width {width} and length {length} of the room, its area is equal to {area}")
# show — строка с результатом (f-string)
# ВНИМАНИЕ: ты тут show не печатаешь. Чтобы увидеть, нужно print(show).


# ============================================================
# HOME TASK: Площадь комнаты (числа как строки -> перевод в float)
# ============================================================

length = "2.75"                       # длина как строка
width = "1.75"                        # ширина как строка
area = float(length) * float(width)   # переводим строки в float и считаем площадь

show = (f"With width {width} and length {length} of the room, its area is equal to {area}")
# show — строка с результатом (опять же, если надо увидеть: print(show))


# ============================================================
# HOME TASK: Площадь комнаты (ввод от пользователя)
# ============================================================

if RUN_INPUT:
    length = float(input("Enter length size"))  # просим длину, переводим в float
    width = float(input("Enter width size"))    # просим ширину, переводим в float
    area = length * width                       # считаем площадь
    print(area)                                 # выводим площадь (чтобы видеть результат)


# ============================================================
# HOME TASK: Работа со списком
# ============================================================

my_list = [2024, 3.12]              # список с числами
some_data = ["Python"]              # другой список (с одной строкой)

my_list.extend(some_data)           # extend добавляет элементы списка some_data в конец my_list
# было: [2024, 3.12]
# стало: [2024, 3.12, "Python"]

my_list.insert(1, "Python")         # insert вставляет элемент по индексу 1 (второе место)
# станет: [2024, "Python", 3.12, "Python"]

my_list.reverse()                   # reverse переворачивает список на месте (в обратном порядке)


# ============================================================
# TASK: Проверка возраста
# ============================================================

if RUN_INPUT:
    age_input = int(input("\nPlease, Enter your age: "))  # ввод возраста -> int

    if age_input < 18:         # если меньше 18
        print("Acess Denied")  # доступ запрещён
    else:                      # иначе (18 и больше)
        print("Access Granted")# доступ разрешён


# ============================================================
# TASK: Сортировка чисел, введённых пользователем
# ============================================================

if RUN_INPUT:
    nums = input("Please, enter numbers: ")  # ввод одной строкой, например: "5 2 9 1 3"
    nums = nums.split()                      # split() делит строку по пробелам -> список строк

    numbers = []                             # сюда соберём числа уже как int

    for n in nums:                           # перебираем каждую строку-число
        numbers.append(int(n))               # переводим в int и добавляем в список numbers

    sorted_nums = sorted(numbers)            # sorted() возвращает новый отсортированный список
    print(sorted_nums)                       # печать результата


# ============================================================
# TASK: Сортировка списка на месте (sort)
# ============================================================

nums = [5, 2, 9, 1, 3]   # исходный список
nums.sort()              # sort() сортирует сам список (на месте)
print(nums)              # вывод отсортированного


# ============================================================
# TASK: Копия списка + сортировка копии
# ============================================================

nums = [5, 2, 9, 1, 3]       # исходный
nums_copy = nums.copy()      # делаем копию (чтобы не менять оригинал)
nums_copy.sort()             # сортируем копию

print(nums)                  # оригинал остался как был
print(nums_copy)             # копия отсортирована


# ============================================================
# TASK: Сортировка по длине слова (key=len)
# ============================================================

words = ["banana", "Apple", "cherry"]
words.sort(key=len)      # key=len: сортируем по длине слова
print(words)


# ============================================================
# TASK: Очистка слов (strip + lower) и сортировка
# ============================================================

words = ["  Banana", "apple  ", "  Cherry ", "apple"]

clean_words = []                 # сюда складываем очищенные слова

for w in words:                  # перебираем исходные строки
    clean_words.append(w.strip().lower())
    # strip() убирает пробелы по краям
    # lower() делает все буквы маленькими

clean_words.sort()               # сортируем по алфавиту
print(clean_words)


# ============================================================
# TASK: Подсчёт, сколько раз встречается слово "apple"
# ============================================================

words = ["Apple", "banana", "apple", "Cherry", "banana"]
good_words = []

for w in words:
    good_words.append(w.strip().lower())  # очистили и привели к нижнему регистру

good_words.sort()                         # отсортировали

count_apple = good_words.count("apple")   # count считает, сколько раз "apple" в списке

print(good_words)
print(count_apple)


# ============================================================
# TASK: Удаление дублей через set (слова)
# ============================================================

words = ["apple", "banana", "apple", "cherry", "banana"]

d_words = set(words)       # set убирает повторы (но порядок не гарантируется)
words = list(d_words)      # возвращаем обратно в список

print(words)               # порядок может быть не алфавитный


# ============================================================
# TASK: Подсчёт слов через словарь (dict)
# ============================================================

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
result = {}  # словарь: слово -> сколько раз встретилось

for w in words:
    current = result.get(w, 0)   # get(w, 0): если ключа нет — вернёт 0
    result[w] = current + 1      # увеличиваем счётчик на 1

print(result)


# ============================================================
# TASK: Удаление дублей в числах и сортировка
# ============================================================

nums = [3, 1, 4, 1, 5, 9, 2, 3]

nums = list(set(nums))    # set убрал повторы -> list вернули в список
nums.sort()               # сортируем по возрастанию

print(nums)


# ============================================================
# TASK: Срез (reverse списка)
# ============================================================

numbers = [1,2,3,4,5,6,7,8,9,10]
reverse_numbers = numbers[::-1]   # срез с шагом -1 -> разворот
print(reverse_numbers)


# ============================================================
# TASK: Срез чётных чисел (по твоей логике берёшь индексы 1,3,5...)
# ============================================================

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = numbers[1:10:2]
# 1:10:2 означает:
# старт индекс 1 (это число 2)
# до индекса 10 (не включая 10)
# шаг 2 -> берём каждый второй элемент
print(even_numbers)


# ============================================================
# TASK: Копия через срез + сортировка по убыванию
# ============================================================

nums = [3, 1, 4, 1, 5, 9, 2]
nums_copy = nums[:]              # копия списка через срез
nums_copy.sort(reverse=True)     # reverse=True -> сортировка по убыванию

print(nums)
print(nums_copy)


# ============================================================
# TASK: Берём элементы с чётными индексами и сортируем по убыванию
# ============================================================

numbers = [5, 12, 7, 3, 9, 2, 10, 6]

numbers_copy = numbers[0:10:2]   # берём 0,2,4,6... (чётные индексы)
numbers_copy.sort(reverse=True)  # сортировка по убыванию

print(numbers)                   # оригинал
print(numbers_copy)              # обработанный


# ============================================================
# TASK: Таймер событий (исправлять не буду, просто комментирую, тут логика сломана)
# ============================================================

if RUN_INPUT:
    allowed_events = ["deploy", "build", "test", "backup"]
    event_type = input("Text please type of event: ")
    event_time = int(input("Text please duration time: "))

    # ВНИМАНИЕ: эта строка неправильная:
    # if event_type: allowed_events
    # Она ничего не проверяет. Ты хотел: if event_type in allowed_events:
    if event_type:
        allowed_events  # это просто выражение, оно ничего не делает
    else:
        print("Unknown event")

    if event_time < 0:
        print("Invalid duration")

    h = event_time // 3600
    m = (event_time % 3600) // 60
    s = event_time % 60

    print(f"Event {event_type}: {h}h {m}m {s}s")


# ============================================================
# TASK: Таймер событий (правильнее сделано)
# ============================================================

if RUN_INPUT:
    events = ["start", "stop", "restart"]
    event_type = input("Text here please type of event: ")
    event_time1 = int(input("Text please duration time: "))

    if event_type not in events:      # проверяем, что тип события разрешён
        print("Invalid type")
    elif event_time1 < 0:             # проверяем, что время не отрицательное
        print("Invalid duration")
    else:
        # если всё валидно — считаем часы, минуты, секунды
        h = event_time1 // 3600
        m = (event_time1 % 3600) // 60
        s = event_time1 % 60

        print(f"Event {event_type}: {h}h {m}m {s}s")


# ============================================================
# TASK: Очистка пользователей + удаление дублей + сортировка
# ============================================================

raw_users = ["  Andrii ", "", "BORIS", "anna", "  ", "Boris", "ANNA"]

clean_users = []

for r in raw_users:
    name = r.strip().lower()     # чистим пробелы и приводим к нижнему регистру
    if name:                     # если не пустая строка
        clean_users.append(name) # добавляем в список

clean_users = list(set(clean_users))  # убираем повторы
clean_users.sort()                    # сортируем
print(clean_users)


# ============================================================
# TASK: Очистка действий + удаление дублей + сортировка + печать
# ============================================================

raw_actions = ["  Login", "logout ", "LOGIN", "", "  ", "Logout", "login", "Delete"]

clean_actions = []

for r in raw_actions:
    action = r.strip().lower()
    if action:
        clean_actions.append(action)

clean_actions = list(set(clean_actions))  # удалили дубли
clean_actions.sort()                      # сортировка

for action in clean_actions:
    print(action)


# ============================================================
# TASK: Счётчик действий (dict)
# ============================================================

actions = [" Login", "logout ", "LOGIN", "update", "Logout", "", "login"]

clean_actions = []
result = {}

for action in actions:
    action = action.strip().lower()
    if action:
        clean_actions.append(action)

for action in clean_actions:
    if action in result:
        result[action] += 1
    else:
        result[action] = 1

print(result)


# ============================================================
# TASK: FizzBuzz от 1 до N (N вводится, проверка через try/except)
# ============================================================

while True:
    text = input("Введите число: ")

    try:
        text = int(text)                 # пытаемся перевести ввод в int
        if text <= 0:
            print("Нужно число больше 0")
            continue                     # просим ввод снова

        # если число > 0 — печатаем FizzBuzz
        for t in range(1, text + 1):
            if t % 3 == 0 and t % 5 == 0:
                print("FizzBuzz")
            elif t % 3 == 0:
                print("Fizz")
            elif t % 5 == 0:
                print("Buzz")
            else:
                print(t)

        break                             # выходим из while после успешного выполнения

    except ValueError:
        print("Это не число")            # если int() не получилось


# ============================================================
# TASK: while + match (match стоит ПОСЛЕ цикла, работает только для последнего text)
# ============================================================

while True:
    text = input("Enter please: ")

    if not text:
        print("Empty info")
        continue

    if text == "exit":
        print("Good luck next time")
        break

# ВНИМАНИЕ: match тут выполнится 1 раз, после выхода из while
match text:
    case "Yes":
        print("Accepted")
    case "No":
        print("Denied")
    case _:
        print("Undefined command")


# ============================================================
# TASK: Команды: exit / count (ввод числа c и печать 1..c)
# ============================================================

while True:
    command = input("Enter command: ")

    if not command:
        print("Empty info")
        continue

    if command == "exit":
        print("Good luck next time")
        break

    if command == "count":
        try:
            c = int(input("Enter please c: "))   # ввод числа
            if c <= 0:
                print("Need number > 0")
                continue                         # если не подходит — просим команду снова

            for i in range(1, c + 1):
                print(i)

        except ValueError:
            print("Это не число")


### TASK
is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
    print("Successful candidate")
else:
    is_next = False
    print("Candidate is not valid")



### TASK
work_experience = int(input("Enter your full work experience in years: "))
developer_type = "Junior"
if work_experience > 1 and work_experience < 6:
    developer_type = "Middle"
    print(developer_type)
elif work_experience == 0 or work_experience == 1:
    developer_type = "Junior"
    print(developer_type)
else:
    developer_type = "Senior"
    print(developer_type)


### TASK
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 1:
        result = "Positive odd number"
    if num % 2 == 0:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"
