# ================================
# 1. Greeting (Вітання)
# ================================

RUN_INPUT = False

print("Hello World!")
print("Hello Git")


# ================================
# 2. Name check (Перевірка імені)
# ================================

if RUN_INPUT:
    # Берём имя, убираем пробелы по краям
    name = input("Enter your name: ").strip()
    banned_names = ["володимир", "путін", "росія", "росіянин", "тварина"]

    # Приводим к нижнему регистру и проверяем, есть ли имя в списке запрещённых
    if name.lower() in banned_names:
        print("Good evening, we are from Ukraine")
    else:
        print(f"Hello, {name}!")


# ================================
# 3. Age check (Перевірка віку)
# ================================

if RUN_INPUT:
    # Считываем возраст как число
    age = int(input("\nHow old are you? "))

    # Проверяем возраст по условию
    if age < 18:
        print("Access denied")
    else:
        print("Access granted")


# ================================
# 4. Square perimeter calculation
# (Обчислення периметра квадрата)
# ================================

if RUN_INPUT:
    # Считываем сторону квадрата
    side = float(input("\nEnter side length: "))
    # Считаем периметр (4 * сторона)
    perimeter = 4 * side
    print(f"Perimeter of the square is {perimeter}")


# ================================
# 5. Shopping calculation
# (Розрахунок вартості покупок)
# ================================

if RUN_INPUT:
    # Цены за 1 единицу товара
    price_per_croissant = 1.04
    price_per_glass = 0.34
    price_per_coffee_pack = 4.42

    # Количество товаров
    num_croissants = int(input("\nEnter quantity of croissants: "))
    num_glasses = int(input("Enter quantity of drinking glasses: "))
    num_coffee_packs = int(input("Enter quantity of coffee packs: "))

    # Общая стоимость
    total_cost = (
        num_croissants * price_per_croissant +
        num_glasses * price_per_glass +
        num_coffee_packs * price_per_coffee_pack
    )

    # Выделяем доллары и центы из общей суммы
    total_dollars = int(total_cost)
    total_cents = int(total_cost * 100) % 100

    print(f"Total price: {total_dollars} dollars and {total_cents} cents")


# ================================
# 6. List example + count()
# (Робота зі списком)
# ================================

my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)  # Считаем, сколько раз число 2 встречается в списке
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази


my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Длина списка

nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()          # Сортировка списка по возрастанию (меняет сам список)
print(nums)  # [1, 1, 2, 3, 4, 5, 9]

nums.sort(reverse=True)  # Сортировка по убыванию (меняет сам список)
print(nums)  # [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
words.sort(key=len)  # Сортировка по длине слова
print(words)  # ['apple', 'banana', 'cherry']


# ================================
# 7. sorted() vs sort()
# (Сортування без зміни оригіналу)
# ================================

nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)  # sorted() возвращает новый список, не меняя оригинал
print(sorted_nums)  # [1, 1, 2, 3, 4, 5, 9]

sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)  # [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['apple', 'banana', 'cherry']


# ================================
# 8. Dictionary basics
# (Робота зі словником)
# ================================

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["city"])  # Берём значение по ключу "city"

my_dict["age"] = 26                    # Меняем значение по ключу
my_dict["email"] = "alice@example.com" # Добавляем новую пару ключ-значение
print(my_dict)

del my_dict["age"]  # Удаляем пару по ключу
print(my_dict)

print("name" in my_dict)  # Проверяем наличие ключа
print("age" in my_dict)


# ================================
# 9. Set basics
# (Основи множин)
# ================================

numbers = {1, 2, 3}
numbers.add(4)       # Добавляем элемент в множество
print(numbers)  # {1, 2, 3, 4}

numbers = {1, 2, 3}
numbers.remove(3)    # Удаляем элемент (ошибка, если элемента нет)
print(numbers)  # {1, 2}

numbers = {1, 2, 3}
numbers.discard(2)   # Удаляем элемент (без ошибки, если элемента нет)
print(numbers)  # {1, 3}


# ================================
# 10. Set operations
# (Операції над множинами)
# ================================

a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # Пересечение: общие элементы
print(a & b)              # То же самое

a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))    # Разница: что есть в a, но нет в b
print(a - b)              # То же самое

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # Симметричная разница: всё кроме общего
print(a ^ b)                       # То же самое

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # Объединение: все элементы из обоих множеств
print(a | b)       # То же самое

my_frozenset = frozenset([1, 2, 3, 4, 5])  # Неизменяемое множество

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

union = a | b                 # Объединение frozenset
intersection = a & b          # Пересечение frozenset
difference = a - b            # Разница frozenset
symmetric_difference = a ^ b  # Симметричная разница frozenset

print(union)
print(intersection)
print(difference)
print(symmetric_difference)


# ================================
# 11. String methods (Робота з рядками)
# ================================

s = "Hello world!"
print(s[0])   # Первый символ
print(s[-1])  # Последний символ

s = "Hello"
print(s.upper())  # Делает все буквы заглавными

s = "Some Text"
print(s.lower())  # Делает все буквы маленькими

s = "Bill Jons"
print(s.startswith("Bi"))  # Проверка: начинается ли строка с "Bi"

s = "hello.jpg"
print(s.endswith("jpg"))   # Проверка: заканчивается ли строка на "jpg"

s = "hello world".capitalize()  # Делает первую букву заглавной
print(s.capitalize())

s = "hello world".title()       # Делает заглавной первую букву каждого слова
print(s.title())


# ================================
# 12. String formatting (Форматування рядків)
# ================================

name = "John"
print("Hello, {}!".format(name))  # Подставляем значение в {}

age = 25
print("Hello, {}. You are {} years old.".format(name, age))  # Несколько подстановок

print("Hello, {name}. You are {age} years old.".format(name="Jane", age=30))  # Именованные

print("Hello, {1}. You are {0} years old.".format(age, name))  # По индексам


# ================================
# 13. Slices (Зрізи у Python)
# ================================

s = "Hello, World!"
first_five = s[:5]  # Срез первых 5 символов
print(first_five)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers[::-1]  # Разворот списка
print(reverse_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers[:]  # Копия списка
print(copy_numbers)


# ================================
# 14. Conditional statements, loops (Умовні оператори, цикли)
# ================================

num = 7

if num > 10:
    print("num більше за 10")
else:
    print("num не більше за 10")

money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")


# ================================
# 15. Оператор is
# ================================

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True: это одна и та же ссылка на объект
print(a is c)  # False: разные объекты, хотя содержимое одинаковое


# ================================
# 16. Булева алгебра
# ================================

name = "Taras"
age = 17
has_driver_licence = True

# Проверяем сразу несколько условий через and
if name and age >= 18 and has_driver_licence:
    print(f"User {name} can rent a car")
else:
    print(f"User {name} can not rent a car")


# ================================
# 17. Блоки інструкцій та вкладені if
# ================================

x = 8
y = 5

# Определяем четверть координатной плоскости
if x >= 0:
    if y >= 0:
        print("Перша чверть")
    else:
        print("Четверта чверть")
else:
    if y >= 0:
        print("Друга чверть")
    else:
        print("Третя чверть")


# ================================
# 18. Оператор match
# ================================

fruit = "apple"

# Сравниваем значение с шаблонами (case)
match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")

point = (1, 0)

# Матчим кортеж (x, y) на разные варианты
match point:
    case (0, 0):
        print("Точка в центрі координат")
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}")
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}")
    case _:
        print("Це не точка")


# ================================
# 19. Цикл for
# ================================

fruit = "apple"
for char in fruit:
    print(char)  # Печатаем каждый символ строки

alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")  # Печатаем в одну строку через пробел

some_iterable = ["a", "b", "c"]
for i in some_iterable:
    print(i)  # Проходим по списку и печатаем элементы

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)  # Печатаем квадраты чисел


# ================================
# 19. Цикл while
# ================================

k = 0
while k < 10:
    k = k + 1  # Увеличиваем счётчик, пока условие True
print(k)


# ================================
# 20. Завершення ітерації за допомогою continue
# ================================

a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue  # Пропускаем чётные числа
    print(a)


# ================================
# 21. Функція range
# ================================

for i in range(5):
    print(i)  # 0..4

for i in range(2, 10):
    print(i)  # 2..9

for i in range(0, 10, 2):
    print(i)  # 0,2,4,6,8


# ================================
# 22. Функція enumerate
# ================================

some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)  # Даёт индекс и значение


# ================================
# 23. Функція zip
# ================================

list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)  # Склеиваем элементы попарно

list1 = [1, 2, 3]
list2 = ["a", "b", "c", "d", "e"]
for number, letter in zip(list1, list2):
    print(number, letter)  # zip остановится на длине короткого списка


# ================================
# 24. Цикли та словники
# ================================

numbers = {
    1: "one",
    2: "two",
    3: "three"
}

for key in numbers:
    print(key)  # По умолчанию перебираются ключи

for key in numbers.keys():
    print(key)  # Явно ключи

for val in numbers.values():
    print(val)  # Значения

for key, value in numbers.items():
    print(key, value)  # Пары ключ-значение


# ================================
# 24. Механізм обробки винятків
# ================================

val = "a"
try:
    # Пробуем преобразовать строку в число
    val = int(val)
except ValueError:
    # Срабатывает, если преобразование невозможно
    print(f"val {val} is not a number")
else:
    # Срабатывает, если ошибок не было
    print(val > 0)
finally:
    # Срабатывает всегда
    print("This will be printed anyway")


# ================================
# 25. Створення та виклик функцій
# ================================

def say_hello():
    """Печатает приветствие."""
    print("Привіт, Світ!")


say_hello()
say_hello()


# ================================
# 26. Аргумент функції
# ================================

def print_max(a, b):
    """Печатает, какое число больше (или что они равны)."""
    if a > b:
        print(a, "максимально")
    elif a == b:
        print(a, "дорівнює", b)
    else:
        print(b, "максимально")


print_max(3, 4)

x = 5
y = 7
print_max(x, y)


# ================================
# 27. Повернення результату
# ================================

def add_numbers(num1: int, num2: int) -> int:
    """Возвращает сумму двух чисел."""
    total = num1 + num2
    return total


result = add_numbers(5, 10)
print(result)

def greet(name: str) -> str:
    """Возвращает строку-приветствие по имени."""
    return f"Привіт, {name}!"

### Розділення задачі 

def greet(name: str) -> str:
    return f"Привіт, {name}!"

greeting = greet("Олексій")
print(greeting)  # Виведе: Привіт, Олексій!

def is_even(num: int) -> bool:
    """Возвращает True, если число чётное, иначе False."""
    return num % 2 == 0


check_even = is_even(4)
print(check_even)


# ================================
# 28. Принципи змінності об'єктів у Python
# ================================

def modify_string(original: str) -> str:
    """Показывает, что строка (immutable) не меняется снаружи — возвращаем новую."""
    original = "змінено"
    return original


str_var = "оригінал"
print(modify_string(str_var))
print(str_var)

def modify_list_inplace(lst: list) -> None:
    """Меняет список напрямую (mutable): добавляет элемент 4."""
    lst.append(4)


### Розділення задачі 

my_list = [1, 2, 3]
modify_list_inplace(my_list)
print(my_list)

def modify_list_copy(lst: list) -> None:
    """Создаёт копию списка и меняет копию — оригинал снаружи не меняется."""
    lst = lst.copy()
    lst.append(4)


my_list = [1, 2, 3]
modify_list_copy(my_list)
print(my_list)


# ================================
# 29. Задача на функцію
# ================================

def string_to_codes(string: str) -> dict:
    """Возвращает словарь: символ -> его ASCII/Unicode код (ord), без повторов."""
    codes = {}              # Словарь для результата
    for ch in string:       # Перебираем каждый символ строки
        if ch not in codes: # Если символ ещё не добавляли
            codes[ch] = ord(ch)  # Добавляем символ и его код
    return codes


result = string_to_codes("Hello world!")
print(result)


# ================================
# 30. Область видимості: Local
# ================================

x = 50

def func() -> None:
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2

func()
print('Глобальний x як і раніше', x)  # x як і раніше 50

# ================================
# 30. Область видимості: Global
# ================================

x = 50

def func():
    global x
    print('x дорівнює', x)  # x дорівнює 50
    x = 2
    print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

func()
print('Значення x складає', x)# Значення x складає 2

# ================================
# 31. Ключові аргументи функції
# ================================

def greet(name, message="Привіт"):
    print(f"{message}, {name}!")

    greet("Олексій")
    greet("Марія", message="Добрий день")  


### Розділення задачі 

def func(a, b=5, c=10):
    print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# a дорівнює 3, b дорівнює 7, а c дорівнює 10
func(3, 7)

# a дорівнює 25, b дорівнює 5, а c дорівнює 24
func(25, c=24)

# a дорівнює 100, b дорівнює 5, а c дорівнює 50
func(c=50, a=100)



def say(message, times=1):
    print(message * times)

say('Привіт') 
say('Світ', 5)

# ================================
# 32. Приклад використання параметру *args
# ================================

def print_all_args(*args):
    for arg in args:
        print(arg)

print_all_args(1, 'hello', True)

#Виведення: 
# 1
# hello
# True


### Розділення задачі 

def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))


# ================================
# 33. Приклад використання параметру *args та **kwargs
# ================================
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25)


### Розділення задачі 

def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)

example_function(1, 2, 3, name="Alice", age=25)

# ================================
# 34. Рекурсія
# ================================

def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок

print(factorial(5)) # виведе 120

### Розділення задачі про Фібоначчі 

def fibonacci(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

print(fibonacci(10)) # виведе 55

# ================================
# 35. Стек викликів рекурсії
# ================================

def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5))



