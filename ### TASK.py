RUN_INPUT = False  # флаг: если True — участки с input() выполняются, если False — пропускаются (удобно для тестов без ввода)


# ============================================================
# ЗАДАЧА 1: Склейка имени и фамилии
# ============================================================

first_name = "Andrii"  # строка с именем
last_name = "Nedoshivkin"  # строка с фамилией
full_name = first_name + " " + last_name  # склеиваем строки через +, добавляя пробел между ними

print(full_name)  # выводим итоговую строку


# ============================================================
# ЗАДАЧА 2: Площадь комнаты (числа как float)
# ============================================================

length = 2.75  # длина комнаты как число float
width = 1.75  # ширина комнаты как число float
area = length * width  # площадь = длина * ширина

show = (f"With width {width} and length {length} of the room, its area is equal to {area}")  # формируем строку-отчёт через f-string
# (почему так) f-string удобен: не надо вручную склеивать строки и числа


# ============================================================
# ЗАДАЧА 3: Площадь комнаты (числа как строки -> перевод в float)
# ============================================================

length = "2.75"  # длина как строка (это не число)
width = "1.75"  # ширина как строка
area = float(length) * float(width)  # переводим строки в float, иначе умножение строк невозможно

show = (f"With width {width} and length {length} of the room, its area is equal to {area}")  # снова делаем строку-отчёт


# ============================================================
# ЗАДАЧА 4: Площадь комнаты (ввод от пользователя)
# ============================================================

if RUN_INPUT:  # выполняем блок только если включён ввод
    length = float(input("Enter length size"))  # input() даёт строку, поэтому переводим в float
    width = float(input("Enter width size"))  # аналогично
    area = length * width  # считаем площадь
    print(area)  # выводим площадь


# ============================================================
# ЗАДАЧА 5: Работа со списком (extend, insert, reverse)
# ============================================================

my_list = [2024, 3.12]  # список со значениями int и float
some_data = ["Python"]  # второй список (одна строка)

my_list.extend(some_data)  # добавляем элементы списка some_data в конец my_list (расширяем список)

my_list.insert(1, "Python")  # вставляем "Python" на позицию с индексом 1, сдвигая элементы вправо

my_list.reverse()  # переворачиваем список “на месте” (без создания нового)


# ============================================================
# ЗАДАЧА 6: Проверка возраста (if/else)
# ============================================================

if RUN_INPUT:  # выполняем блок только при RUN_INPUT == True
    age_input = int(input("\nPlease, Enter your age: "))  # берём ввод и переводим в int, чтобы сравнивать числа

    if age_input < 18:  # проверяем условие “меньше 18”
        print("Acess Denied")  # печатаем запрет
    else:  # иначе
        print("Access Granted")  # печатаем разрешение


# ============================================================
# ЗАДАЧА 7: Сортировка чисел, введённых пользователем (split + append + sorted)
# ============================================================

if RUN_INPUT:
    nums = input("Please, enter numbers: ")  # ввод строки с числами через пробел
    nums = nums.split()  # режем строку по пробелам -> получаем список строк

    numbers = []  # сюда будем складывать числа int

    for n in nums:  # перебираем строки из списка nums
        numbers.append(int(n))  # каждую строку переводим в int и добавляем в numbers

    sorted_nums = sorted(numbers)  # создаём новый отсортированный список (оригинал numbers не меняется)
    print(sorted_nums)  # печатаем отсортированный список


# ============================================================
# ЗАДАЧА 8: Сортировка списка на месте (sort)
# ============================================================

nums = [5, 2, 9, 1, 3]  # исходный список чисел
nums.sort()  # сортируем сам список nums (изменяет nums)
print(nums)  # печатаем уже отсортированный nums


# ============================================================
# ЗАДАЧА 9: Копия списка + сортировка копии
# ============================================================

nums = [5, 2, 9, 1, 3]  # исходный список
nums_copy = nums.copy()  # делаем отдельную копию списка, чтобы не портить оригинал
nums_copy.sort()  # сортируем копию

print(nums)  # печатаем оригинал (он остался как был)
print(nums_copy)  # печатаем отсортированную копию


# ============================================================
# ЗАДАЧА 10: Сортировка по длине слова (key=len)
# ============================================================

words = ["banana", "Apple", "cherry"]  # список строк
words.sort(key=len)  # сортируем по длине строки (len возвращает длину)
print(words)  # печать результата


# ============================================================
# ЗАДАЧА 11: Очистка слов (strip + lower) и сортировка
# ============================================================

words = ["  Banana", "apple  ", "  Cherry ", "apple"]  # строки с пробелами и разным регистром
clean_words = []  # список для очищенных слов

for w in words:  # перебираем исходные слова
    clean_words.append(w.strip().lower())  # strip убирает пробелы по краям, lower приводит к нижнему регистру

clean_words.sort()  # сортируем по алфавиту
print(clean_words)  # печатаем очищенный список


# ============================================================
# ЗАДАЧА 12: Подсчёт, сколько раз встречается слово "apple" (count)
# ============================================================

words = ["Apple", "banana", "apple", "Cherry", "banana"]  # исходный список
good_words = []  # список очищенных слов

for w in words:  # перебираем исходные слова
    good_words.append(w.strip().lower())  # чистим пробелы и приводим к lower

good_words.sort()  # сортируем, порядок тут не обязателен для count, но ты сделал
count_apple = good_words.count("apple")  # count считает количество точных совпадений строки "apple"

print(good_words)  # печатаем очищенный список
print(count_apple)  # печатаем, сколько раз встретилось "apple"


# ============================================================
# ЗАДАЧА 13: Удаление дублей через set (слова)
# ============================================================

words = ["apple", "banana", "apple", "cherry", "banana"]  # список с дублями

d_words = set(words)  # set убирает повторы (но порядок в set не гарантирован)
words = list(d_words)  # превращаем обратно в list

print(words)  # печатаем список без дублей (порядок может быть “случайным”)


# ============================================================
# ЗАДАЧА 14: Подсчёт слов через словарь (dict + get)
# ============================================================

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]  # список слов
result = {}  # словарь: слово -> количество

for w in words:  # перебираем каждое слово
    current = result.get(w, 0)  # get берёт текущее значение по ключу; если ключа нет — вернёт 0
    result[w] = current + 1  # увеличиваем счётчик на 1

print(result)  # печатаем “частотный словарь”


# ============================================================
# ЗАДАЧА 15: Удаление дублей в числах и сортировка
# ============================================================

nums = [3, 1, 4, 1, 5, 9, 2, 3]  # список с повторами

nums = list(set(nums))  # set убирает повторы, list возвращает обратно список
nums.sort()  # сортируем по возрастанию
print(nums)  # печать результата


# ============================================================
# ЗАДАЧА 16: Разворот списка через срез [::-1]
# ============================================================

numbers = [1,2,3,4,5,6,7,8,9,10]  # исходный список
reverse_numbers = numbers[::-1]  # срез с шагом -1 создаёт новый перевёрнутый список
print(reverse_numbers)  # печатаем перевёрнутый список


# ============================================================
# ЗАДАЧА 17: Срез "чётных" чисел по твоей логике (индексы 1,3,5...)
# ============================================================

numbers = [1,2,3,4,5,6,7,8,9,10]  # исходный список
even_numbers = numbers[1:10:2]  # берём элементы с индексами 1,3,5,7,9 (это НЕ “чётные числа”, а “чётные индексы” по твоей логике)
print(even_numbers)  # печать результата


# ============================================================
# ЗАДАЧА 18: Копия через срез + сортировка по убыванию
# ============================================================

nums = [3, 1, 4, 1, 5, 9, 2]  # исходный список
nums_copy = nums[:]  # копия через полный срез
nums_copy.sort(reverse=True)  # сортировка по убыванию (reverse=True)

print(nums)  # оригинал не менялся
print(nums_copy)  # копия отсортирована


# ============================================================
# ЗАДАЧА 19: Берём элементы с чётными индексами и сортируем по убыванию
# ============================================================

numbers = [5, 12, 7, 3, 9, 2, 10, 6]  # исходный список

numbers_copy = numbers[0:10:2]  # берём индексы 0,2,4,6 (верхняя граница 10 просто “с запасом”)
numbers_copy.sort(reverse=True)  # сортируем этот новый список по убыванию

print(numbers)  # печать оригинала
print(numbers_copy)  # печать результата


# ============================================================
# ЗАДАЧА 20: Таймер событий (вариант с логической ошибкой)
# ============================================================

if RUN_INPUT:
    allowed_events = ["deploy", "build", "test", "backup"]  # список разрешённых типов (но ниже он не используется правильно)
    event_type = input("Text please type of event: ")  # ввод типа события
    event_time = int(input("Text please duration time: "))  # ввод длительности в секундах

    if event_type:  # проверка только “не пустая ли строка” (НЕ проверяет что event_type в allowed_events)
        allowed_events  # это просто выражение, ничего не делает (логическая ошибка)
    else:
        print("Unknown event")  # если event_type пустой — печатаем ошибку

    if event_time < 0:  # проверяем что длительность не отрицательная
        print("Invalid duration")  # печатаем ошибку

    h = event_time // 3600  # целые часы
    m = (event_time % 3600) // 60  # минуты из остатка
    s = event_time % 60  # секунды

    print(f"Event {event_type}: {h}h {m}m {s}s")  # выводим форматированную строку


# ============================================================
# ЗАДАЧА 21: Таймер событий (вариант с проверками not in / elif)
# ============================================================

if RUN_INPUT:
    events = ["start", "stop", "restart"]  # разрешённые типы
    event_type = input("Text here please type of event: ")  # ввод типа
    event_time1 = int(input("Text please duration time: "))  # ввод длительности

    if event_type not in events:  # проверяем, есть ли тип в списке разрешённых
        print("Invalid type")  # если нет — ошибка
    elif event_time1 < 0:  # иначе проверяем длительность
        print("Invalid duration")  # ошибка
    else:
        h = event_time1 // 3600  # часы
        m = (event_time1 % 3600) // 60  # минуты
        s = event_time1 % 60  # секунды

        print(f"Event {event_type}: {h}h {m}m {s}s")  # вывод


# ============================================================
# ЗАДАЧА 22: Очистка пользователей + удаление дублей + сортировка
# ============================================================

raw_users = ["  Andrii ", "", "BORIS", "anna", "  ", "Boris", "ANNA"]  # “грязные” значения
clean_users = []  # сюда кладём очищенные имена

for r in raw_users:  # перебираем исходные строки
    name = r.strip().lower()  # чистим пробелы по краям и приводим к нижнему регистру
    if name:  # если после очистки строка не пустая
        clean_users.append(name)  # добавляем в чистый список

clean_users = list(set(clean_users))  # убираем дубли через set
clean_users.sort()  # сортируем по алфавиту
print(clean_users)  # печать результата


# ============================================================
# ЗАДАЧА 23: Очистка действий + удаление дублей + сортировка + печать
# ============================================================

raw_actions = ["  Login", "logout ", "LOGIN", "", "  ", "Logout", "login", "Delete"]  # “грязные” действия
clean_actions = []  # чистые действия

for r in raw_actions:  # перебираем исходные строки
    action = r.strip().lower()  # чистим и приводим к lower
    if action:  # если не пустая строка
        clean_actions.append(action)  # добавляем

clean_actions = list(set(clean_actions))  # удаляем дубли
clean_actions.sort()  # сортируем

for action in clean_actions:  # перебираем чистый отсортированный список
    print(action)  # печатаем каждое действие


# ============================================================
# ЗАДАЧА 24: Счётчик действий (dict)
# ============================================================

actions = [" Login", "logout ", "LOGIN", "update", "Logout", "", "login"]  # исходный список
clean_actions = []  # сюда сложим очищенные строки
result = {}  # словарь: действие -> количество

for action in actions:  # перебираем исходные строки
    action = action.strip().lower()  # чистим пробелы и приводим к lower
    if action:  # если не пустая строка
        clean_actions.append(action)  # добавляем в список чистых

for action in clean_actions:  # перебираем чистые действия
    if action in result:  # если ключ уже есть
        result[action] += 1  # увеличиваем счётчик
    else:
        result[action] = 1  # иначе создаём ключ со значением 1

print(result)  # печать словаря


# ============================================================
# ЗАДАЧА 25: FizzBuzz от 1 до N (проверка через try/except)
# ============================================================
if RUN_INPUT:
    while True:  # крутимся, пока не получим корректный ввод
        text = input("Введите число: ")  # ввод строкой

        try:
            text = int(text)  # пытаемся преобразовать к int
            if text <= 0:  # проверка диапазона
                print("Нужно число больше 0")  # сообщение
                continue  # снова просим ввод

            for t in range(1, text + 1):  # цикл от 1 до N включительно
                if t % 3 == 0 and t % 5 == 0:  # кратно 3 и 5
                    print("FizzBuzz")
                elif t % 3 == 0:  # кратно 3
                    print("Fizz")
                elif t % 5 == 0:  # кратно 5
                    print("Buzz")
                else:
                    print(t)  # иначе печатаем число

            break  # выходим из while после успешного выполнения

        except ValueError:  # если int() не смог преобразовать
            print("Это не число")  # сообщение и повтор ввода


# ============================================================
# ЗАДАЧА 26: while + match (match выполняется после цикла)
# ============================================================
if RUN_INPUT:
    while True:  # цикл ввода команд
        text = input("Enter please: ")  # ввод команды

        if not text:  # если пустая строка
            print("Empty info")  # сообщение
            continue  # просим ввод снова

        if text == "exit":  # если команда exit
            print("Good luck next time")  # прощание
            break  # выходим из while

    match text:  # match сработает ОДИН раз после выхода из цикла, по последнему text
        case "Yes":
            print("Accepted")
        case "No":
            print("Denied")
        case _:
            print("Undefined command")


# ============================================================
# ЗАДАЧА 27: Команды: exit / count (ввод числа c и печать 1..c)
# (ВНИМАНИЕ: в твоём коде тут есть логическая ошибка с отступами continue/break)
# ============================================================
if RUN_INPUT:
    while True:
        command = input("Enter command: ")

        if not command:
            print("Empty info")
        continue  # ОШИБКА: этот continue всегда срабатывает и не даёт дойти до exit/count

        if command == "exit":
            print("Good luck next time")
        break  # ОШИБКА: break стоит не в том месте (выйдет сразу, если дойдёт сюда)

        if command == "count":
            try:
                c = int(input("Enter please c: "))
                if c <= 0:
                    print("Need number > 0")
                continue  # ОШИБКА: continue стоит до цикла for, for не выполнится

                for i in range(1, c + 1):
                    print(i)

            except ValueError:
                print("Это не число")


# ============================================================
# ЗАДАЧА 28: Проверка баллов кандидата (True/False)
# ============================================================
if RUN_INPUT:
    is_next = None  # переменная под True/False
    num = int(input("Enter the number of points: "))  # ввод баллов

    if num >= 83:  # проходной порог
        is_next = True  # кандидат проходит
        print("Successful candidate")
    else:
        is_next = False  # кандидат не проходит
        print("Candidate is not valid")


# ============================================================
# ЗАДАЧА 29: Уровень разработчика по стажу (Junior/Middle/Senior)
# ============================================================
if RUN_INPUT:
    work_experience = int(input("Enter your full work experience in years: "))  # ввод стажа в годах
    developer_type = "Junior"  # значение по умолчанию

    if work_experience > 1 and work_experience < 6:  # 2..5 лет
        developer_type = "Middle"
        print(developer_type)
    elif work_experience == 0 or work_experience == 1:  # 0..1 год
        developer_type = "Junior"
        print(developer_type)
    else:  # 6+ лет (и также отрицательные, если введут — по твоей логике тоже сюда)
        developer_type = "Senior"
        print(developer_type)


# ============================================================
# ЗАДАЧА 30: Определить тип числа (positive odd/even, negative, zero)
# ============================================================
if RUN_INPUT:
    num = int(input("Enter a number: "))  # ввод числа

    if num > 0:  # положительное
        if num % 2 == 1:  # нечётное (остаток 1)
            result = "Positive odd number"
        if num % 2 == 0:  # чётное (остаток 0)
            result = "Positive even number"
    elif num < 0:  # отрицательное
        result = "Negative number"
    else:  # ноль
        result = "It is zero"


# ============================================================
# ЗАДАЧА 31: Сумма чисел от 1 до num (пока num <= 100)
# ============================================================
if RUN_INPUT:
    num = int(input("Enter the integer (0 to 100): "))  # ввод числа
    sum = 0  # накопитель суммы (лучше не называть sum, но ты назвал так)
    b = 0  # счётчик

    while b < num:  # пока счётчик меньше num
        if num <= 100:  # проверка ограничения
            b = b + 1  # увеличиваем b
            sum = sum + b  # добавляем b к сумме
            print(sum)  # печатаем текущую сумму на каждом шаге

        if num > 100:  # если num больше 100
            print("Incorrect number")
            break  # выходим из цикла


# ============================================================
# ЗАДАЧА 32: Подсчёт символа "r" в строке
# ============================================================

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."  # исходная строка
search = "r"  # что ищем
result = 0  # счётчик
symbol_r = search  # лишняя переменная (но не критично)

for symbol_r in message:  # перебираем каждый символ строки
    if symbol_r == search:  # сравниваем с искомым символом
        result = result + 1  # увеличиваем счётчик
print(result)  # выводим количество


# ============================================================
# ЗАДАЧА 33: Деление 1000 писем на количество рассылок (ловим деление на ноль)
# ============================================================
if RUN_INPUT:
    pool = 1000  # общее количество писем
    try:
        quantity = int(input("Enter the number of mailings: "))  # ввод количества рассылок
        chunk = pool // quantity  # целочисленное деление (сколько писем в одной рассылке)
        print(chunk)  # печать результата
    except ZeroDivisionError:  # если quantity == 0
        print('Divide by zero completed!')  # сообщение


# ============================================================
# ЗАДАЧА 34: Функция greeting() без параметров
# ============================================================

def greeting():  # объявляем функцию без аргументов
    print("Hello world!")  # печать внутри функции

greeting()  # вызов функции


# ============================================================
# ЗАДАЧА 35: Функция greet(name) -> строка "Hello name!"
# ============================================================

def greet(name: str) -> str:  # функция принимает строку и возвращает строку
    return f"Hello {name}!"  # возвращаем готовую строку

greeting = ()  # создаёшь переменную greeting как tuple (потом перезаписываешь)
greeting = greet("world")  # сохраняем результат вызова функции в переменную
print(greeting)  # печатаем результат


# ============================================================
# ЗАДАЧА 36: Приглашение на событие (invite_to_event)
# ============================================================

def invite_to_event(username: str) -> str:  # функция принимает имя пользователя
    return f"Dear {username}, we have the honour to invite you to our event"  # возвращает строку приглашения

invite = ()  # создаёшь переменную invite (tuple), потом перезаписываешь строкой
invite = invite_to_event("Vasya")  # получаем строку приглашения
print(invite)  # печать


# ============================================================
# ЗАДАЧА 37: Скидка (внутренняя функция + nonlocal)
# ============================================================

def discount_price(price: float, discount: float) -> float:  # цена и скидка (например 0.1 = 10%)
    def apply_discount():  # внутренняя функция
        nonlocal price  # разрешаем менять переменную price из внешней функции
        price = price * (1 - discount)  # пересчитываем цену со скидкой

    apply_discount()  # запускаем внутреннюю функцию, она меняет price
    return price  # возвращаем итоговую цену


# ============================================================
# ЗАДАЧА 38: ФИО с опциональным middle_name
# ============================================================

def get_fullname(first_name, last_name, middle_name=""):  # middle_name по умолчанию пустая строка
    if middle_name:  # если middle_name не пустой
       return (f"{first_name} {middle_name} {last_name}")  # три части
    else:
       return (f"{first_name} {last_name}")  # только имя и фамилия


# ============================================================
# ЗАДАЧА 39: Центровка строки пробелами до length
# ============================================================

def format_string(string, length):  # строка и целевая длина
    spaces = (length - len(string)) // 2  # сколько пробелов добавить слева (половина разницы)
    another_string = " " * spaces  # создаём строку из пробелов
    if len(string) >= length:  # если строка уже не короче
        return string  # возвращаем как есть
    if len(string) < length:  # если короче
        return another_string + string  # возвращаем строку с пробелами слева


# ============================================================
# ЗАДАЧА 40: *args и **kwargs (считаем количество аргументов)
# ============================================================

def first(size, *args):  # size — обычный аргумент, args — все позиционные “лишние” аргументы
    n = len(args)  # считаем, сколько дополнительных аргументов
    result = size + n  # складываем size и количество args
    return result  # возвращаем

print(first(5, "first", "second", "third"))  # args содержит 3 элемента -> 5+3
print(first(1, "Alex", "Boris"))  # args содержит 2 элемента -> 1+2


def second(size, **kwargs):  # kwargs — все именованные аргументы в виде словаря
    n = len(kwargs)  # количество ключей в kwargs
    result = size + n  # складываем size и количество kwargs
    return result  # возвращаем

print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # 3 kwargs -> 3+3
print(second(10, comment_one="Alex", comment_two="Boris"))  # 2 kwargs -> 10+2


# ============================================================
# ЗАДАЧА 41: Факториал + число сочетаний (комбинаторика)
# ============================================================

n = 50  # пример n
k = 7  # пример k

def factorial(n):  # рекурсивный факториал
    if n < 2:  # база: 0! и 1! = 1
        return 1
    else:
        return n * factorial(n - 1)  # рекурсия: n! = n * (n-1)!


def number_of_groups(n, k):  # комбинации C(n, k)
    if k > n:  # если выбираем больше, чем есть
        return 0
    if k < 0:  # отрицательные значения не подходят
        return 0
    if n < 0:
        return 0

    n_minus_k = n - k  # считаем n-k
    a = factorial(n)  # n!
    b = factorial(n_minus_k)  # (n-k)!
    c = factorial(k)  # k!
    result = a // (b * c)  # формула C(n,k) = n! / ((n-k)!*k!)
    return result  # возвращаем


# ============================================================
# ЗАДАЧА 42: Учёт покупок (ввод: name price quantity)
# словарь: name -> quantity
# total_sum: общая сумма денег по всем введённым строкам
# ============================================================
if RUN_INPUT:
    my_dict = {}  # словарь товаров: имя -> суммарное количество
    total_sum = 0  # сумма денег по всем товарам

    while True:
        line = input("Please, enter information: ").strip()  # ввод строки и чистка пробелов по краям

        if line == "help":  # команда help
            print("Please, enter first info as the name of product, second info as the float number and third number as the int number")
            continue

        elif line == "done":  # команда завершения
            break

        parts = line.split()  # делим строку на части по пробелам

        if len(parts) != 3:  # ожидаем ровно 3 части
            print("Invalid value")
            continue

        name = parts[0]  # название товара

        try:
            price = float(parts[1])  # цена -> float
        except ValueError:
            print("Invalid Format")
            continue

        if price <= 0:  # цена должна быть положительной
            continue

        try:
            quantity = int(parts[2])  # количество -> int
        except ValueError:
            print("Invalid Format")
            continue

        if quantity <= 0:  # количество должно быть положительным
            continue

        if name in my_dict:  # если товар уже есть в словаре
            my_dict[name] = my_dict[name] + quantity  # увеличиваем количество
        else:
            my_dict[name] = quantity  # создаём запись

        string_price = price * quantity  # стоимость этой позиции (цена * количество)
        total_sum = string_price + total_sum  # добавляем к общей сумме

        result = len(my_dict)  # количество уникальных товаров (количество ключей)

        print(total_sum)  # печатаем текущую сумму
        print(result)  # печатаем число уникальных товаров


# ============================================================
# ПРИМЕРЫ: Работа с датами (datetime/date/time)
# ============================================================

import datetime  # импортируем модуль datetime целиком (удобно писать datetime.datetime, datetime.date и т.д.)
now = datetime.datetime.now()  # текущая дата и время (datetime)
print(now)  # печать текущего datetime

##########################################################

from datetime import datetime  # импортируем только класс datetime

current_datetime = datetime.now()  # текущий datetime

print(current_datetime.year)  # год
print(current_datetime.month)  # месяц
print(current_datetime.day)  # день
print(current_datetime.hour)  # час
print(current_datetime.minute)  # минута
print(current_datetime.second)  # секунда
print(current_datetime.microsecond)  # микросекунды
print(current_datetime.tzinfo)  # информация о временной зоне (обычно None, если не задана)

##########################################################
from datetime import datetime  # снова импорт datetime

current_datetime = datetime.now()  # снова берём текущий datetime
print(current_datetime.date())  # достаём часть date (без времени)
print(current_datetime.time())  # достаём часть time (без даты)

##########################################################
import datetime  # снова импорт модуля

date_part = datetime.date(2023, 12, 14)  # создаём объект date (год, месяц, день)
time_part = datetime.time(12, 30, 15)  # создаём объект time (часы, минуты, секунды)

combined_datetime = datetime.datetime.combine(date_part, time_part)  # объединяем date+time в datetime

print(combined_datetime)  # печать объединённого datetime

##########################################################
import datetime  # импорт

specific_date = datetime.datetime(year=2020, month=1, day=7)  # создаём datetime с датой (время по умолчанию 00:00:00)
print(specific_date)  # печать

##########################################################
specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)  # datetime с датой и временем
print(specific_datetime)  # печать

##########################################################
import datetime  # импорт

specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)  # ещё раз тот же пример
print(specific_datetime)  # печать

##########################################################

from datetime import datetime  # импорт datetime

now = datetime.now()  # текущий datetime
day_of_week = now.weekday()  # номер дня недели: 0=пн ... 6=вс
print(f"Сьогодні: {day_of_week}")  # печать дня недели

##########################################################

from datetime import datetime  # импорт

datetime1 = datetime(2023, 3, 14, 12, 0)  # первый datetime
datetime2 = datetime(2023, 3, 15, 12, 0)  # второй datetime

print(datetime1 == datetime2)  # сравнение на равенство
print(datetime1 != datetime2)  # сравнение на неравенство
print(datetime1 < datetime2)   # “раньше”
print(datetime1 > datetime2)   # “позже”


# ============================================================
# ПРИМЕРЫ: Работа с промежутками timedelta
# ============================================================

from datetime import timedelta  # импорт timedelta

delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)  # создаём интервал времени из разных единиц
print(delta)  # печать итогового интервала (всё будет сведено к дням/секундам)

##########################################################

from datetime import datetime  # импорт

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)  # datetime 2019
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)  # datetime 2020

difference = seventh_day_2020 - seventh_day_2019  # разница двух datetime -> timedelta
print(difference)  # печать разницы
print(difference.total_seconds())  # печать разницы в секундах

##########################################################

from datetime import datetime, timedelta  # импорт

now = datetime.now()  # текущий datetime
future_date = now + timedelta(days=10)  # добавляем 10 дней
print(future_date)  # печать будущей даты

##########################################################

from datetime import datetime, timedelta  # импорт

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)  # опорная дата
four_weeks_interval = timedelta(weeks=4)  # интервал 4 недели

print(seventh_day_2020 + four_weeks_interval)  # добавляем интервал
print(seventh_day_2020 - four_weeks_interval)  # вычитаем интервал

##########################################################

from datetime import datetime  # импорт

date = datetime(year=2023, month=12, day=18)  # создаём datetime (время 00:00:00)
ordinal_number = date.toordinal()  # порядковый номер дня (для удобного подсчёта разницы)
print(f"Порядковий номер дати {date} становить {ordinal_number}")  # печать

##########################################################

from datetime import datetime  # импорт

napoleon_burns_moscow = datetime(year=1812, month=9, day=14)  # историческая дата
current_date = datetime.now()  # текущий datetime

days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()  # считаем разницу в днях через ordinal
print(days_since)  # печать


# ============================================================
# ПРИМЕРЫ: Работа с timestamp
# ============================================================

from datetime import datetime  # импорт

now = datetime.now()  # текущий datetime
timestamp = datetime.timestamp(now)  # переводим datetime в timestamp (секунды с 1970-01-01)
print(timestamp)  # печать timestamp

##########################################################

from datetime import datetime  # импорт

timestamp = 1617183600  # пример timestamp
dt_object = datetime.fromtimestamp(timestamp)  # переводим timestamp обратно в datetime
print(dt_object)  # печать datetime


# ============================================================
# ПРИМЕРЫ: Парсинг даты в строку (strftime/strptime)
# ============================================================

from datetime import datetime  # импорт

now = datetime.now()  # текущий datetime

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")  # форматируем дату+время в строку
print(formatted_date)

formatted_date_only = now.strftime("%A, %d %B %Y")  # форматируем только дату в “человекочитаемом” виде
print(formatted_date_only)

formatted_time_only = now.strftime("%I:%M %p")  # форматируем только время
print(formatted_time_only)

formatted_date_only = now.strftime("%d.%m.%Y")  # форматируем дату как dd.mm.yyyy
print(formatted_date_only)

##########################################################

from datetime import datetime  # импорт

date_string = "2023.03.14"  # строка с датой
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")  # парсим строку -> datetime по шаблону
print(datetime_object)  # печать


# ============================================================
# ПРИМЕРЫ: Работа с ISO форматом даты
# ============================================================

from datetime import datetime  # импорт

now = datetime.now()  # текущий datetime
iso_format = now.isoformat()  # переводим в ISO-строку
print(iso_format)  # печать

##########################################################

from datetime import datetime  # импорт

iso_date_string = "2023-03-14T12:39:29.992996"  # ISO-строка
date_from_iso = datetime.fromisoformat(iso_date_string)  # парсим ISO-строку -> datetime
print(date_from_iso)  # печать

##########################################################

from datetime import datetime  # импорт

now = datetime.now()  # текущий datetime
day_of_week = now.isoweekday()  # ISO-день недели: 1=пн ... 7=вс
print(f"Сьогодні: {day_of_week}")  # печать

##########################################################

from datetime import datetime  # импорт

now = datetime.now()  # текущий datetime
iso_calendar = now.isocalendar()  # получаем ISO-календарь: (ISO-год, ISO-неделя, ISO-день)
print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")  # печать


# ============================================================
# ПРИМЕРЫ: Работа с временными зонами (timezone)
# ============================================================

from datetime import datetime, timezone  # импорт

local_now = datetime.now()  # локальный datetime без tzinfo
utc_now = datetime.now(timezone.utc)  # datetime с tzinfo UTC

print(local_now)  # печать локального времени
print(utc_now)  # печать UTC

##########################################################

from datetime import datetime, timezone, timedelta  # импорт

utc_time = datetime.now(timezone.utc)  # текущее UTC-время

eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))  # переводим UTC во временную зону UTC-5
print(eastern_time)  # печать

##########################################################

from datetime import datetime, timezone, timedelta  # импорт

local_timezone = timezone(timedelta(hours=2))  # создаём tzinfo для UTC+2
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)  # datetime с tzinfo

utc_time = local_time.astimezone(timezone.utc)  # переводим локальное время в UTC
print(utc_time)  # печать

##########################################################

from datetime import datetime, timezone, timedelta  # импорт

timezone_offset = timezone(timedelta(hours=2))  # UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)  # datetime с tzinfo

iso_format_with_timezone = timezone_datetime.isoformat()  # ISO-строка, включает смещение
print(iso_format_with_timezone)  # печать


# ============================================================
# ПРИМЕРЫ: Работа со временем (time)
# ============================================================

import time  # импорт time

current_time = time.time()  # timestamp (секунды с 1970-01-01)
print(f"Поточний час: {current_time}")  # печать

##########################################################

import time  # импорт

print("Початок паузи")  # сообщение
time.sleep(1)  # пауза 1 секунда
print("Кінець паузи")  # сообщение

##########################################################

import time  # импорт

current_time = time.time()  # timestamp
print(f"Поточний час: {current_time}")

readable_time = time.ctime(current_time)  # переводим timestamp в строку “человеческого” вида
print(f"Читабельний час: {readable_time}")

##########################################################

import time  # импорт

current_time = time.time()  # timestamp
print(f"Поточний час: {current_time}")

local_time = time.localtime(current_time)  # структура времени в локальной зоне
print(f"Місцевий час: {local_time}")

##########################################################

import time  # импорт

start_time = time.perf_counter()  # высокоточный таймер начала

for _ in range(1_000_000):  # цикл “нагрузка”
    pass  # ничего не делаем

end_time = time.perf_counter()  # таймер конца

execution_time = end_time - start_time  # длительность выполнения
print(f"Час виконання: {execution_time} секунд")  # печать

##########################################################

a = 1_000_000  # подчёркивания в числе для читаемости
print(a)

b = 10_000_000  # 10 миллионов
print(b)

c = 1_000_000_000  # 1 миллиард
print(c)

#########################################
# ЗАДАЧА: Статус игр (owned/installed)
#########################################

games = [
    {"id": 101, "title": "Cyberpunk 2077"},  # игра 101
    {"id": 102, "title": "The Witcher 3"},   # игра 102
    {"id": 103, "title": "SWAT 4"},          # игра 103
    {"id": 104, "title": "Metro 2033"},      # игра 104
]

owned_ids = {102, 103}  # set купленных игр (быстрые проверки in)
installed_ids = {103}  # set установленных игр

for game in games:  # перебираем каталог игр
    if game["id"] in owned_ids:  # если игра куплена
        status = "INSTALL"  # базово предлагаем установить
        if game["id"] in installed_ids:  # если ещё и установлена
            status = "PLAY"  # можно играть
    else:
        status = "BUY"  # если не куплена — купить
    print(f'{game["title"]}: {status}')  # печатаем “название: статус”

#########################################
# ЗАДАЧА: Корзина игр (проверка наличия в каталоге)
#########################################

catalog = {
    101: "Cyberpunk 2077",  # id -> название
    102: "The Witcher 3",
    103: "SWAT 4",
}

cart_ids = [103, 999, 101, 103]  # корзина: список id (999 — отсутствует в каталоге)

for game_id in cart_ids:  # перебираем id из корзины
    if game_id in catalog:  # если id есть в каталоге (ключ существует)
        print(f"OK: {catalog[game_id]}")  # выводим название
    else:
        print(f"MISSING: {game_id}")  # выводим что id нет

#########################################
# ЗАДАЧА: Печать профиля (dict.items)
#########################################

profile = {
    "username": "andrewn",
    "email": "andrew@gmail.com",
    "age": 24,
    "country": "Ukraine"
}

for key, value in profile.items():  # items() даёт пары (ключ, значение)
     print(f"{key} : {value}")  # печать каждой пары


# ============================================================
# ДЗ: Дни рождения (подготовка + перенос с выходных)
# ============================================================

from datetime import datetime, timedelta, date  # импортируем нужные классы/функции

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},  # пользователь с датой строкой
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def find_next_weekday(start_date, weekday):  # ищем ближайший следующий weekday (0=пн ... 6=вс)
    current_weekday = start_date.weekday()  # день недели у start_date
    days_ahead = weekday - current_weekday  # сколько дней до нужного weekday
    if days_ahead <= 0:  # если сегодня уже этот день или позже — переносим на следующую неделю
        days_ahead = days_ahead + 7  # добавляем 7 дней

    return start_date + timedelta(days=days_ahead)  # возвращаем новую дату

def string_to_date(date_string):  # перевод строки даты в date
    date_obj = datetime.strptime(date_string, "%Y.%m.%d")  # парсим строку по формату
    date_obj.date()  # эта строка ничего не меняет (лишняя), т.к. ниже ты возвращаешь date()
    return date_obj.date()  # возвращаем именно date (без времени)

def prepare_user_list(user_data):  # превращаем список users со строками дат в список с date
    result = []  # сюда сложим пользователей в новом виде
    for user in user_data:  # перебираем исходные словари
        name = user["name"]  # берём имя
        birthday_date = string_to_date(user["birthday"])  # переводим строку даты в date
        result.append({"name": name, "birthday": birthday_date})  # добавляем новый словарь в результат
    return result  # возвращаем новый список

prepared_users = prepare_user_list(users)  # делаем подготовленный список (birthday уже date)
print(prepared_users)  # печатаем, чтобы проверить

def date_to_string(date):  # перевод date в строку
    date = datetime.strftime(date, "%Y.%m.%d")  # форматируем по шаблону YYYY.MM.DD
    return date  # возвращаем строку

def adjust_for_weekend(birthday):  # если ДР на выходных — переносим поздравление на понедельник
    day_of_date = birthday.weekday()  # номер дня недели у даты
    if day_of_date >= 5:  # 5=сб, 6=вс
       find_next_weekday(birthday, 0)  # лишняя строка (ничего не делает, результат не используется)
       return find_next_weekday(birthday, 0)  # возвращаем следующий понедельник
    else:
        return birthday  # если будний — возвращаем дату как есть

def get_upcoming_birthdays(users, days=7):  # возвращает список ближайших ДР на days дней вперёд
    upcoming_birthdays = []  # сюда складываем результат
    today = date.today()  # сегодняшняя дата
    for user in users:  # перебираем пользователей
        birthday_this_year = user["birthday"].replace(year=today.year)  # переносим дату ДР на текущий год
        if birthday_this_year < today:  # если ДР уже был в этом году
            birthday_this_year = user["birthday"].replace(year=today.year + 1)  # берём следующий год
        delta_days = (birthday_this_year - today).days  # считаем сколько дней осталось
        if delta_days in range(0, days + 1):  # если попадает в окно 0..days
            congratulation_date = adjust_for_weekend(birthday_this_year)  # переносим с выходных на рабочий день
            congratulation_date = congratulation_date.strftime("%Y.%m.%d")  # форматируем дату поздравления в строку
            new_dict = {"name": user["name"], "congratulation_date": congratulation_date}  # формируем итоговый словарь
            upcoming_birthdays.append(new_dict)  # добавляем в список результата
    return upcoming_birthdays  # возвращаем список


# ============================================================
# ДЗ 1: Даты — get_days_from_today
# ============================================================

from datetime import datetime  # импорт

date = "2020-10-09"  # строка даты (переменную лучше не называть date, но ты так назвал)

def get_days_from_today(date):  # функция считает разницу в днях от указанной даты до сегодня
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d")  # парсим строку по формату YYYY-MM-DD
    except ValueError:
        return  # если формат неверный — выходим без результата
    current_date = datetime.today()  # текущая дата-время
    days_count = current_date.toordinal() - formatted_date.toordinal()  # разница в днях через ordinal
    return days_count  # возвращаем число дней


# ============================================================
# ДЗ 2: Лотерея — get_numbers_ticket
# ============================================================

import random  # импорт генератора случайных чисел

def get_numbers_ticket(min, max, quantity):  # генерируем quantity уникальных чисел в диапазоне [min..max]
    if min < 1:  # проверка нижней границы
        return []
    if max > 1000:  # ограничение верхней границы по условию
        return []
    if min >= max:  # некорректный диапазон
        return []
    if quantity < 1:  # количество должно быть >= 1
        return []
    if quantity > (max - min + 1):  # нельзя взять уникальных чисел больше, чем размер диапазона
        return []
    numbers = set()  # set для уникальности
    while len(numbers) < quantity:  # пока не набрали нужное количество
        num = random.randint(min, max)  # случайное число из диапазона
        numbers.add(num)  # добавляем в set (повторы сами исчезают)
    lottery_numbers = list(numbers)  # переводим set в список
    lottery_numbers.sort()  # сортируем по возрастанию
    return lottery_numbers  # возвращаем готовый список


# ============================================================
# ДЗ 3: Номера — normalize_phone
# ============================================================

import re  # импорт регулярных выражений

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]  # список “грязных” номеров

def normalize_phone(phone_number):  # нормализуем номер к виду +380XXXXXXXXX
    pattern = r"[^\d\+]"  # шаблон: всё, что НЕ цифра и НЕ плюс
    replacement = ""  # заменяем на пустую строку
    clean = re.sub(pattern, replacement, phone_number)  # удаляем пробелы, скобки, дефисы, табы, переносы и т.д.
    if clean.startswith("+380"):  # если уже начинается с +380 — возвращаем как есть
        return clean
    if clean.startswith("380"):  # если начинается с 380 — добавляем плюс
        return "+" + clean
    if clean.startswith("0"):  # если начинается с 0 — добавляем +38
        return "+38" + clean
    else:
        return clean  # иначе возвращаем как получилось (на случай нестандартного формата)

# ============================================================
# ДЗ 3: Обнова для выхода патча
# ============================================================

import re
from datetime import datetime, timedelta, timezone

# --- Настройки времени пользователя ---
USER_TZ_OFFSET_HOURS = 2  # Киев, UTC+2

# Последнее время проверки (строка ISO без таймзоны)
LAST_CHECK_ISO = "2026-02-07T10:15:00"

# Превращаем строку в datetime-объект
DATETIME_LAST_CHECK_ISO = datetime.fromisoformat(LAST_CHECK_ISO)

# Интервал проверки в минутах
CHECK_EVERY_MINUTES = 45

# Считаем время следующей проверки
NEXT_TIME_CHECK = DATETIME_LAST_CHECK_ISO + timedelta(minutes=CHECK_EVERY_MINUTES)

# Берём только "время" (часы:минуты:секунды) из datetime
ONLY_TIME = NEXT_TIME_CHECK.time()

# Окно патча (строки времени)
PATCH_WINDOW_START = "01:00"
PATCH_WINDOW_END = "05:00"

# Превращаем строки времени в time-объекты, чтобы их сравнивать
DATE_TIME_PATCH_WINDOW_START = datetime.strptime(PATCH_WINDOW_START, "%H:%M").time()
DATE_TIME_PATCH_WINDOW_END = datetime.strptime(PATCH_WINDOW_END, "%H:%M").time()

# Проверяем, попадает ли время следующей проверки в окно патча
if DATE_TIME_PATCH_WINDOW_START <= ONLY_TIME <= DATE_TIME_PATCH_WINDOW_END:
    print("Patch has been released")

# Форматируем NEXT_TIME_CHECK в читаемую строку
FORMATTED_NEXT_TIME_CHECK = NEXT_TIME_CHECK.strftime("%Y-%m-%d %H:%M:%S")

# Создаём таймзону пользователя UTC+2
LOCAL_TIMEZONE = timezone(timedelta(hours=USER_TZ_OFFSET_HOURS))

# "Приклеиваем" таймзону к NEXT_TIME_CHECK (делаем datetime aware)
LOCAL_TIME = NEXT_TIME_CHECK.replace(tzinfo=LOCAL_TIMEZONE)

# Переводим локальное время в UTC
UTC_time = LOCAL_TIME.astimezone(timezone.utc)

# Печатаем UTC-время и отформатированное локальное
print(UTC_time)
print(FORMATTED_NEXT_TIME_CHECK)

# --- Лог (многострочный текст) ---
LOG_TEXT = """
[2026.02.07 10:15:04] ping=42ms fps=118.6 user=andrewnedoshivkin
[2026.02.07 10:16:10] ping=55ms fps=101.2 user=andrewnedoshivkin
[2026.02.07 10:17:00] ping=39ms fps=abc user=andrewnedoshivkin
"""

# --- Паттерны для регулярных выражений ---
# Дата и время вида 2026.02.07 10:15:04
pattern_date = r"(\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2})"

# ping вида ping=42ms (захватываем число отдельно)
pattern_ping = r"ping=(\d+)ms"

# fps вида fps=118.6 или fps=101 (захватываем число отдельно)
pattern_fps = r"fps=(\d+(?:\.\d+)?)"

# --- Аккумуляторы (списки) ---
list_date = []
list_fps = []
list_ping = []

# Режем лог на строки
LOG_TEXT_SPLITTED = LOG_TEXT.split("\n")

# Проходим по каждой строке лога
for element in LOG_TEXT_SPLITTED:
    # Пропускаем пустые строки (из-за тройных кавычек)
    if not element.strip():
        continue

    # Ищем дату
    match_date = re.search(pattern_date, element)
    if not match_date:
        continue

    # Ищем fps
    match_fps = re.search(pattern_fps, element)
    if not match_fps:
        continue

    # Ищем ping
    match_ping = re.search(pattern_ping, element)
    if not match_ping:
        continue

    # Берём строку даты (группа 1)
    result_match_date = match_date.group(1)

    # Берём fps-число как строку (группа 1)
    result_match_fps = match_fps.group(1)

    # Берём ping-число как строку (группа 1)
    result_match_ping = match_ping.group(1)

    try:
        # Переводим fps в float
        normalized_fps = float(result_match_fps)

        # Переводим ping в int
        normalized_ping = int(result_match_ping)

        # Переводим строку даты в datetime
        date_obj = datetime.strptime(result_match_date, "%Y.%m.%d %H:%M:%S")
    except ValueError:
        # Если не получилось конвертировать (например fps=abc) — пропускаем строку
        continue

    # Добавляем в аккумуляторы
    list_date.append(date_obj)
    list_fps.append(normalized_fps)
    list_ping.append(normalized_ping)

# --- Средние значения ---
# Защита от пустых списков
if list_fps:
    sum_fps = 0
    for s in list_fps:
        sum_fps += s
    average_fps = sum_fps / len(list_fps)
else:
    average_fps = None

if list_ping:
    sum_ping = 0
    for p in list_ping:
        sum_ping += p
    average_ping = sum_ping / len(list_ping)
else:
    average_ping = None

# Печать результатов (по желанию)
print("records:", len(list_date))
print("avg_fps:", average_fps)
print("avg_ping:", average_ping)