import random

def get_numbers_ticket(min: int, max: int, quantity: int)->list:
    if quantity > (max - min + 1):    #  Питання до ментора - як краще повертати помилку чи порожній масив?
        return []
    if not ( 1<= min < max <= 1000):
        return []
    if not (min <= quantity <= max):
        return []

    random_list = random.sample(range(min, max + 1), quantity)
    return sorted(random_list)

lottery_numbers = get_numbers_ticket(6, 9, 7)
print(f'Ваші виграшні номери: {lottery_numbers}')


