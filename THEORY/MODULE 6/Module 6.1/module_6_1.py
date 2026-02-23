# ----------------------------
# Тема 1: Основи ООП в Python
# ----------------------------
class User:
    name = "Anonymous"
    age = 15


user1 = User()
print(user1.name)  # Anonymous
print(user1.age)  # 15

user2 = User()
user2.name = "John"
user2.age = 90

print(user2.name)  # John
print(user2.age)  # 90


class Person:
    def __init__(
        self, name: str, age: int
    ):  # Mетод __init__() — спеціальний метод-конструктор, який автоматично виконується під час створення кожного нового екземпляра на базі класу Person. Ім'я методу починається і закінчується двома символами підкреслення.
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f"Hi! I am {self.name} and I am {self.age} years old.")

    def set_age(self, age: int) -> None:
        self.age = age


bob = Person("Boris", 34)

bob.say_name()  # Hi! I am Boris and I am 34 years old.
bob.set_age(25)
bob.say_name()  # Hi! I am Boris and I am 34 years old.


class Person:
    count = 0

    def __init__(self, name: str):
        self.name = name  # Змінна name належить об'єкту та є змінною об'єкту, і надає значення за допомогою self. Його значення для кожного об'єкту своє.
        Person.count += 1  # Тут count належить класу Person і є атрибутом класу. Його значення завжди одне й те саме для любого об'єкту класу.

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")


first = Person("Boris")
first.how_many_persons()  # Кількість людей зараз 1
second = Person("Alex")
first.how_many_persons()  # Кількість людей зараз 2


class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form


# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")


# ----------------------------
# Тема 2: Інкапсуляція
# ----------------------------
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active  # <- захищене поле

    def greeting(self):
        return f"Hi {self.name}"


p = Person("Boris", 34, True)
print(p.name, p.age, p._is_active)  # <- не можна його змінювати, приклад неправ підходу
print(p.greeting())


class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(
        self,
    ):  # Ми додали метод is_active, щоб отримати доступ для читання захищеного атрибута _is_active

        return self._is_active

    def set_active(
        self, active: bool
    ):  # метод set_active для зміни значення захищеного атрибута _is_active
        self._is_active = active


p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active())
print(p.greeting())


class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin


p = Person("Boris", 34, True, False)
print(p.get_is_admin())  # False
p.set_is_admin(True)
print(p.get_is_admin())  # True


# ----------------------------
# Тема 3: Наслідування
# ----------------------------
class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"


class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof"


class Cow(Animal):
    def make_sound(self):
        return "Moo"


my_cat = Cat("Simon", 4)
my_dog = Dog("Rex", 5)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # Виведе "Meow"
print(my_dog.make_sound())  # Виведе "Woof"
print(my_cow.make_sound())  # Виведе "Moo"


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"


class Dog(Animal):
    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Викликаємо конструктор базового класу
        self.breed = breed  # Додаємо нову властивість

    def make_sound(self) -> str:
        return "Woof"

    def chase_tail(self) -> str:
        return f"{self.nickname} is chasing its tail!"


class Cow(Animal):
    def make_sound(self):
        return "Moo"


my_cat = Cat("Simon", 4)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # Виведе "Meow"
print(my_cow.make_sound())  # Виведе "Moo"

my_dog = Dog("Rex", 5, "Golden Retriever")
print(my_dog.make_sound())  # Виведе "Woof"
print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"


# ----------------------------
# Тема 4: Багаторівневе наслідування та Method Resolution Order (MRO)
# ----------------------------
class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Bird(Animal):
    def make_sound(self):
        return "Chirp"


class Parrot(Bird):
    def can_fly(self):
        return True


class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"


my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound())
print(my_parrot.can_fly())
print(my_parrot.say_phrase("Hello, World!"))


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())  # Виведе порядок розв'язання методів для класу D
### Це порядок MRO для класу D який означає, що Python спочатку шукатиме методи в D, потім у B, за ними в C, потім в A, і, нарешті, в вбудованому базовому класі object, який є предком всіх класів.


class A:
    name = "Я клас A"


class B:
    name = "Я клас B"
    property = "Я знаходжусь в класі B"


class C(A, B):
    property = "Я знаходжусь в класі C"


c = C()
print(c.name)  # Я клас A

print(c.property)  # Я знаходжусь в класі C


class A:
    name = "Я клас A"


class B:
    name = "Я клас B"
    property = "Я знаходжусь в класі B"


class C(B, A):
    property = "Я знаходжусь в класі C"


c = C()
print(c.name)
print(c.property)


# ----------------------------
# Тема 5: Поліморфізм та качина типізація
# ----------------------------
class Duck:
    def quack(self):
        print("Quack, quack!")


class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")


def make_it_quack(duck):
    duck.quack()


duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)


class Dog:
    def speak(self) -> str:
        return "Woof"


class Cat:
    def speak(self) -> str:
        return "Meow"


class Robot:
    def speak(self) -> str:
        return "Beep boop"


def make_it_speak(
    speaker,
) -> None:  # У цьому прикладі, качина типізація дозволяє нам передавати будь-який об'єкт, який має метод speak,
    # у функцію make_it_speak, не зважаючи на його конкретний клас.
    print(speaker.speak())


dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop


from typing import Protocol


class Speaker(
    Protocol
):  # Результат буде той самий але статична типізація за допомогою typing.Protocol використовується для вказівки,
    # що параметр speaker повинен відповідати інтерфейсу, який має метод speak.
    def speak(self) -> str:
        pass


class Dog:
    def speak(self) -> str:
        return "Woof"


class Cat:
    def speak(self) -> str:
        return "Meow"


class Robot:
    def speak(self) -> str:
        return "Beep boop"


def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())


dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop
