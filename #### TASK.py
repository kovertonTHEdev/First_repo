

########## ДЗ -1 
from datetime import datetime

date = "2020-10-09"
def get_days_from_today(date):
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d") 
    except ValueError:
        return 
    current_date = datetime.today()
    days_count = current_date.toordinal() - formatted_date.toordinal()
    return days_count

########## ДЗ -2
get_numbers_ticket(min, max, quantity)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

