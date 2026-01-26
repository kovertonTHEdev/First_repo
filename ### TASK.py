RUN_INPUT = False

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


#### TASK  (Первірка віку)
if RUN_INPUT:
    age_input = int(input(" \nPlease, Enter your age: " ))

    if age_input < 18:
        print("Acess Denied")
    else:
        print("Access Granted")


### TASK (Сортування)
if RUN_INPUT: 
    nums = input(" Please, enter numbers: ")
    nums = nums.split()

    numbers = []

    for n in nums:
        numbers.append(int(n))

    sorted_nums = sorted(numbers)

    print(sorted_nums)

### TASK (Сортування)
nums = [ 5, 2, 9, 1, 3]
nums.sort()
print(nums)


### TASK 
nums = [5, 2, 9, 1, 3]
nums_copy = nums.copy()
nums_copy.sort()

print(nums)
print(nums_copy)

### TASK
words = ["banana", "Apple", "cherry"]
words.sort(key=len)
print(words)

### TASK
words = ["  Banana", "apple  ", "  Cherry ", "apple"]

clean_words = []

for w in words:
    clean_words.append(w.strip().lower())

clean_words.sort()

print(clean_words)



### TASK
words = ["Apple", "banana", "apple", "Cherry", "banana"]
good_words = []

for w in words:
    good_words.append(w.strip().lower())

good_words.sort()

count_3 = good_words.count("apple")


print(good_words)
print(count_3)


### TASK
words = ["apple", "banana", "apple", "cherry", "banana"]
d_words = []
d_words.sort()
d_words = set(words)
words = list(d_words)

print(words)

### TASK

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
result = {}

for w in words:
    current = result.get(w, 0)
    result [w] = current + 1


print(result)

### TASK
nums = [3, 1, 4, 1, 5, 9, 2, 3]
d_lst = set(nums)
nums = list(d_lst)
nums.sort()

print(nums)

### TASK
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers [::-1]
print(reverse_numbers)

### TASK
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = numbers[1:10:2]
print(even_numbers)

### TASK
nums = [3, 1, 4, 1, 5, 9, 2]
nums_copy = nums[:]
nums_copy.sort(reverse=True)

print(nums)
print(nums_copy)



### TASK
numbers = [5, 12, 7, 3, 9, 2, 10, 6]
numbers_copy = numbers[:]
numbers_copy = numbers[0:10:2] 
numbers_copy.sort(reverse=True)

print(nums)
print(numbers_copy)

### TASK
if RUN_INPUT:
    allowed_events = ["deploy", "build", "test", "backup"]
    event_type = input("Text please type of event: ")
    event_time = int(input("Text please duration time: "))
    if event_type: allowed_events 
    else: 
        print("Unknown event")
    if event_time < 0:
        print("Invalid duration")

    h = event_time // 3600
    m = (event_time % 3600) // 60
    s = event_time % 60

    print(f"Event {event_type}: {h}h {m}m {s}s")

### TASK
if RUN_INPUT:
    events = ["start", "stop", "restart"]
    event_type = input("Text here please type of event: ")
    event_time1 = int(input("Text please duration time: "))
    if event_type not in events:
        print("Invalid type")
    elif event_time1 < 0:
        print("Invalid duration")

    else:
        h = event_time1 // 3600
        m = (event_time1 % 3600) // 60
        s = event_time1 % 60

    print(f"Event {event_type}: {h}h {m}m {s}s")

### TASK
raw_users = ["  Andrii ", "", "BORIS", "anna", "  ", "Boris", "ANNA"]

clean_users = []

for r in raw_users:
    name = r.strip().lower()
    if name:
        clean_users.append(name)

clean_users = list(set(clean_users))
clean_users.sort()

print(clean_users)

### TASK
raw_actions = ["  Login", "logout ", "LOGIN", "", "  ", "Logout", "login", "Delete"]

clean_actions = []  # сюда будем складывать очищенные действия

# 1. Очистка данных
for r in raw_actions:
    action = r.strip().lower()      # убираем пробелы и приводим к нижнему регистру
    if action:                      # проверяем, что строка не пустая
        clean_actions.append(action)  # добавляем в список

# 2. Удаление дубликатов
clean_actions = list(set(clean_actions))
# set() убирает повторы, list() возвращает обратно список

# 3. Сортировка по алфавиту
clean_actions.sort()

# 4. Вывод результата
for action in clean_actions:
    print(action)

### TASK 
actions = [" Login", "logout ", "LOGIN", "update", "Logout", "", "login"]

clean_actions = []      # список для очищенных действий (без пробелов, в нижнем регистре)
result = {}             # словарь-счётчик: действие -> сколько раз встретилось

# 1. Очистка исходного списка
for action in actions:
    action = action.strip().lower()   # убираем пробелы и приводим к нижнему регистру
    if action:                        # проверяем, что строка не пустая
        clean_actions.append(action)  # добавляем очищенное действие в список

# 2. Подсчёт количества действий
for action in clean_actions:
    if action in result:              # если действие уже есть в словаре
        result[action] += 1           # увеличиваем счётчик на 1
    else:                             # если действия ещё нет
        result[action] = 1            # создаём ключ и ставим начальное значение 1

# 3. Вывод результата
print(result)