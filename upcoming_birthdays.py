from datetime import date
from typing import List, Dict

def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    pass

users = [
    {"name": "John Doe", "birthday": "1985.03.09"},
    {"name": "Jane Smith", "birthday": "1990.03.10"},
    {"name": "Michael Brown", "birthday": "1987.03.11"},
    {"name": "Emily White", "birthday": "1995.03.12"},
    {"name": "David Wilson", "birthday": "1992.03.13"},
    {"name": "Sophia Miller", "birthday": "1988.03.14"},
    {"name": "Daniel Taylor", "birthday": "1991.03.15"},
    {"name": "Olivia Thomas", "birthday": "1993.03.16"},
    {"name": "James Anderson", "birthday": "1986.03.17"},
    {"name": "Charlotte Martinez", "birthday": "1994.03.18"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
