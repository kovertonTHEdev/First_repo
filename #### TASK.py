from datetime import datetime

date = "2020-10-09"
def get_days_from_today(date):
    pass
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d") 
    except ValueError:
        return 
    result = get_days_from_today("2020-10-09")
    current_date = datetime.today()
    get_days_from_today = current_date.toordinal() - formatted_date.toordinal()
    return print(result)