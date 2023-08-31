somaPrimo = 0
listaPrimos = ''
for i in range(2, 16):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        somaPrimo += i
        listaPrimos += str(i) + ','

print(f'Números primos do intervalo [2,15]')
print(f'A soma dos números primos é: {somaPrimo}')
print(f'Os números primos deste intervalo são: {listaPrimos}')



