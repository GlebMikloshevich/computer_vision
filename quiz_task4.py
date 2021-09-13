import random

number_list = [random.uniform(100, -100) for _ in range(10)]

print(sorted(number_list, key=lambda number: abs(number) % 1))
