while True:
    print(f'{"Sistema Bancário":=^54}')
    print(f'Valor de Empréstimo: entre R$ 1.000,00 e R$ 50.000,00')
    print(f'Quantidade de Parcelas: entre 6 e 36')
    print(f'{"":=^54}')

    rendaMensal = 0
    while rendaMensal <= 0:
        rendaMensal = float(input(f'Valor da Renda Mensal: R$ '))
        if rendaMensal <= 0:
            print(f'O valor da sua renda deve ser maior do zero!')

    valorEmp = 0
    while not 1000 <= valorEmp <= 5000:
        valorEmp = float(input(f'Valor do Empréstimo: R$ '))
        if not 1000 <= valorEmp <= 5000:
            print(f'O valor do empréstimo deve estar entre R$ 1.000,00 e R$ 5.000,00!')

    qtdParcelas = 0
    while not 6 <= qtdParcelas <= 36:
        qtdParcelas = int(input(f'Quantidade de parcelas: '))
        if not 6 <= qtdParcelas <= 36:
            print(f'A quantidade de parcelas deve estar entre 6 e 36!!')

    rendaMaxima = rendaMensal * 0.3
    valorParcela = valorEmp / qtdParcelas

    if valorParcela <= rendaMaxima:
        print(f'Empréstimo Aprovado!')

    else:
        print(f'Empréstimo Reprovado!')

    print(f'Renda Mensal: R$ {rendaMensal:.2f}')
    print(f'Valor do Empréstimo: R$ {valorEmp:.2f}')
    print(f'Valor Parcela Máxima: R$ {rendaMaxima:.2f}')
    print(f'Valor Parcela Mensal: R$ {valorParcela:.2f}')
    print(f'Quantidade de parcelas: {qtdParcelas}')

    while True:
        continuar = str(input('Deseja continuar - (S)im | (N)ão: ')).lower()
        if continuar != 's' and continuar != 'n':
            print(f'Você deve digitar S ou N!')
        else:
            break

    if continuar == 'n':
        print(f'Você saiu do programa!')
        break