import random

i = 0
ix = 0

num3_koodi = ""
num4_koodi = ""


while i < 3:
    rand_num = random.randint(0,9)
    num3_koodi += str(rand_num)
    i += 1

while ix < 4:
    rand_num = random.randint(1,6)
    num4_koodi += str(rand_num)
    ix += 1

print(f"3 numeroinen koodi: {num3_koodi}")
print(f"4 numeroinen koodi: {num4_koodi}")
