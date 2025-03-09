import re

def normalize_phone(phone_number: str) -> str:
    pattern = re.compile(r'\D')
    clean_phone_number= re.sub(pattern, '',  phone_number)

    correct_phone_number =  re.sub(r'^(?:380|80|0)?', '+380', clean_phone_number)
    return correct_phone_number

raw_numbers = [
    "067\\t123 45+67",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "80-    12345.  67",
    "880-----1234567"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(f'Sanitized numbers: {sanitized_numbers}')
