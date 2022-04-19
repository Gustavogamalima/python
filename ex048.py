total = 0
n = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        total += c
        n += 1
print(f'A soma de todos os {n} valores solicitados é {total}')
