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
