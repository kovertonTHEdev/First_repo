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


from typing import (
    Callable,
)  # Функції як об'єкт першого класу можуть повертають інші функції


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
operations: Dict[
    str, Callable
] = {  # Cловник містить назви операцій і посилання на функції, які виконують ці операції.
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
def outer_function(
    msg,
):  # визначена таким чином, що приймає аргумент msg і створює внутрішню змінну message, значення якої ініціалізується переданим аргументом
    message = msg

    def inner_function():  # використовує змінну message, яка була визначена у зовнішньому лексичному середовищі outer_function.
        print(message)

    return inner_function


# Створення замикання
my_func = outer_function("Hello, world!")
my_func()


from typing import (
    Callable,
)  # замикання, яке буде зберігати інформацію про кількість разів виклику функції


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
    def apply_discount(
        price: float,
    ) -> float:  # Перетворимо функцію apply_discount, використовуючи каррінг. Це дозволить нам створити "замовлені" функції для різних рівнів знижок, кожна з яких буде приймати тільки ціну товару
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


def logger(
    func,
):  # Декоратор logger приймає функцію як аргумент і повертає нову функцію complicated = logger(complicated)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner


complicated = logger(complicated)
print(complicated(2, 3))


def logger(
    func,
):  # Щоб спростити застосування цього шаблону проектування, в Python є спеціальний синтаксис декоратора. Декоратори використовуються з синтаксисом @, що робить їх застосування простим та елегантним.
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

