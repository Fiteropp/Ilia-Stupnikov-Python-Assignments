import random
import time

i = 0
iterations = 1000000
dots_inside_circle = 0

start = time.time()
while i < iterations:

    x = random.uniform(-1,1)
    y = random.uniform(-1,1)


    if (x * x + y * y) < 1:
        dots_inside_circle += 1

    i += 1

pi_approx = (4 * dots_inside_circle) / i
end = time.time()
exec_time = (end - start) * 1000

print(f"Pi approx: {pi_approx}")
print(f"Exectution time: {exec_time:.6f} ms")
