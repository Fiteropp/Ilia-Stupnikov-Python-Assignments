import random


def return_random_num(dice_faces: int):
    num = random.randint(1, dice_faces)
    return num

noppa = 0
i = 1


while True:
    try:
        user_input = int(input("Anna nopan tahkojen määrää: "))
        break


    except ValueError:
        print("Virheellinen syöte")


while noppa != user_input:
    noppa = return_random_num(user_input)
    print(f"Hetitto {i}: {noppa}")
    i += 1
