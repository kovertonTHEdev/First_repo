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
    name = input("Enter your name: ").strip()
    banned_names = ["володимир", "путін", "росія", "росіянин", "тварина"]

    if name.lower() in banned_names:
        print("Good evening, we are from Ukraine")
    else:
        print(f"Hello, {name}!")


# ================================
# 3. Age check (Перевірка віку)
# ================================

if RUN_INPUT:
    age = int(input("\nHow old are you? "))

    if age < 18:
        print("Access denied")
    else:
        print("Access granted")


# ================================
# 4. Square perimeter calculation
# (Обчислення периметра квадрата)
# ================================

if RUN_INPUT:
    side = float(input("\nEnter side length: "))
    perimeter = 4 * side
    print(f"Perimeter of the square is {perimeter}")


# ================================
# 5. Shopping calculation
# (Розрахунок вартості покупок)
# ================================

if RUN_INPUT:
    price_per_croissant = 1.04
    price_per_glass = 0.34
    price_per_coffee_pack = 4.42

    num_croissants = int(input("\nEnter quantity of croissants: "))
    num_glasses = int(input("Enter quantity of drinking glasses: "))
    num_coffee_packs = int(input("Enter quantity of coffee packs: "))

    total_cost = (
        num_croissants * price_per_croissant +
        num_glasses * price_per_glass +
        num_coffee_packs * price_per_coffee_pack
    )

    total_dollars = int(total_cost)
    total_cents = int(total_cost * 100) % 100

    print(f"Total price: {total_dollars} dollars and {total_cents} cents")


# ================================
# 6. List example + count()
# (Робота зі списком)
# ================================

my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази


my_list = [1, 2, 3, 4, 5]
print(len(my_list))

nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]


nums.sort(reverse=True)
print(nums)  # Виведе [9, 5, 4, 3, 2, 1, 1]


words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # Виведе ['apple', 'banana', 'cherry']


# ================================
# 7. sorted() vs sort()
# (Сортування без зміни оригіналу)
# ================================

nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)  # Виведе [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Виведе ['apple', 'banana', 'cherry']


# ================================
# 8. Dictionary basics
# (Робота зі словником)
# ================================

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["city"])  # Виведе 'New York'

my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)

del my_dict["age"]
print(my_dict)

print("name" in my_dict)
print("age" in my_dict)


# ================================
# 9. Set basics
# (Основи множин)
# ================================

numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}

numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)  # {1, 2}

numbers = {1, 2, 3}
numbers.discard(2)
print(numbers)  # {1, 3}


# ================================
# 10. Set operations
# (Операції над множинами)
# ================================

a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))  # {1, 2}
print(a - b)  # {1, 2}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)  # {1, 2, 4, 5}


a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}

my_frozenset = frozenset([1, 2, 3, 4, 5])


a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

union = a | b  # Об'єднання множин
intersection = a & b  # Перетин множин
difference = a - b  # Різниця множин
symmetric_difference = a ^ b  # Симетрична різниця

print(union)  # frozenset({1, 2, 3, 4, 5})
print(intersection)  # frozenset({3})
print(difference)  # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})


# ================================
# 11. String methods (Робота з рядками)
# ================================

s = "Hello world!"
print(s[0])# H
print(s[-1])# !


s = "Hello" 
print(s.upper()) # Виведе 'HELLO'

s = "Some Text"
print(s.lower())  # Виведе 'some text'

s = "Bill Jons"
print(s.startswith("Bi"))  # Виведе True

s = "hello.jpg"
print(s.endswith("jpg"))  # Виведе True

s = "hello world".capitalize()  # Результат: "Hello world"
print(s.capitalize())

s = "hello world".title()  # Результат: "Hello World"
print(s.title())


# ================================
# 12. String formatting (Форматування рядків)
# ================================

# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))


# ================================
# 13. Slices (Зрізи у Python)
# ================================

s = "Hello, World!"
first_five = s[:5]
print(first_five)  # Виведе 'Hello'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers[::-1]
print(reverse_numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers[:]
print(copy_numbers)



###  Home tasks
first_name = "Andrii"
last_name = "Nedoshivkin"
full_name = first_name+ " " +last_name 

print(full_name)


length = 2.75
width = 1.75
area = length * width
show = (f"With width {width} and length {length} of the room, its area is equal to {area}")



length =  "2.75"
width = "1.75"
area =  float(length) * float(width)
show = (f"With width {width} and length {length} of the room, its area is equal to {area}")

if RUN_INPUT:

    length = float(input("Enter length size"))
    width = float(input("Enter width size"))
    area = length * width


my_list = [2024, 3.12]
some_data = ['Python']
my_list.extend(some_data)
my_list.insert(1, "Python")
my_list.reverse()


#### TASK
age_input = int(input(" \nPlease, Enter your age: " ))

if age_input < 18:
    print("Acess Denied")
else:
    print("Access Granted")

