soma = 0
for i in range(500):
    if i % 2 != 0:
        if i % 3 == 0:
            soma += i

print(soma)