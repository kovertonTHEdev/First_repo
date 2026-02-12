import os
def calculations (SALARIES_FILE): 
        with open(SALARIES_FILE, 'r', encoding='utf-8') as file: #відкриття файлу
            total = 0 # акумулятор
            count = 0 # акумулятор
            for line in file:
                cleaned_line = line.strip() # прибирає пробіли 
                parts = cleaned_line.split(",") # робить список імен + ЗП
                if len(parts) == 2:
                    first_name = parts[0] 
                    salary_text = parts[1]
                    try:
                         salary = int(salary_text)
                         total = total + salary
                         count+=1
                    except ValueError:
                         continue
                    
        if count > 0:
             average = total / count 
             return average 
        elif count == 0:
            average = 0
        return (total, average)