while True:
    precoR = float(input('Digite o preço do KW/h Residencial: R$ '))
    if precoR <= 0:
        print(f'Erro: O valor deve ser maior do que zero!')
    else:
        break

while True:
    precoC = float(input('Digite o preço do KW/h Comercial: R$ '))
    if precoC <= 0:
        print(f'Erro: O valor deve ser maior do que zero!')
    else:
        break

while True:
    precoI = float(input('Digite o preço do KW/h Industrial: R$ '))
    if precoI <= 0:
        print(f'Erro: O valor deve ser maior do que zero!')
    else:
        break

while True:
    nConsumidores = int(input('Digite a quantidade de consumidores: '))
    if nConsumidores <= 0:
        print(f'Erro: A quantidade de consumidores deve ser maior do que zero!')
    else:
        break

contR = contI = contC = preco = 0
somaKwR = somaKwI = somaKwC = 0

for i in range(nConsumidores):
    idConsumidor = int(input('Digite o ID do consumidor: '))
    qteKwMensal = int(input('Digite a quantidade de KWh mensal: '))

    while True:
        print(f'Tipo de consumidor')
        print(f'R - Residencial')
        print(f'C - Comercial')
        print(f'I - Industrial')
        tipoConsumidor = str(input('Digite o tipo de consumidor: ')).lower()
        if tipoConsumidor != 'r' and tipoConsumidor != 'c' and tipoConsumidor != 'i':
            print(f'Erro: Você deve informar o tipo de consumidor: R, C ou I!')
        else:
            break

    match tipoConsumidor:
        case 'r':
            contR += 1
            somaKwR += qteKwMensal
            precoTotal = qteKwMensal * precoR
        case 'c':
            contC += 1
            somaKwC += qteKwMensal
            precoTotal = qteKwMensal * precoC
        case 'i':
            contI += 1
            somaKwI += qteKwMensal
            precoTotal = qteKwMensal * precoI

    print(f'{i+1}º Consumidor')
    print(f'Id consumidor: {idConsumidor}')
    print(f'Tota a pagar: R$ {precoTotal} ')

print(f'Resumo')
print(f'Foram {nConsumidores} consumidores')
print(f'Qte consumidores Residencial: {contR}')
print(f'Qte consumidores Comercial: {contC}')
print(f'Qte consumidores Industrial: {contI}')
print(f'Total de Kwh Residencial: {somaKwR}')
print(f'Total de Kwh Comercial: {somaKwC}')
print(f'Total de Kwh Industrial: {somaKwI}')
print(f'A média geral de consumo é { (somaKwI + somaKwR + somaKwC) / nConsumidores:.2f}')