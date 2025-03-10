from datetime import date, datetime, timedelta
from typing import List, Dict

def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    # current_date = datetime.today().date()
    current_date = date(2024, 12, 29)
    date_after_7_days = current_date + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_birthday_this_year = date(current_date.year, user_birthday.month, user_birthday.day)

        if user_birthday_this_year < current_date and date_after_7_days.month == 1 and user_birthday.month == 1:
            user_birthday_this_year = date(current_date.year + 1, user_birthday.month, user_birthday.day)

        if current_date <= user_birthday_this_year <= date_after_7_days:
            user_birthday_day_week = user_birthday_this_year.weekday()
            if (user_birthday_day_week == 5):
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": (user_birthday_this_year + timedelta(days=2)).strftime("%Y.%m.%d")
                })
            elif user_birthday_day_week == 6:
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": (user_birthday_this_year + timedelta(days=1)).strftime("%Y.%m.%d"),
                })
            else:
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": user_birthday_this_year.strftime("%Y.%m.%d"),
                })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.12.29"},
    {"name": "Jane Smith", "birthday": "1990.01.01"},
    {"name": "Michael Brown", "birthday": "1987.01.04"},
    {"name": "Emily White", "birthday": "1995.03.14"},
    {"name": "David Wilson", "birthday": "1992.03.16"},
    {"name": "Sophia Miller", "birthday": "1988.03.17"},
    {"name": "Daniel Taylor", "birthday": "1991.03.23"},
    {"name": "Olivia Thomas", "birthday": "1993.03.30"},
    {"name": "James Anderson", "birthday": "1986.04.01"},
    {"name": "Charlotte Martinez", "birthday": "1994.04.04"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
