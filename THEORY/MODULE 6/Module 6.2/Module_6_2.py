# ----------------------------
# Тема 1: Класи контейнери
# ----------------------------
from collections import UserDict


class MyDictionary(UserDict):
    # Приклад додавання нового методу
    def add_key(self, key, value):
        self.data[key] = value


# Створення екземпляра власного класу
my_dict = MyDictionary({"a": 1, "b": 2})
my_dict.add_key("c", 3)
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}


from collections import UserDict

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    },
]


class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"


if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]

    print("---------------------------")

    for customer in customers:
        print(customer.phone_info())

    print("---------------------------")

    for customer in customers:
        print(customer.email_info())


from collections import UserList


class MyList(UserList):
    # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, якщо він ще не існує
    def add_if_not_exists(self, item):
        if item not in self.data:
            self.data.append(item)


# Створення екземпляру MyList
my_list = MyList([1, 2, 3])
print("Оригінальний список:", my_list)  # Оригінальний список: [1, 2, 3]

# Додавання елементу, якщо він не існує
my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
print("Оновлений список:", my_list)  # Оновлений список: [1, 2, 3, 4]


from collections import UserList


class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))


countable = CountableList([1, "2", 3, "4"])
countable.append("5")
print(countable.sum())


from collections import UserString


# Створення класу, який розширює UserString
class MyString(UserString):
    # Додавання методу, який перевіряє, чи рядок є паліндромом
    def is_palindrome(self):
        return self.data == self.data[::-1]


# Створення екземпляру MyString
my_string = MyString("radar")
print("Рядок:", my_string)  # Рядок: radar
print("Чи є паліндромом?", my_string.is_palindrome())  # Чи є паліндромом? True

# Створення іншого екземпляру MyString
another_string = MyString("hello")
print("Рядок:", another_string)  # Рядок: hello
print("Чи є паліндромом?", another_string.is_palindrome())  # Чи є паліндромом? False


from collections import UserString


class TruncatedString(UserString):
    MAX_LEN = 8

    def truncate(self):
        self.data = self.data[: self.MAX_LEN]


ts = TruncatedString("hello world!")
ts.truncate()
print(ts)  # hello wo


# ----------------------------
# Тема 2: Класи даних
# ----------------------------
from dataclasses import dataclass


@dataclass
class Rectangle:  # Коли ми визначаємо клас Rectangle за допомогою @dataclass, Python автоматично створює метод __init__, який приймає атрибути width та height
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height


rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

print(f"Площа прямокутника 1: {rect1.area()}")  # Площа прямокутника 1: 50
print(f"Площа прямокутника 2: {rect2.area()}")  # Площа прямокутника 2: 21
print(f"Площа прямокутника 3: {rect3.area()}")  # Площа прямокутника 3: 48


# ----------------------------
# Тема 3: Перелічуваний тип даних
# ----------------------------
from enum import Enum


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


today = Day.MONDAY
print(today)  # Виведе: Day.MONDAY

if today == Day.MONDAY:
    print("Сьогодні понеділок.")  # Сьогодні понеділок.
else:
    print("Сьогодні не понеділок.")

print(today.name)  # MONDAY
print(today.value)  # 1

day_from_value = Day(1)  # 1
print(day_from_value)  # Виведе: Day.MONDAY


from enum import Enum, auto


class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()  # функцію auto(), щоб автоматично присвоїти унікальні значення кожному статусу, уникаючи необхідності вручну вказувати їх
    CANCELED = auto()  # Зміна або додавання нових значень в Enum не впливає на решту коду, що робить зміну (рефакторінг) та розширення коду простішими. Наприклад, Hовий статус "Відмінений"(CANCELED)


class Order:  # створимо клас Order, який буде використовувати наш перелічуваний тип даних OrderStatus для відстеження статусу замовлення
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")


order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)

order1.display_status()  # Статус замовлення 'Ноутбук': NEW.
order2.display_status()  # Статус замовлення 'Книга': NEW.

order1.update_status(
    OrderStatus.PROCESSING
)  # Замовлення 'Ноутбук' оновлено до статусу PROCESSING.
order2.update_status(
    OrderStatus.SHIPPED
)  # Замовлення 'Книга' оновлено до статусу SHIPPED.

order1.display_status()  # Статус замовлення 'Ноутбук': PROCESSING.
order2.display_status()  # Статус замовлення 'Книга': SHIPPED.


# ----------------------------
# Тема 5: Асоціація композиція та агрегація в ООП
# ----------------------------
# Розглянемо приклад, який ілюструє, чому наслідування не є найкращим рішенням, і як асоціація між цими класами через агрегацію є більш відповідним підходом.
class Owner:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"


class Cat(Owner):
    def __init__(self, nickname, age, name, phone):
        super().__init__(name, phone)
        self.nickname = nickname
        self.age = age

    def cat_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"


cat = Cat("Simon", 4, "Boris", "+380503002010")
print(cat.info())  # Boris: +380503002010
print(cat.cat_info())  # Cat Name: Simon, Age: 4


# У цьому прикладі, Cat та Owner асоційовані через агрегацію, де Cat має посилання на Owner, але об'єкти Owner можуть існувати незалежно від Cat.
# Тут ми кажемо: "Кішка має господаря", що є більш логічним і правильним з точки зору нашої програми.
class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"


class Cat:
    def __init__(self, nickname: str, age: int, owner: Owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner

    def get_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"


owner = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner)

print(cat.owner.info())
print(cat.get_info())

#  Агрегація дозволяє "частині" існувати незалежно від "цілого".
# У нашому прикладі, це означає, що господар може існувати окремо від улюбленця.
# Екземпляр господаря створюється незалежно і лише потім асоціюється з твариною, передаючись в конструктор вихованця як параметр.


# ----------------------------
# Тема 5: Kомпозиція
# ----------------------------
class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Задача: {self.name}, Опис: {self.description}")


class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list(Task) = []

    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))

    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def display_project_info(self):
        print(f"Проект: {self.name}")
        for task in self.tasks:
            task.display_info()


# Створення проекту
my_project = Project("Веб-розробка")  # Веб-розробка

# Додавання задач
my_project.add_task(
    "Дизайн інтерфейсу", "Створити макет головної сторінки."
)  # Дизайн інтерфейсу", "Створити макет головної сторінки.
my_project.add_task(
    "Розробка API", "Реалізувати ендпоінти для користувачів."
)  # Розробка API", "Реалізувати ендпоінти для користувачів.

# Відображення інформації про проект
my_project.display_project_info()  # Веб-розробка

# Видалення задачі
my_project.remove_task("Розробка API")

# Перевірка видалення задачі
my_project.display_project_info()  # Дизайн інтерфейсу", "Створити макет головної сторінки.


# ----------------------------
# Тема 6: Власні винятки
# ----------------------------
# Визначення власного класу винятку
class AgeVerificationError(Exception):
    def __init__(self, message="Вік не задовольняє мінімальній вимозі"):
        self.message = message
        super().__init__(self.message)


# Функція для перевірки віку
def verify_age(age: int):
    if age < 18:
        raise AgeVerificationError("Вік особи меньший за 18 років")


if __name__ == "__main__":
    # Обробка винятку
    try:
        verify_age(16)  # Змініть вік для різних результатів
    except AgeVerificationError as e:
        print(f"Виняток: {e}")
    else:
        print(
            "Вік перевірено, особа доросла."
        )  # Виняток: Вік особи меньший за 18 років


class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError("Name is too short, need more than 2 symbols")
    if not name[0].isupper():
        raise NameStartsFromLowError("Name should start from capital letter")
    return name


if __name__ == "__main__":
    try:
        name = enter_name()
        print(f"Hello, {name}")
    except (NameTooShortError, NameStartsFromLowError) as e:
        print(e)
