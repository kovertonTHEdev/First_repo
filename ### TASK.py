RUN_INPUT = False  # флаг: если True — участки с input() выполняются, если False — пропускаются


# ============================================================
# ЗАДАЧА 1: Склейка имени и фамилии
# ============================================================

first_name = "Andrii"  # создаём переменную-строку с именем
last_name = "Nedoshivkin"  # создаём переменную-строку с фамилией
full_name = first_name + " " + last_name  # склеиваем 3 строки: имя + пробел + фамилия

print(full_name)  # печатаем результат склейки в консоль


# ============================================================
# ЗАДАЧА 2: Площадь комнаты (числа как float)
# ============================================================

length = 2.75  # задаём длину как число float (с дробной частью)
width = 1.75  # задаём ширину как число float
area = length * width  # считаем площадь умножением (float * float)

show = (f"With width {width} and length {length} of the room, its area is equal to {area}")
# создаём строку (f-string), куда подставляются переменные width, length, area


# ============================================================
# ЗАДАЧА 3: Площадь комнаты (числа как строки -> перевод в float)
# ============================================================

length = "2.75"  # задаём длину как строку (не число)
width = "1.75"  # задаём ширину как строку
area = float(length) * float(width)  # переводим строки в float и умножаем

show = (f"With width {width} and length {length} of the room, its area is equal to {area}")
# снова создаём строку с подстановкой значений


# ============================================================
# ЗАДАЧА 4: Площадь комнаты (ввод от пользователя)
# ============================================================

if RUN_INPUT:  # условие: выполняем блок только если RUN_INPUT == True
    length = float(input("Enter length size"))  # берём ввод строкой -> переводим в float
    width = float(input("Enter width size"))  # берём ввод строкой -> переводим в float
    area = length * width  # считаем площадь
    print(area)  # выводим площадь на экран


# ============================================================
# ЗАДАЧА 5: Работа со списком (extend, insert, reverse)
# ============================================================

my_list = [2024, 3.12]  # создаём список с двумя элементами: int и float
some_data = ["Python"]  # создаём второй список с одной строкой

my_list.extend(some_data)  # добавляем элементы some_data в конец my_list (расширяем список)

my_list.insert(1, "Python")  # вставляем строку "Python" в my_list на индекс 1

my_list.reverse()  # переворачиваем порядок элементов списка my_list “на месте”


# ============================================================
# ЗАДАЧА 6: Проверка возраста (if/else)
# ============================================================

if RUN_INPUT:  # выполняем блок только если RUN_INPUT == True
    age_input = int(input("\nPlease, Enter your age: "))  # ввод -> строка, int() -> число

    if age_input < 18:  # проверка: возраст меньше 18?
        print("Acess Denied")  # печатаем запрет
    else:  # иначе (18 и больше)
        print("Access Granted")  # печатаем разрешение


# ============================================================
# ЗАДАЧА 7: Сортировка чисел, введённых пользователем (split + append + sorted)
# ============================================================

if RUN_INPUT:  # включаем ввод только при RUN_INPUT == True
    nums = input("Please, enter numbers: ")  # ввод одной строкой, например "5 2 9"
    nums = nums.split()  # делим строку по пробелам -> получаем список строк

    numbers = []  # создаём пустой список, куда будем класть числа int

    for n in nums:  # перебираем каждый элемент списка nums (это строки)
        numbers.append(int(n))  # переводим строку в int и добавляем в numbers

    sorted_nums = sorted(numbers)  # создаём новый отсортированный список (оригинал numbers не меняется)
    print(sorted_nums)  # печатаем отсортированный список


# ============================================================
# ЗАДАЧА 8: Сортировка списка на месте (sort)
# ============================================================

nums = [5, 2, 9, 1, 3]  # создаём список чисел
nums.sort()  # сортируем сам список nums “на месте”
print(nums)  # печатаем список после сортировки


# ============================================================
# ЗАДАЧА 9: Копия списка + сортировка копии
# ============================================================

nums = [5, 2, 9, 1, 3]  # исходный список
nums_copy = nums.copy()  # создаём отдельную копию списка
nums_copy.sort()  # сортируем копию

print(nums)  # печатаем оригинал (он не изменился)
print(nums_copy)  # печатаем копию (она отсортирована)


# ============================================================
# ЗАДАЧА 10: Сортировка по длине слова (key=len)
# ============================================================

words = ["banana", "Apple", "cherry"]  # список строк
words.sort(key=len)  # сортируем список по длине каждой строки (len)
print(words)  # печатаем результат


# ============================================================
# ЗАДАЧА 11: Очистка слов (strip + lower) и сортировка
# ============================================================

words = ["  Banana", "apple  ", "  Cherry ", "apple"]  # список слов с пробелами/регистром

clean_words = []  # пустой список под очищенные слова

for w in words:  # перебираем каждое слово из исходного списка
    clean_words.append(w.strip().lower())  # strip убирает пробелы по краям, lower -> нижний регистр

clean_words.sort()  # сортируем список clean_words по алфавиту
print(clean_words)  # печатаем итог


# ============================================================
# ЗАДАЧА 12: Подсчёт, сколько раз встречается слово "apple" (count)
# ============================================================

words = ["Apple", "banana", "apple", "Cherry", "banana"]  # исходный список слов
good_words = []  # сюда положим очищенные и приведённые к lower слова

for w in words:  # перебираем исходные слова
    good_words.append(w.strip().lower())  # приводим к нормальному виду и добавляем

good_words.sort()  # сортируем список
count_apple = good_words.count("apple")  # считаем количество вхождений строки "apple" в списке

print(good_words)  # печатаем очищенный список
print(count_apple)  # печатаем число повторов


# ============================================================
# ЗАДАЧА 13: Удаление дублей через set (слова)
# ============================================================

words = ["apple", "banana", "apple", "cherry", "banana"]  # список с повторами

d_words = set(words)  # превращаем список в set: повторы исчезают
words = list(d_words)  # превращаем set обратно в list

print(words)  # печатаем список без дублей (порядок может быть случайным)


# ============================================================
# ЗАДАЧА 14: Подсчёт слов через словарь (dict + get)
# ============================================================

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]  # список слов
result = {}  # создаём пустой словарь: ключ=слово, значение=сколько раз встречалось

for w in words:  # перебираем каждое слово
    current = result.get(w, 0)  # берём текущее значение по ключу w; если ключа нет -> 0
    result[w] = current + 1  # записываем обратно увеличенный счётчик

print(result)  # печатаем словарь (слово -> количество)


# ============================================================
# ЗАДАЧА 15: Удаление дублей в числах и сортировка
# ============================================================

nums = [3, 1, 4, 1, 5, 9, 2, 3]  # список с повторами

nums = list(set(nums))  # убираем повторы через set и возвращаем обратно в list
nums.sort()  # сортируем список по возрастанию
print(nums)  # печать результата


# ============================================================
# ЗАДАЧА 16: Разворот списка через срез [::-1]
# ============================================================

numbers = [1,2,3,4,5,6,7,8,9,10]  # исходный список
reverse_numbers = numbers[::-1]  # создаём новый список в обратном порядке
print(reverse_numbers)  # печатаем перевёрнутый список


# ============================================================
# ЗАДАЧА 17: Срез "чётных" чисел по твоей логике (индексы 1,3,5...)
# ============================================================

numbers = [1,2,3,4,5,6,7,8,9,10]  # исходный список
even_numbers = numbers[1:10:2]  # берём элементы начиная с индекса 1, до 10, шаг 2
print(even_numbers)  # печать результата


# ============================================================
# ЗАДАЧА 18: Копия через срез + сортировка по убыванию
# ============================================================

nums = [3, 1, 4, 1, 5, 9, 2]  # исходный список
nums_copy = nums[:]  # делаем копию списка через срез
nums_copy.sort(reverse=True)  # сортируем копию по убыванию (reverse=True)

print(nums)  # печатаем исходный
print(nums_copy)  # печатаем обработанный


# ============================================================
# ЗАДАЧА 19: Берём элементы с чётными индексами и сортируем по убыванию
# ============================================================

numbers = [5, 12, 7, 3, 9, 2, 10, 6]  # исходный список

numbers_copy = numbers[0:10:2]  # берём элементы по индексам 0,2,4,6...
numbers_copy.sort(reverse=True)  # сортируем этот новый список по убыванию

print(numbers)  # печать оригинала
print(numbers_copy)  # печать результата


# ============================================================
# ЗАДАЧА 20: Таймер событий (вариант с логической ошибкой)
# ============================================================

if RUN_INPUT:  # блок выполняется только при RUN_INPUT == True
    allowed_events = ["deploy", "build", "test", "backup"]  # список разрешённых событий
    event_type = input("Text please type of event: ")  # ввод типа события
    event_time = int(input("Text please duration time: "))  # ввод времени, перевод в int

    if event_type:  # проверка “не пустая ли строка” (НЕ проверяет allowed_events)
        allowed_events  # просто выражение, ничего не делает
    else:
        print("Unknown event")  # если строка пустая — печать “Unknown event”

    if event_time < 0:  # проверка, что время не отрицательное
        print("Invalid duration")  # сообщение об ошибке

    h = event_time // 3600  # целые часы (деление без остатка)
    m = (event_time % 3600) // 60  # минуты: остаток после часов делим на 60
    s = event_time % 60  # секунды: остаток после деления на 60

    print(f"Event {event_type}: {h}h {m}m {s}s")  # печать результата в формате


# ============================================================
# ЗАДАЧА 21: Таймер событий (вариант с проверками not in / elif)
# ============================================================

if RUN_INPUT:  # выполняем блок только при RUN_INPUT == True
    events = ["start", "stop", "restart"]  # список разрешённых типов
    event_type = input("Text here please type of event: ")  # ввод типа
    event_time1 = int(input("Text please duration time: "))  # ввод длительности, int

    if event_type not in events:  # проверяем, что введённый тип есть в списке events
        print("Invalid type")  # если нет — печать ошибки
    elif event_time1 < 0:  # иначе проверяем, что время не отрицательное
        print("Invalid duration")  # если отрицательное — печать ошибки
    else:
        h = event_time1 // 3600  # считаем часы
        m = (event_time1 % 3600) // 60  # считаем минуты
        s = event_time1 % 60  # считаем секунды

        print(f"Event {event_type}: {h}h {m}m {s}s")  # печать “тип + время”


# ============================================================
# ЗАДАЧА 22: Очистка пользователей + удаление дублей + сортировка
# ============================================================

raw_users = ["  Andrii ", "", "BORIS", "anna", "  ", "Boris", "ANNA"]  # “грязный” список пользователей
clean_users = []  # список для чистых имён

for r in raw_users:  # перебираем каждый элемент
    name = r.strip().lower()  # убираем пробелы по краям и приводим к нижнему регистру
    if name:  # если строка не пустая (не "")
        clean_users.append(name)  # добавляем её в clean_users

clean_users = list(set(clean_users))  # убираем дубли через set и возвращаем обратно в list
clean_users.sort()  # сортируем по алфавиту
print(clean_users)  # печатаем список


# ============================================================
# ЗАДАЧА 23: Очистка действий + удаление дублей + сортировка + печать
# ============================================================

raw_actions = ["  Login", "logout ", "LOGIN", "", "  ", "Logout", "login", "Delete"]  # “грязные” действия
clean_actions = []  # список для чистых действий

for r in raw_actions:  # перебираем каждое действие
    action = r.strip().lower()  # strip убирает пробелы, lower -> нижний регистр
    if action:  # если действие не пустое
        clean_actions.append(action)  # добавляем в clean_actions

clean_actions = list(set(clean_actions))  # убираем повторяющиеся действия
clean_actions.sort()  # сортируем список

for action in clean_actions:  # перебираем уже чистые действия
    print(action)  # печатаем каждое действие отдельной строкой


# ============================================================
# ЗАДАЧА 24: Счётчик действий (dict)
# ============================================================

actions = [" Login", "logout ", "LOGIN", "update", "Logout", "", "login"]  # исходные действия
clean_actions = []  # список под чистые действия
result = {}  # словарь: действие -> сколько раз встречалось

for action in actions:  # перебираем исходные элементы
    action = action.strip().lower()  # очищаем и приводим к lower
    if action:  # если не пусто
        clean_actions.append(action)  # добавляем в список чистых

for action in clean_actions:  # перебираем чистые действия
    if action in result:  # если ключ уже есть в словаре
        result[action] += 1  # увеличиваем счётчик на 1
    else:
        result[action] = 1  # если ключа не было — создаём с значением 1

print(result)  # печатаем словарь подсчёта


# ============================================================
# ЗАДАЧА 25: FizzBuzz от 1 до N (проверка через try/except)
# ============================================================
if RUN_INPUT:
    while True:  # бесконечный цикл, пока не сделаем break
        text = input("Введите число: ")  # вводим строку

        try:
            text = int(text)  # пытаемся превратить строку в int
            if text <= 0:  # проверяем, что число > 0
                print("Нужно число больше 0")  # сообщение об ошибке
                continue  # просим ввод снова (переход к новой итерации)

            for t in range(1, text + 1):  # цикл от 1 до N включительно
                if t % 3 == 0 and t % 5 == 0:  # кратно и 3, и 5
                    print("FizzBuzz")  # печать FizzBuzz
                elif t % 3 == 0:  # кратно 3
                    print("Fizz")  # печать Fizz
                elif t % 5 == 0:  # кратно 5
                    print("Buzz")  # печать Buzz
                else:
                    print(t)  # иначе печатаем само число

            break  # выходим из while после успешного выполнения

        except ValueError:  # если int(text) не получилось
            print("Это не число")  # печатаем сообщение и цикл продолжается


# ============================================================
# ЗАДАЧА 26: while + match (match выполняется после цикла)
# ============================================================
if RUN_INPUT: 
    while True:  # цикл команд
        text = input("Enter please: ")  # ввод строки

        if not text:  # если строка пустая
            print("Empty info")  # сообщение
            continue  # просим ввод снова

        if text == "exit":  # если команда exit
            print("Good luck next time")  # прощание
            break  # выходим из цикла

    match text:  # match запускается ОДИН раз после выхода из while, для последнего text
        case "Yes":
            print("Accepted")  # если text == "Yes"
        case "No":
            print("Denied")  # если text == "No"
        case _:
            print("Undefined command")  # иначе


# ============================================================
# ЗАДАЧА 27: Команды: exit / count (ввод числа c и печать 1..c)
# ============================================================
if RUN_INPUT: 
    while True:  # бесконечный цикл команд
        command = input("Enter command: ")  # ввод команды

        if not command:  # если пусто
            print("Empty info")  # сообщение
        continue  # запрос снова

        if command == "exit":  # если exit
            print("Good luck next time")  # прощание
        break  # выходим

        if command == "count":  # если count
            try:
                c = int(input("Enter please c: "))  # ввод числа, перевод в int
                if c <= 0:  # проверка что > 0
                    print("Need number > 0")  # сообщение
                continue  # возвращаемся к вводу команды

                for i in range(1, c + 1):  # печатаем 1..c
                    print(i)

            except ValueError:  # если int() не смог
                print("Это не число")  # сообщение


# ============================================================
# ЗАДАЧА 28: Проверка баллов кандидата (True/False)
# ============================================================
if RUN_INPUT: 
    is_next = None  # переменная-плейсхолдер, потом станет True или False
    num = int(input("Enter the number of points: "))  # ввод баллов -> int

    if num >= 83:  # если баллов 83 или больше
        is_next = True  # кандидат проходит дальше
        print("Successful candidate")  # сообщение
    else:
        is_next = False  # кандидат не проходит
        print("Candidate is not valid")  # сообщение


# ============================================================
# ЗАДАЧА 29: Уровень разработчика по стажу (Junior/Middle/Senior)
# ============================================================
if RUN_INPUT: 
    work_experience = int(input("Enter your full work experience in years: "))  # ввод стажа
    developer_type = "Junior"  # значение по умолчанию

    if work_experience > 1 and work_experience < 6:  # стаж от 2 до 5
        developer_type = "Middle"  # присваиваем Middle
        print(developer_type)  # печатаем результат
    elif work_experience == 0 or work_experience == 1:  # стаж 0 или 1
        developer_type = "Junior"  # присваиваем Junior
        print(developer_type)  # печатаем
    else:  # иначе (6+)
        developer_type = "Senior"  # присваиваем Senior
        print(developer_type)  # печатаем


# ============================================================
# ЗАДАЧА 30: Определить тип числа (positive odd/even, negative, zero)
# ============================================================
if RUN_INPUT: 
    num = int(input("Enter a number: "))  # ввод числа -> int

    if num > 0:  # если положительное
        if num % 2 == 1:  # если остаток 1 -> нечётное
            result = "Positive odd number"  # строка-результат
        if num % 2 == 0:  # если остаток 0 -> чётное
            result = "Positive even number"  # строка-результат
    elif num < 0:  # если отрицательное
        result = "Negative number"  # строка-результат
    else:  # иначе (0)
        result = "It is zero"  # строка-результат


# ============================================================
# ЗАДАЧА 31: Сумма чисел от 1 до num (пока num <= 100)
# ============================================================
if RUN_INPUT: 
    num = int(input("Enter the integer (0 to 100): "))  # ввод числа
    sum = 0  # переменная для накопления суммы
    b = 0  # счётчик

    while b < num:  # цикл пока b меньше num
        if num <= 100:  # проверка, что num в пределах
            b = b + 1  # увеличиваем b на 1
            sum = sum + b  # добавляем b к сумме
            print(sum)  # печатаем текущую сумму на каждом шаге

        if num > 100:  # если num больше 100
            print("Incorrect number")  # ошибка
            break  # выходим из цикла


# ============================================================
# ЗАДАЧА 32: Подсчёт символа "r" в строке
# ============================================================

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"  # какой символ ищем
result = 0  # счётчик найденных символов
symbol_r = search  # лишняя переменная (но ты её создал)

for symbol_r in message:  # перебираем каждый символ строки message
    if symbol_r == search:  # если текущий символ равен "r"
        result = result + 1  # увеличиваем счётчик
print(result)  # печатаем сколько раз встретился "r"


# ============================================================
# ЗАДАЧА 33: Деление 1000 писем на количество рассылок (ловим деление на ноль)
# ============================================================
if RUN_INPUT: 
    pool = 1000  # общий пул
    try:
        quantity = int(input("Enter the number of mailings: "))  # ввод количества рассылок
        chunk = pool // quantity  # целочисленное деление: сколько в каждой рассылке
        print(chunk)  # печать результата
    except ZeroDivisionError:  # если quantity == 0
        print('Divide by zero completed!')  # сообщение


# ============================================================
# ЗАДАЧА 34: Функция greeting() без параметров
# ============================================================

def greeting():  # объявляем функцию без аргументов
    print("Hello world!")  # функция печатает строку

greeting()  # вызываем функцию


# ============================================================
# ЗАДАЧА 35: Функция greet(name) -> строка "Hello name!"
# ============================================================

def greet(name: str) -> str:  # функция принимает name (строка) и возвращает строку
    return f"Hello {name}!"  # возвращаем f-string

greeting = ()  # создаёшь переменную greeting и кладёшь туда пустой tuple ()
greeting = greet("world")  # перезаписываешь greeting строкой, которую вернул greet()
print(greeting)  # печатаешь строку


# ============================================================
# ЗАДАЧА 36: Приглашение на событие (invite_to_event)
# ============================================================

def invite_to_event(username: str) -> str:  # функция принимает имя пользователя
    return f"Dear {username}, we have the honour to invite you to our event"  # возвращает строку

invite = ()  # создаёшь переменную invite как пустой tuple ()
invite = invite_to_event("Vasya")  # перезаписываешь invite строкой
print(invite)  # печатаешь приглашение


# ============================================================
# ЗАДАЧА 37: Скидка (внутренняя функция + nonlocal)
# ============================================================

def discount_price(price: float, discount: float) -> float:  # функция получает цену и скидку
    def apply_discount():  # внутренняя функция
        nonlocal price  # говорим: будем менять переменную price из внешней функции
        price = price * (1 - discount)  # изменяем price с учётом скидки

    apply_discount()  # вызываем внутреннюю функцию (она меняет price)
    return price  # возвращаем финальную цену


# ============================================================
# ЗАДАЧА 38: ФИО с опциональным middle_name
# ============================================================

def get_fullname(first_name, last_name, middle_name =""):  # middle_name по умолчанию пустая строка
    if middle_name:  # если middle_name НЕ пустой
       return(f"{first_name} {middle_name} {last_name}")  # возвращаем 3 части
    else:
       return(f"{first_name} {last_name}")  # возвращаем только имя+фамилия


# ============================================================
# ЗАДАЧА 39: Центровка строки пробелами до length
# ============================================================

def format_string(string, length):  # функция принимает строку и желаемую длину
    spaces = (length - len(string)) // 2  # сколько пробелов добавить слева (половина разницы)
    another_string = " " * spaces  # создаём строку из пробелов нужной длины
    if len(string) >= length:  # если строка уже длинная
        return string  # возвращаем как есть
    if len(string) < length:  # если строка короче
        return another_string + string  # возвращаем строку с пробелами слева


# ============================================================
# ЗАДАЧА 40: *args и **kwargs (считаем количество аргументов)
# ============================================================

def first(size, *args):  # size — обычный аргумент, args — всё остальное в виде tuple
    n = len(args)  # считаем, сколько элементов в args
    result = size + n  # складываем size и количество args
    return result  # возвращаем результат

print(first(5, "first", "second", "third"))  # вызываем first с 3 доп. аргументами
print(first(1, "Alex", "Boris"))  # вызываем first с 2 доп. аргументами


def second(size, **kwargs):  # kwargs — все именованные аргументы в виде dict
    n = len(kwargs)  # считаем, сколько ключей в kwargs
    result = size + n  # складываем size и количество kwargs
    return result  # возвращаем результат

print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # 3 kwargs
print(second(10, comment_one="Alex", comment_two="Boris"))  # 2 kwargs


# ============================================================
# ЗАДАЧА 41: Факториал + число сочетаний (комбинаторика)
# ============================================================

n = 50  # число n (как пример)
k = 7  # число k (как пример)

def factorial(n):  # функция факториала
    if n < 2:  # база рекурсии: 0! и 1! = 1
        return 1
    else:
        return n * factorial(n - 1)  # рекурсивный шаг: n! = n * (n-1)!


def number_of_groups(n, k):  # считаем C(n, k)
    if k > n:  # если k больше n — комбинаций нет
        return 0
    if k < 0:  # отрицательное k — некорректно
        return 0
    if n < 0:  # отрицательное n — некорректно
        return 0

    n_minus_k  = n - k  # считаем n-k
    a = factorial(n)  # a = n!
    b = factorial(n_minus_k)  # b = (n-k)!
    c = factorial(k)  # c = k!
    result = a // (b * c)  # C(n,k) = n! / ((n-k)! * k!) (целочисленно)
    return result  # возвращаем результат


# ============================================================
# ЗАДАЧА 42: Учёт покупок (ввод: name price quantity)
# словарь: name -> quantity
# total_sum: общая сумма денег по всем введённым строкам
# ============================================================
if RUN_INPUT: 
    my_dict = {}  # создаём пустой словарь для хранения количества по товарам
    total_sum = 0  # создаём переменную для накопления общей суммы денег

    while True:  # бесконечный цикл ввода строк
        line = input("Please, enter information: ").strip()  # ввод строки + убираем пробелы по краям

        if line == "help":  # если команда help
            print("Please, enter first info as the name of product, second info as the float number and third number as the int number")
            continue  # возвращаемся в начало цикла (просим ввод снова)

        elif line == "done":  # если команда done
            break  # выходим из цикла

        parts = line.split()  # делим строку по пробелам -> список частей

        if len(parts) != 3:  # если частей не ровно 3
            print("Invalid value")  # сообщение об ошибке формата
            continue  # просим ввод снова

        name = parts[0]  # берём имя товара (строка)

        try:
            price = float(parts[1])  # пытаемся перевести цену в float
        except ValueError:
            print("Invalid Format")  # если не получилось — значит не число
            continue  # просим ввод снова

        if price <= 0:  # если цена ноль или отрицательная
            continue  # пропускаем эту строку и просим ввод снова

        try:
            quantity = int(parts[2])  # пытаемся перевести количество в int
        except ValueError:
            print("Invalid Format")  # если не получилось — значит не число
            continue  # просим ввод снова

        if quantity <= 0:  # если количество ноль или отрицательное
            continue  # пропускаем эту строку

        if name in my_dict:  # если такой товар уже есть в словаре
            my_dict[name] = my_dict[name] + quantity  # увеличиваем количество в словаре
        else:
            my_dict[name] = quantity  # если товара не было — создаём запись

        string_price = price * quantity  # считаем стоимость этой строки (цена * количество)
        total_sum = string_price + total_sum  # добавляем стоимость строки к общей сумме

        result = len(my_dict)  # считаем количество уникальных товаров (ключей) в словаре

        print(total_sum)  # печатаем текущую общую сумму
        print(result)  # печатаем количество уникальных товаров


# ============================================================
# Примеры: Работа с датами 
# ============================================================

import datetime
now = datetime.datetime.now()
print(now)
##########################################################


from datetime import datetime

current_datetime = datetime.now()

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)

##########################################################
from datetime import datetime

current_datetime = datetime.now()
print(current_datetime.date())
print(current_datetime.time())

##########################################################
import datetime

# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)


print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

##########################################################
import datetime

# Створення об'єкта datetime з конкретною датою
specific_date = datetime.datetime(year=2020, month=1, day=7)

print(specific_date)  # Виведе "2020-01-07 00:00:00"

##########################################################
specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

##########################################################
import datetime

# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"


##########################################################

from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання номера дня тижня
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")  

##########################################################

from datetime import datetime

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

# ============================================================
# Примеры: Работа с промежутками timedelta
# ============================================================

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)

##########################################################

from datetime import datetime

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0

##########################################################

from datetime import datetime, timedelta

now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date)

##########################################################

from datetime import datetime, timedelta

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

##########################################################

from datetime import datetime

# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)

# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")

##########################################################

from datetime import datetime

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)

# ============================================================
# Примеры: Работа с timestamp
# ============================================================

from datetime import datetime

# Поточний час
now = datetime.now()

# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу

##########################################################

from datetime import datetime

# Припустимо, є timestamp
timestamp = 1617183600

# Конвертація timestamp назад у datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime


# ============================================================
# Примеры: Парсинг даты в строку
# ============================================================

from datetime import datetime

now = datetime.now()

# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)  

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)

##########################################################

from datetime import datetime

# Припустимо, у нас є дата у вигляді рядка
date_string = "2023.03.14"

# Перетворення рядка в об'єкт datetime
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу


# ============================================================
# Примеры: Работа с ISO форматом дати
# ============================================================

from datetime import datetime

# Поточна дата та час
now = datetime.now()

# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)

##########################################################

from datetime import datetime

iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)

##########################################################

from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()

print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня

##########################################################

from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")


# ============================================================
# Примеры: Работа с временными зонами
# ============================================================

from datetime import datetime, timezone

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print(local_now)
print(utc_now)  # Виведе поточний час в UTC

##########################################################

from datetime import datetime, timezone, timedelta

utc_time = datetime.now(timezone.utc)

# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)  

##########################################################

from datetime import datetime, timezone, timedelta

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC

##########################################################

from datetime import datetime, timezone, timedelta

# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)


# ============================================================
# Примеры: Работа с временем
# ============================================================

import time

current_time = time.time()
print(f"Поточний час: {current_time}")

##########################################################

import time

print("Початок паузи")
time.sleep(1)
print("Кінець паузи")

##########################################################

import time

current_time = time.time()
print(f"Поточний час: {current_time}")

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

##########################################################

import time

current_time = time.time()
print(f"Поточний час: {current_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")

##########################################################

import time

# Записуємо час на початку виконання
start_time = time.perf_counter()

# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")

##########################################################

# Один мільйон
a = 1_000_000
print(a)  # Виведе 1000000

# Десять мільйонів
b = 10_000_000
print(b)  # Виведе 10000000

# Один мільярд
c = 1_000_000_000
print(c)  # Виведе 1000000000

#########################################

games = [
    {"id": 101, "title": "Cyberpunk 2077"},
    {"id": 102, "title": "The Witcher 3"},
    {"id": 103, "title": "SWAT 4"},
    {"id": 104, "title": "Metro 2033"},
]

owned_ids = {102, 103}
installed_ids = {103}

for game in games:
    if game ["id"] in owned_ids:
        status = "INSTALL"
        if game ["id"] in installed_ids:
                status = "PLAY"
    else: 
        status = "BUY"
    print(f'{game["title"]}: {status}')

#########################################

catalog = {
    101: "Cyberpunk 2077",
    102: "The Witcher 3",
    103: "SWAT 4",
}

cart_ids = [103, 999, 101, 103]

for game_id in cart_ids:
    if game_id in catalog:
        print(f"OK: {catalog[game_id]}")
    else:
        print(f"MISSING: {game_id}")

#########################################

profile = {
    "username": "andrewn",
    "email": "andrew@gmail.com",
    "age": 24,
    "country": "Ukraine"
}


for key, value in profile.items():
     print(f"{key} : {value}")











