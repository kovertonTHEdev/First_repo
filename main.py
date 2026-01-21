# Greeting
print("Hello World!")
print("Hello Git")

# Name check
name = input("Enter your name: ").strip()

banned_names = ["володимир", "путін", "росія", "росіянин", "тварина"]

if name.lower() in banned_names:
    print("Good evening, we are from Ukraine")
else:
    print(f"Hello, {name}!")

# Age check
age = int(input("\nHow old are you? "))

if age < 18:
    print("Access denied")
else:
    print("Access granted")

# Square perimeter calculation
side = float(input("\nEnter side length: "))
perimeter = 4 * side
print(f"Perimeter of the square is {perimeter}")

# Shopping calculation
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
