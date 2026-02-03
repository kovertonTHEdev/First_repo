# ================================
# 1. Greeting (Вітання)
# ================================

RUN_INPUT = False  # Перемикач: якщо False — блоки з input() не виконуються, якщо True — виконуються

print("Hello World!")  # Виводимо рядок у консоль
print("Hello Git")     # Виводимо ще один рядок у консоль


# ================================
# 2. Name check (Перевірка імені)
# ================================

if RUN_INPUT:  # Умова: цей блок виконається тільки якщо RUN_INPUT == True
    name = input("Enter your name: ").strip()  # input() зчитує текст (str), strip() прибирає пробіли по краях
    banned_names = ["володимир", "путін", "росія", "росіянин", "тварина"]  # Список (list) заборонених імен

    if name.lower() in banned_names:  # lower() робить нижній регістр; in перевіряє, чи є елемент у списку
        print("Good evening, we are from Ukraine")  # Вивід повідомлення, якщо ім'я заборонене
    else:  # Інакше (якщо ім'я не в списку)
        print(f"Hello, {name}!")  # f-рядок: підставляє значення змінної name в текст


# ================================
# 3. Age check (Перевірка віку)
# ================================

if RUN_INPUT:  # Блок працює тільки якщо RUN_INPUT == True
    age = int(input("\nHow old are you? "))  # input() повертає str; int(...) перетворює у ціле число

    if age < 18:  # Перевіряємо умову: якщо вік менший за 18
        print("Access denied")  # Якщо менше 18 — доступ заборонено
    else:  # В іншому випадку (18 і більше)
        print("Access granted")  # Доступ дозволено


# ================================
# 4. Square perimeter calculation
# (Обчислення периметра квадрата)
# ================================

if RUN_INPUT:  # Виконується тільки при RUN_INPUT == True
    side = float(input("\nEnter side length: "))  # float(...) перетворює введення у число з дробом
    perimeter = 4 * side  # Математика: периметр квадрата = 4 * сторона
    print(f"Perimeter of the square is {perimeter}")  # Виводимо результат через f-рядок


# ================================
# 5. Shopping calculation
# (Розрахунок вартості покупок)
# ================================

if RUN_INPUT:
    price_per_croissant = 1.04  # Ціна за 1 круасан (float)
    price_per_glass = 0.34      # Ціна за 1 склянку (float)
    price_per_coffee_pack = 4.42  # Ціна за 1 упаковку кави (float)

    num_croissants = int(input("\nEnter quantity of croissants: "))  # Кількість круасанів (int)
    num_glasses = int(input("Enter quantity of drinking glasses: "))  # Кількість склянок (int)
    num_coffee_packs = int(input("Enter quantity of coffee packs: "))  # Кількість упаковок кави (int)

    total_cost = (  # Загальна вартість (float); дужки дають писати вираз у кілька рядків
        num_croissants * price_per_croissant +  # Множимо кількість на ціну
        num_glasses * price_per_glass +         # Множимо кількість на ціну
        num_coffee_packs * price_per_coffee_pack  # Множимо кількість на ціну
    )

    total_dollars = int(total_cost)  # Беремо цілу частину (долари) від загальної суми
    total_cents = int(total_cost * 100) % 100  # Переводимо в "центи", беремо останні 2 цифри через %

    print(f"Total price: {total_dollars} dollars and {total_cents} cents")  # Виводимо суму


# ================================
# 6. List example + count()
# (Робота зі списком)
# ================================

my_list = [1, 2, 3, 4, 2, 2, 5, 2]  # Створюємо список (list) з числами
count_2 = my_list.count(2)  # Метод count(x) рахує, скільки разів x зустрічається у списку
print(count_2)  # Виводимо кількість двійок (очікувано 4)

my_list = [1, 2, 3, 4, 5]  # Новий список
print(len(my_list))  # len(...) повертає довжину списку (кількість елементів)

nums = [3, 1, 4, 1, 5, 9, 2]  # Список для сортування
nums.sort()  # sort() сортує список "на місці" (змінює сам список)
print(nums)  # Виводимо відсортований список

nums.sort(reverse=True)  # reverse=True сортує за спаданням
print(nums)  # Виводимо список після сортування за спаданням

words = ["banana", "apple", "cherry"]  # Список рядків
words.sort(key=len)  # key=len означає: сортувати за довжиною кожного слова
print(words)  # Виводимо відсортований список слів


# ================================
# 7. sorted() vs sort()
# (Сортування без зміни оригіналу)
# ================================

nums = [3, 1, 4, 1, 5, 9, 2]  # Оригінальний список
sorted_nums = sorted(nums)  # sorted(...) повертає новий відсортований список, НЕ змінює nums
print(sorted_nums)  # Виводимо новий список

sorted_nums_desc = sorted(nums, reverse=True)  # Сортування за спаданням у новий список
print(sorted_nums_desc)  # Виводимо

words = ["banana", "apple", "cherry"]  # Список слів
sorted_words = sorted(words, key=len)  # Новий список: сортування за довжиною слова
print(sorted_words)  # Виводимо


# ================================
# 8. Dictionary basics
# (Робота зі словником)
# ================================

my_dict = {"name": "Alice", "age": 25, "city": "New York"}  # Словник (dict): ключ -> значення
print(my_dict["city"])  # Доступ до значення за ключем "city" (якщо ключа нема — буде помилка KeyError)

my_dict["age"] = 26  # Заміна значення за існуючим ключем "age"
my_dict["email"] = "alice@example.com"  # Додавання нового ключа і значення
print(my_dict)  # Вивід словника

del my_dict["age"]  # del видаляє пару ключ-значення за ключем "age"
print(my_dict)  # Вивід після видалення

print("name" in my_dict)  # in для словника перевіряє наявність КЛЮЧА
print("age" in my_dict)   # Перевіряємо, чи є ключ "age"


# ================================
# 9. Set basics
# (Основи множин)
# ================================

numbers = {1, 2, 3}  # Множина (set): зберігає тільки унікальні елементи (без дублікатів)
numbers.add(4)  # add(...) додає елемент у множину
print(numbers)  # Виводимо множину (порядок може бути різний)

numbers = {1, 2, 3}  # Нова множина
numbers.remove(3)  # remove(...) видаляє елемент; якщо елемента немає — буде помилка
print(numbers)  # Вивід

numbers = {1, 2, 3}  # Нова множина
numbers.discard(2)  # discard(...) видаляє елемент; якщо елемента немає — помилки не буде
print(numbers)  # Вивід


# ================================
# 10. Set operations
# (Операції над множинами)
# ================================

a = {1, 2, 3}  # Перша множина
b = {3, 4, 5}  # Друга множина
print(a.intersection(b))  # intersection(...) повертає перетин: спільні елементи
print(a & b)  # Оператор & робить те саме: перетин

a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))  # difference(...) повертає різницю: елементи, що є в a, але нема в b
print(a - b)  # Оператор - робить те саме

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # симетрична різниця: все, крім спільного
print(a ^ b)  # Оператор ^ робить те саме

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # union(...) об'єднання: всі елементи з a і b
print(a | b)  # Оператор | робить те саме

my_frozenset = frozenset([1, 2, 3, 4, 5])  # frozenset — незмінювана множина (immutable)

a = frozenset([1, 2, 3])  # frozenset можна створювати як set, але змінювати не можна
b = frozenset([3, 4, 5])

union = a | b  # Об'єднання для frozenset (працює як для set)
intersection = a & b  # Перетин
difference = a - b  # Різниця
symmetric_difference = a ^ b  # Симетрична різниця

print(union)  # Вивід об'єднання
print(intersection)  # Вивід перетину
print(difference)  # Вивід різниці
print(symmetric_difference)  # Вивід симетричної різниці


# ================================
# 11. String methods (Робота з рядками)
# ================================

s = "Hello world!"  # Рядок (str)
print(s[0])  # Індекс 0 — перший символ рядка
print(s[-1])  # Індекс -1 — останній символ

s = "Hello"
print(s.upper())  # upper() робить всі літери великими

s = "Some Text"
print(s.lower())  # lower() робить всі літери маленькими

s = "Bill Jons"
print(s.startswith("Bi"))  # startswith(...) перевіряє, чи починається рядок з "Bi"

s = "hello.jpg"
print(s.endswith("jpg"))  # endswith(...) перевіряє, чи закінчується рядок на "jpg"

s = "hello world".capitalize()  # capitalize() робить першу букву великою, решту — малими
print(s.capitalize())  # (увага: тут ти викликаєш capitalize() вдруге — буде той самий результат)

s = "hello world".title()  # title() робить першу букву кожного слова великою
print(s.title())  # (увага: тут теж виклик вдруге — результат той самий)


# ================================
# 12. String formatting (Форматування рядків)
# ================================

name = "John"  # Змінна-рядок
print("Hello, {}!".format(name))  # format(...) підставляє значення у {}

age = 25
print("Hello, {}. You are {} years old.".format(name, age))  # Кілька підстановок по порядку

print("Hello, {name}. You are {age} years old.".format(name="Jane", age=30))  # Іменовані параметри

print("Hello, {1}. You are {0} years old.".format(age, name))  # Підстановка за індексами


# ================================
# 13. Slices (Зрізи у Python)
# ================================

s = "Hello, World!"
first_five = s[:5]  # Зріз: від початку (0) до 5 НЕ включно
print(first_five)  # Виводимо "Hello"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers[::-1]  # Зріз зі кроком -1: розвертає список
print(reverse_numbers)  # Вивід перевернутого списку

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers[:]  # Зріз без меж: робить копію списку
print(copy_numbers)  # Вивід копії


# ================================
# 14. Conditional statements, loops (Умовні оператори, цикли)
# ================================

num = 7  # Змінна з числом

if num > 10:  # Перевірка умови
    print("num більше за 10")  # Виконується, якщо умова True
else:
    print("num не більше за 10")  # Виконується, якщо умова False

money = 0  # 0 у Python вважається False у булевому контексті
if money:  # Якщо money "істинне" (не 0, не порожнє тощо)
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")  # Для 0 спрацює else


# ================================
# 15. Оператор is
# ================================

a = [1, 2, 3]  # Створюємо список
b = a  # b посилається на той самий об'єкт, що і a (це одне посилання)
c = [1, 2, 3]  # Новий окремий список з таким самим вмістом

print(a is b)  # is перевіряє "це той самий об'єкт?" -> True
print(a is c)  # Тут різні об'єкти -> False


# ================================
# 16. Булева алгебра
# ================================

name = "Taras"
age = 17
has_driver_licence = True

if name and age >= 18 and has_driver_licence:  # and: всі умови мають бути True
    print(f"User {name} can rent a car")
else:
    print(f"User {name} can not rent a car")  # Тут age < 18, тому буде else


# ================================
# 17. Блоки інструкцій та вкладені if
# ================================

x = 8
y = 5

if x >= 0:  # Якщо x не від’ємний
    if y >= 0:  # Якщо y теж не від’ємний
        print("Перша чверть")  # x>=0, y>=0
    else:
        print("Четверта чверть")  # x>=0, y<0
else:
    if y >= 0:
        print("Друга чверть")  # x<0, y>=0
    else:
        print("Третя чверть")  # x<0, y<0


# ================================
# 18. Оператор match
# ================================

fruit = "apple"

match fruit:  # match порівнює значення fruit з варіантами case
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:  # _ означає "будь-що інше" (за замовчуванням)
        print("Unknown fruit.")

point = (1, 0)  # Кортеж (tuple) з двох значень

match point:  # match може розпаковувати кортежі у шаблонах
    case (0, 0):
        print("Точка в центрі координат")
    case (0, y):  # y тут — змінна, яка отримає значення другого елемента
        print(f"Точка лежить на осі Y: y={y}")
    case (x, 0):  # x тут — змінна, яка отримає значення першого елемента
        print(f"Точка лежить на осі X: x={x}")
    case (x, y):  # Загальний випадок: будь-які координати
        print(f"Точка має координати:  x={x}, y={y}")
    case _:
        print("Це не точка")


# ================================
# 19. Цикл for
# ================================

fruit = "apple"
for char in fruit:  # for перебирає кожен символ рядка по черзі
    print(char)  # Виводимо символ

alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")  # end=" " — щоб не було переносу рядка, а ставився пробіл

some_iterable = ["a", "b", "c"]
for i in some_iterable:  # Перебір елементів списку
    print(i)

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)  # ** — піднесення до степеня (квадрат числа)


# ================================
# 19. Цикл while
# ================================

k = 0  # Лічильник
while k < 10:  # while повторює блок, поки умова True
    k = k + 1  # Збільшуємо k на 1
print(k)  # Після циклу k буде 10


# ================================
# 20. Завершення ітерації за допомогою continue
# ================================

a = 0
while a < 6:
    a = a + 1
    if not a % 2:  # a % 2 дає остачу; якщо 0 — число парне; not робить True
        continue  # continue пропускає решту тіла циклу і переходить до наступної ітерації
    print(a)  # Виведе тільки непарні: 1,3,5


# ================================
# 21. Функція range
# ================================

for i in range(5):  # range(5) дає числа 0..4
    print(i)

for i in range(2, 10):  # range(2,10) дає 2..9
    print(i)

for i in range(0, 10, 2):  # range(start, stop, step): крок 2
    print(i)


# ================================
# 22. Функція enumerate
# ================================

some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):  # enumerate дає пару (індекс, значення)
    print(index, value)


# ================================
# 23. Функція zip
# ================================

list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):  # zip з'єднує елементи попарно
    print(number, letter)

list1 = [1, 2, 3]
list2 = ["a", "b", "c", "d", "e"]
for number, letter in zip(list1, list2):  # zip зупиниться на довжині коротшого списку
    print(number, letter)


# ================================
# 24. Цикли та словники
# ================================

numbers = {  # Словник: ключ -> значення
    1: "one",
    2: "two",
    3: "three"
}

for key in numbers:  # Перебір словника за замовчуванням проходить по ключах
    print(key)

for key in numbers.keys():  # keys() явним чином повертає ключі
    print(key)

for val in numbers.values():  # values() повертає значення
    print(val)

for key, value in numbers.items():  # items() повертає пари (ключ, значення)
    print(key, value)


# ================================
# 24. Механізм обробки винятків
# ================================

val = "a"
try:  # try: пробуємо виконати код, який може впасти з помилкою
    val = int(val)  # int("a") викличе ValueError, бо "a" не число
except ValueError:  # except ловить конкретну помилку ValueError
    print(f"val {val} is not a number")  # Обробка: повідомляємо, що це не число
else:  # else виконується, якщо помилки НЕ було
    print(val > 0)  # Перевіряємо, чи число більше 0
finally:  # finally виконується завжди (було виключення чи ні)
    print("This will be printed anyway")


# ================================
# 25. Створення та виклик функцій
# ================================

def say_hello():  # def створює функцію без параметрів
    """Печатает приветствие."""  # Докстрінг: опис функції
    print("Привіт, Світ!")  # Тіло функції

say_hello()  # Виклик функції
say_hello()  # Повторний виклик


# ================================
# 26. Аргумент функції
# ================================

def print_max(a, b):  # Функція з двома параметрами a і b
    """Печатает, какое число больше (или что они равны)."""
    if a > b:
        print(a, "максимально")
    elif a == b:
        print(a, "дорівнює", b)
    else:
        print(b, "максимально")

print_max(3, 4)  # Передаємо аргументи 3 і 4

x = 5
y = 7
print_max(x, y)  # Передаємо значення змінних


# ================================
# 27. Повернення результату
# ================================

def add_numbers(num1: int, num2: int) -> int:  # Підказки типів: int -> int (не обов'язково для роботи)
    """Возвращает сумму двух чисел."""
    total = num1 + num2  # Обчислюємо суму
    return total  # return повертає значення з функції

result = add_numbers(5, 10)  # Зберігаємо результат виклику
print(result)  # Вивід

def greet(name: str) -> str:
    """Возвращает строку-приветствие по имени."""
    return f"Привіт, {name}!"  # Повертаємо рядок

def greet(name: str) -> str:  # (дублікат) функція з тим самим ім'ям перекриє попередню
    return f"Привіт, {name}!"

greeting = greet("Олексій")  # Викликаємо функцію
print(greeting)  # Вивід

def is_even(num: int) -> bool:
    """Возвращает True, если число чётное, иначе False."""
    return num % 2 == 0  # %2 дає остачу; якщо 0 — парне

check_even = is_even(4)  # Перевірка
print(check_even)  # Вивід True


# ================================
# 28. Принципи змінності об'єктів у Python
# ================================

def modify_string(original: str) -> str:
    """Показує, що рядок незмінний (immutable): повертаємо новий рядок."""
    original = "змінено"  # Всередині функції змінюємо локальну змінну original
    return original  # Повертаємо нове значення

str_var = "оригінал"
print(modify_string(str_var))  # Виведе "змінено" (те, що повернула функція)
print(str_var)  # Виведе "оригінал" (оригінальна змінна не змінилась)

def modify_list_inplace(lst: list) -> None:
    """Список змінний (mutable): можемо змінити його напряму."""
    lst.append(4)  # append змінює список "на місці"

my_list = [1, 2, 3]
modify_list_inplace(my_list)  # Після виклику my_list зміниться
print(my_list)  # [1, 2, 3, 4]

def modify_list_copy(lst: list) -> None:
    """Якщо зробити копію — зміниться копія, а не оригінал."""
    lst = lst.copy()  # copy() створює новий список
    lst.append(4)  # Змінюємо копію

my_list = [1, 2, 3]
modify_list_copy(my_list)  # Оригінал не зміниться
print(my_list)  # [1, 2, 3]


# ================================
# 29. Задача на функцію
# ================================

def string_to_codes(string: str) -> dict:
    """Повертає словник: символ -> його Unicode-код (ord), без повторів."""
    codes = {}  # Порожній словник для результату
    for ch in string:  # Перебираємо кожен символ рядка
        if ch not in codes:  # Перевіряємо, чи символ ще не був ключем у словнику
            codes[ch] = ord(ch)  # ord(...) повертає код символу; записуємо у словник
    return codes  # Повертаємо готовий словник

result = string_to_codes("Hello world!")  # Викликаємо функцію
print(result)  # Вивід


# ================================
# 30. Область видимості: Local
# ================================

x = 50  # Глобальна змінна

def func() -> None:
    x = 2  # Локальна змінна x (не змінює глобальну)
    print('Зміна локального x на', x)

func()  # Виклик функції
print('Глобальний x як і раніше', x)  # Глобальний x залишився 50


# ================================
# 30. Область видимості: Global
# ================================

x = 50  # Глобальна змінна

def func():
    global x  # global дозволяє змінювати глобальну змінну всередині функції
    print('x дорівнює', x)
    x = 2  # Тут ми змінюємо саме глобальний x
    print('Змінюємо глобальне значення x на', x)

func()
print('Значення x складає', x)  # Тепер x = 2


# ================================
# 31. Ключові аргументи функції
# ================================

def greet(name, message="Привіт"):  # message має значення за замовчуванням
    print(f"{message}, {name}!")  # Вивід привітання

greet("Олексій")  # Виклик: message буде "Привіт"
greet("Марія", message="Добрий день")  # Виклик з іменованим аргументом

def func(a, b=5, c=10):
    print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

func(3, 7)  # a=3, b=7, c=10
func(25, c=24)  # a=25, b=5, c=24
func(c=50, a=100)  # a=100, b=5, c=50

def say(message, times=1):
    print(message * times)  # * для рядка повторює його times разів

say('Привіт')
say('Світ', 5)


# ================================
# 32. Приклад використання параметру *args
# ================================

def print_all_args(*args):  # *args збирає всі позиційні аргументи у кортеж (tuple)
    for arg in args:  # Перебираємо всі аргументи
        print(arg)  # Виводимо кожен

print_all_args(1, 'hello', True)  # Передали 3 аргументи

def concatenate(*args) -> str:
    result = ""  # Початковий порожній рядок
    for arg in args:  # Перебираємо всі передані рядки
        result += arg  # Додаємо до результату
    return result  # Повертаємо склеєний рядок

print(concatenate("Hello", " ", "world", "!"))


# ================================
# 33. Приклад використання параметру *args та **kwargs
# ================================

def greet(**kwargs):  # **kwargs збирає всі іменовані аргументи у словник (dict)
    for key, value in kwargs.items():  # items() дає пари (ключ, значення)
        print(f"{key}: {value}")  # Вивід кожної пари

greet(name="Alice", age=25)  # Передаємо іменовані аргументи

def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)  # args — кортеж позиційних аргументів
    print("Ключові аргументи:", kwargs)  # kwargs — словник іменованих аргументів

example_function(1, 2, 3, name="Alice", age=25)


# ================================
# 34. Рекурсія
# ================================

def factorial(n):
    if n == 0:  # Базовий випадок: коли n == 0, зупиняємо рекурсію
        return 1
    else:
        return n * factorial(n-1)  # Рекурсивний випадок: викликаємо factorial ще раз

print(factorial(5))  # 5*4*3*2*1 = 120

def fibonacci(n):
    if n <= 1:  # Базовий випадок: 0 або 1
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Рекурсія: сума двох попередніх

print(fibonacci(10))  # 55


# ================================
# 35. Стек викликів рекурсії
# ================================

def factorial(n):
    print("Виклик функції factorial з n = ", n)  # Друкуємо поточний n, щоб бачити хід рекурсії
    if n == 1:  # Базовий випадок
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)  # Рахуємо результат через рекурсивний виклик
        print("Повернення результату для n = ", n, ": ", result)  # Показуємо, що повертаємо
        return result

print(factorial(5))  # Запуск з n=5


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

# ================================
# 37. Робота з випадковими величинами
# ================================

import random

dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")

#########################################

import random

num = random.random()
print(num)

#########################################

import random

fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")

#########################################

import random

target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")

#########################################

import random

cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

random.shuffle(cards)

print(f"Перемішана колода: {cards}")

#########################################

import random

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

#########################################

import random

items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
print(chosen_item)  

#########################################

import random

numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers)

#########################################

import random

colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)  

#########################################

import random

participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")

#########################################

import random

price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")

# ================================
# 37. Робота з модулем math
# ================================
import math

# Вихідне число
x = 3.7

# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини

print(ceil_result, floor_result, trunc_result)

#########################################

import math

# Використання констант
print(math.pi)  # Виведе приблизне значення π

# Тригонометрія
angle = math.radians(60)  # Конвертація з градусів у радіани
print(math.sin(angle))  # Синус кута

# Корінь числа
print(math.sqrt(9))  # Квадратний корінь з 9

# Логарифми
print(math.log(10, 2))  # Логарифм 10 за основою 2


#########################################


print(0.1 + 0.2 == 0.3)  # Це повертає False

#########################################

import math

r = math.isclose(0.1 + 0.2, 0.3)
print(r)  # Це поверне True

#########################################

import math

r = math.isclose(0.1, 0.10000000009)
print(r)  # Це поверне True






