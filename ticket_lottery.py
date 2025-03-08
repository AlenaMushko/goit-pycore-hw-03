import random

def get_numbers_ticket(min: int, max: int, quantity: int)->list:
    if not ( 1<= min < max <= 1000):
        raise []
    if not (min <= quantity <= max):
        raise []

    random_list = random.sample(range(min, max + 1), quantity)
    return sorted(random_list)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f'Ваші виграшні номери: {lottery_numbers}')


