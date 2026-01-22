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
