# ----------------------------
# Тема 1: Функція як об'єкт першого класу
# ----------------------------
from typing import Callable  # Функції можуть бути аргументами інших функцій.


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)


# Використання
result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)

print(result_add, result_multiply)  # 8 15


from typing import Callable
# Функції як об'єкт першого класу можуть повертають інші функції


def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base**exponent

    return inner


# Використання
square = power(2)
cube = power(3)

print(square(4))  # 16
print(cube(4))  # 64


from typing import Callable, Dict  # зберігання функцій у структурах даних


# Визначення функцій
def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base**exponent

    return inner


# Використання power для створення функцій square та cube
square = power(2)
cube = power(3)

# Словник операцій
operations: Dict[str, Callable] = {  # Cловник містить назви операцій і посилання на функції, які виконують ці операції.
    "add": add,
    "multiply": multiply,
    "square": square,
    "cube": cube,
}

# Використання операцій
result_add = operations["add"](10, 20)  # 30
result_square = operations["square"](5)  # 25

print(result_add)  # 30
print(result_square)  # 25


# ----------------------------
# Тема 2: Замикання
# ----------------------------
def outer_function(msg):  # визначена таким чином, що приймає аргумент msg і створює внутрішню змінну message, значення якої ініціалізується переданим аргументом
    message = msg

    def inner_function():  # використовує змінну message, яка була визначена у зовнішньому лексичному середовищі outer_function.
        print(message)

    return inner_function


# Створення замикання
my_func = outer_function("Hello, world!")
my_func()


from typing import Callable  # замикання, яке буде зберігати інформацію про кількість разів виклику функції


def counter() -> Callable[[], int]:
    count = 0

    def increment() -> (
        int
    ):  # increment замкнула в собі змінну count і має до неї доступ навіть після того, як зовнішня функція counter завершує своє виконання
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count
        count += 1
        return count

    return increment


# Створення лічильника
count_calls = counter()

# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3

# ----------------------------
# Тема 3: Каррінг
# ----------------------------


def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)


# Використання
discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
print(discounted_price)  # 450.0

discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
print(discounted_price)  # 400.0


from typing import Callable


def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float,) -> float:  # Перетворимо функцію apply_discount, використовуючи каррінг. Це дозволить нам створити "замовлені" функції для різних рівнів знижок, кожна з яких буде приймати тільки ціну товару
        return price * (1 - discount_percentage / 100)

    return apply_discount


# Каррінг в дії
ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)

# Застосування знижок
discounted_price = ten_percent_discount(500)  # 450.0
print(discounted_price)

discounted_price = twenty_percent_discount(500)  # 400.0
print(discounted_price)


from typing import Callable, Dict


def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)

    return apply_discount


# Створення словника з функціями знижок
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30),
}

# Використання функції зі словника
price = 500
discount_type = "20%"

discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price}")


# ----------------------------
# Тема 4: Декоратори
# ----------------------------
def complicated(x: int, y: int) -> int:
    return x + y


def logger(func):  # Декоратор logger приймає функцію як аргумент і повертає нову функцію complicated = logger(complicated)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner


complicated = logger(complicated)
print(complicated(2, 3))


def logger(func):  # Щоб спростити застосування цього шаблону проектування, в Python є спеціальний синтаксис декоратора. Декоратори використовуються з синтаксисом @, що робить їх застосування простим та елегантним.
    # Точно той самий код вище, який робить в точності те саме, можна записати у вигляді:

    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner


@logger
def complicated(x: int, y: int) -> int:
    return x + y


print(complicated(2, 3))


from functools import wraps

def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))
print(complicated.__name__)


from functools import wraps  # При створенні декораторів використовувати модуль functools, для збереження метаданих оригінальної функції.
                             # Функція functools.wraps зберігає інформацію про оригінальну функцію.
def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}") # Викликається функція: complicated: 2, 3
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}") # Функція complicated завершила виконання: 5
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3)) # 5
print(complicated.__name__) # complicated


# ----------------------------
# Тема 5: Функція map()
# ----------------------------
numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)
# 1
# 4
# 9
# 16
# 25

# Якщо ми хочем отримати список, а не генератор то код можна записати так:
numbers = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums) # [1, 4, 9, 16, 25]


nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)


# ----------------------------
# Тема 6: Функція filter()
# ----------------------------
even_nums = filter(lambda x: x % 2 == 0, range(1, 11))
print(list(even_nums)) # [2, 4, 6, 8, 10]


some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str) # идавництво


# ----------------------------
# Тема 7: Функція any()
# ----------------------------
nums = [0, False, 5, 0]
result = any(nums)  # Перевіримо, чи наявний хоч один істинний елемент у списку
print(result) # Код поверне True, оскільки 5 є істинним значенням в списку nums


nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)  # перевіримо чи є в списку парні числа
print(result) # Код поверне False, оскільки немає парних чисел в списку nums


# ----------------------------
# Тема 8: Функція all()
# ----------------------------
nums = [1, 2, 3, 4] 
result = all(nums)  # перевірка, чи всі елементи у списку істинні
print(result)


nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums)  # Чи всі елементи списку є парними
print(is_all_even) # Код виведе False, оскільки не всі числа парні в списку nums


words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words) # Чи всі слова у списку мають велику початкову букву
print(is_all_title_case)

