from datetime import datetime

def get_days_from_today(date: str) -> int:
    current_date = datetime.now()
    props_date = datetime.strptime(date, '%Y-%m-%d')
    try:
        renge = (current_date - props_date).days
        return renge
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: {e}')
    return 0

date = '2020-10-09'
res = get_days_from_today(date)
print(f'res: {res}')
