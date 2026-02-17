# ----------------------------
# Тема 1: Іменовані кортежі
# ----------------------------
import collections

# Створення іменованого кортежу Person
Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# Виведення різних атрибутів іменованого кортежу
print(person.first_name)   # Mick    
print(person.post_index) # 01146
print(person.age)     # 35   
print(person[3])  # Boston       


import collections

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Simon', 4, 'Krabat')

print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}') # This is a cat Simon, 4 age, his owner Krabat


# ----------------------------
# Тема 2: Counter
# ----------------------------

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1

print(mark_counts) # {4: 4, 2: 2, 6: 3, 7: 2, 3: 2, 5: 2, 1: 3}


import collections

student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)

print(mark_counts.most_common()) # [(4, 4), (6, 3), (1, 3), (2, 2), (7, 2), (3, 2), (5, 2)]
print(mark_counts.most_common(1)) # [(4, 4)]
print(mark_counts.most_common(2)) # [(4, 4), (6, 3)]


from collections import Counter

# Створення Counter з рядка
letter_count = Counter("banana")
print(letter_count) # Counter({'a': 3, 'n': 2, 'b': 1})


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = Counter(words)

# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")

# Виведення: 
# the: 2
# quick: 1
# brown: 1
# fox: 1
# jumps: 1
# over: 1
#lazy: 1
# dog: 1


# ----------------------------
# Тема 3: Deafaultdict
# ----------------------------
from collections import defaultdict

# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)

# Додавання елементів до списку для кожного ключа
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d) # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})


d = defaultdict(int)

# Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 1
d['a'] += 1

print(d) # defaultdict(<class 'int'>, {'a': 2, 'b': 1})


words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

print(grouped_words) # {'a': ['apple', 'appendix'],'z': ['zoo'], 'l': ['lion', 'lama'], 'b': ['bear', 'bet'], 'w': ['wolf']}


from collections import defaultdict

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list) # Щоб не перевіряти, чи є список на цю літеру в словнику grouped_words, ми можемо скористатися defaultdict із collections та задати значенням за замовчуванням порожній список

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words)) # {'a': ['apple', 'appendix'],'z': ['zoo'], 'l': ['lion', 'lama'], 'b': ['bear', 'bet'], 'w': ['wolf']}


# ----------------------------
# Тема 4: Стек
# ----------------------------

# Створення стеку
def create_stack():
    return []

# Перевірка на порожнечу
def is_empty(stack):
    return len(stack) == 0

# Додавання елементу
def push(stack, item):
    stack.append(item)

# Вилучення елементу
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")

# Перегляд верхнього елемента
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")


### Спочатку створимо стек та додамо декілька елементів:
stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')

### Тепер стек містить елементи ['a', 'b', 'c'], де 'c' є на вершині стеку.
print(peek(stack))  # Переглянемо верхній елемент: Виведе 'c'
print(pop(stack))  # Видалимо верхній елемент: Виведе 'c'


# ----------------------------
# Тема 5: Черга
# ----------------------------
from collections import deque

# Створення черги
queue = deque()

# Enqueue: Додавання елементів
queue.append('a')
queue.append('b')
queue.append('c')

print("Черга після додавання елементів:", list(queue))

# Dequeue: Видалення елемента
print("Видалений елемент:", queue.popleft())

print("Черга після видалення елемента:", list(queue))

# Peek: Перегляд першого елемента
print("Перший елемент у черзі:", queue[0])

# IsEmpty: Перевірка на порожнечу
print("Чи черга порожня:", len(queue) == 0)

# Size: Розмір черги
print("Розмір черги:", len(queue))

# Виведення:
# Черга після додавання елементів: ['a', 'b', 'c']
# Видалений елемент: a
# Черга після видалення елемента: ['b', 'c']
# Перший елемент у черзі: b
# Чи черга порожня: False
# Розмір черги: 2


# ----------------------------
# Тема 6: Двостороння черга deque
# ----------------------------
from collections import deque

# Створення пустої двосторонньої черги
d = deque()

# Додаємо елементи в чергу
d.append('middle')  # Додаємо 'middle' в кінець черги
d.append('last')    # Додаємо 'last' в кінець черги
d.appendleft('first')  # Додаємо 'first' на початок черги

# Виведення поточного стану черги
print("Черга після додавання елементів:", list(d)) # Черга після додавання елементів: ['first', 'middle', 'last']

# Видалення та виведення останнього елемента (з правого кінця)
print("Видалений останній елемент:", d.pop()) # Видалений останній елемент: last

# Видалення та виведення першого елемента (з лівого кінця)
print("Видалений перший елемент:", d.popleft()) # Видалений перший елемент: first

# Виведення поточного стану черги після видалення елементів
print("Черга після видалення елементів:", list(d)) # Черга після видалення елементів: ['middle']


from collections import deque

d = deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d) # deque([5, 6, 7, 8, 9], maxlen=5)


from collections import deque

d = deque(maxlen=5) # можливість обмежити розмір Deque
for i in range(10):
    d.append(i)

print(d) # deque([5, 6, 7, 8, 9], maxlen=5)


from collections import deque

# Список завдань, де кожне завдання - це словник
tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]

# Ініціалізація черги завдань
task_queue = deque()

# Розподіл завдань у чергу відповідно до їх пріоритету
for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)  # Додавання на високий пріоритет
        print(f"Додано швидке завдання: {task['name']}")
    else:
        task_queue.append(task)  # Додавання на низький пріоритет
        print(f"Додано повільне завдання: {task['name']}")

# Виконання завдань
while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")

# Вивід:
# Додано швидке завдання: Помити посуд
# Додано повільне завдання: Подивитись серіал
# Додано швидке завдання: Вигуляти собаку
# Додано повільне завдання: Почитати книгу
# Виконується завдання: Вигуляти собаку
# Виконується завдання: Помити посуд
# Виконується завдання: Подивитись серіал
# Виконується завдання: Почитати книгу


# ----------------------------
# Тема 7: Двостороння черга deque
# ----------------------------
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3")) # True
print(Decimal("0.1") + Decimal("0.2")) # 0.3


from decimal import Decimal, getcontext

getcontext().prec = 6
print(Decimal("1") / Decimal("7")) # 0.142857

getcontext().prec = 8
print(Decimal("1") / Decimal("7")) # 0.14285714


from decimal import Decimal, getcontext

getcontext().prec = 6 # Виведення буде саме 6 значущих цифр.
print(Decimal("233") / Decimal("7")) # 33.2857


from decimal import ROUND_DOWN, Decimal

# Вихідне число Decimal
number = Decimal('3.14159')

# Встановлення точності до двох знаків після коми
rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN) # У цьому прикладі число 3.14159 округляється до 3.14 з використанням методу quantize, шаблон для точності використовується Decimal('0.00')
# режим округлення встановлено як rounding=ROUND_DOWN

print(rounded_number)


import decimal
from decimal import Decimal
 
number = Decimal("1.45")

# Округлення за замовчуванням до одного десяткового знаку
print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0"))) # Округлення за замовчуванням ROUND_HALF_EVEN: 1.4

# Округлення вверх при нічиї (ROUND_HALF_UP)
print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP)) # Округлення вгору ROUND_HALF_UP: 1.5

# Округлення вниз (ROUND_FLOOR)
print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR)) # Округлення вниз ROUND_FLOOR: 1.4

# Округлення вверх (ROUND_CEILING)
print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING)) # Округлення вгору ROUND_CEILING: 1.5

# Округлення до трьох десяткових знаків за замовчуванням
print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000"))) # Округлення до трьох десяткових знаків: 3.142


# ----------------------------
# Тема 8: Генератори
# ----------------------------
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

# Використання next()
print(next(gen))  # Виведе 1
print(next(gen))  # Виведе 2
print(next(gen))  # Виведе 3


from pathlib import Path
def read_lines(file_path):
    BASE = Path(__file__).resolve().parent
    file_path = BASE / "my_file.txt"
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            yield line.strip()

# Використання генератора для читання рядків з файлу
for line in read_lines("my_file.txt"):
    print(line)








