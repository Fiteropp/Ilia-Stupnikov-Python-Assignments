import random


def return_random_num():
    num = random.randint(1, 6)
    return num

noppa = 0
i = 1

while noppa != 6:
    noppa = return_random_num()
    print(f"Hetitto {i}: {noppa}")
    i += 1
