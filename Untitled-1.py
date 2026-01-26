### TASK
raw_actions = ["  Login", "logout ", "LOGIN", "", "  ", "Logout", "login", "Delete"]
clean_actions = []

for r in raw_actions:
    action = r.strip().lower()
    if action:                              ### нижній регістр та прибирання пробілів
        clean_actions.append(action) 

clean_actions = list(set(clean_actions))  ### прибирання дублікатів
clean_actions.sort() ### сортування за алфавітом) 
result = {
1: "one",
2: "two",
3: "three"
}

for key in clean_actions:
    print(key)

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

