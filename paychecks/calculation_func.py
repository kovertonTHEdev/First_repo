def total_salary (SALARIES_FILE): 
        with open(SALARIES_FILE, 'r', encoding='utf-8') as file: #відкриття файлу
            total = 0 # акумулятор
            count = 0 # акумулятор
            for line in file:
                cleaned_line = line.strip() # прибирає пробіли 
                parts = cleaned_line.split(",") # робить список імен + ЗП
                if len(parts) == 2: 
                    salary_text = parts[1]
                    try:
                         salary = int(salary_text)
                         total = total + salary # накопичення сум зарплат
                         count+=1 #накопичення акум
                    except ValueError:
                         continue
                    
        if count > 0:
             average = total / count # cереднє вираховуємо
        return (total, average)