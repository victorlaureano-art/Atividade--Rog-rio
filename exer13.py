import random

n = random.randint(1, 100)
p = 0

while p != n:
    p = int(input())
    if p < n:
        print("Maior")
    elif p > n:
        print("Menor")

print("Acertou")