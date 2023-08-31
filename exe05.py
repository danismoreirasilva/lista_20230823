while True:
    novoSal = 0
    valorAumento = 0
    percentual = 0
    while True:
        salarioAtual = float(input('Digite o salário atual: R$ '))
        if salarioAtual <= 0:
            print(f'O salário não pode ser valor <= zero!')
        else:
            break

    if salarioAtual < 1000:
        novoSal = salarioAtual * 1.12
        valorAumento = 0.12 * salarioAtual
        percentual = 12
    elif salarioAtual <= 2000:
        novoSal = salarioAtual * 1.10
        valorAumento = 0.10 * salarioAtual
        percentual = 10
    elif salarioAtual <= 3500:
        novoSal = salarioAtual * 1.08
        valorAumento = 0.08 * salarioAtual
        percentual = 8
    elif salarioAtual <= 5000:
        novoSal = salarioAtual * 1.04
        valorAumento = 0.04 * salarioAtual
        percentual = 4
    else:
        novoSal = salarioAtual
        valorAumento = 0
        percentual = 0

    if percentual == 0:
        print(f'Para o salário R$ {salarioAtual:.2f} não há aumento!')
    else:
        print(f'Para o salário de R$ {salarioAtual:.2f}')
        print(f'{percentual}% de aumento')
        print(f'Novo Salário R$ {novoSal:.2f}')
        print(f'Aumento de R$ {valorAumento:.2f}')

    while True:
        continuar = str(input('Deseja realizar nova consulta: (s)im | (n)ão: ')).lower()
        if continuar != 's' and continuar != 'n':
            print(f'Você deve digitar somente S ou N!')
        else:
            break

    if continuar == 'n':
        print(f'Você saiu do programa!')
        break