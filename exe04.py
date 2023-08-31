while True:
    maior = menor = meio = 0

    print(f'{"Digite os valores":=^55}')
    num1 = int(input('Digite o 1º valor: '))
    num2 = int(input('Digite o 2º valor: '))
    num3 = int(input('Digite o 3º valor: '))

    print(f'{"Escolha uma opção: ":=^55}')
    print(f'(1) Ordem crescente')
    print(f'(2) Ordem decrescente')
    print(f'(3) Valor maior entre os números digitados')
    print(f'{"":=^55}')

    while True:
        opcao = int(input('Digite sua opção: '))
        if 1 <= opcao <= 3:
            break
        else:
            print(f'Você digitou uma opção inválida! Valores válidos somente entre 1 e 3!!!')

    maior = menor = meio = num1

    if num2 < menor and num2 < num3:
        menor = num2
    elif num3 < menor and num3 < num2:
        menor = num3

    if num2 > maior and num2 > num3:
        maior = num2
    elif num3 > maior and num3 > num2:
        maior = num3

    if menor < num2 < maior:
        meio = num2
    elif menor < num3 < maior:
        meio = num3

    match opcao:
        case 1:
            print(f'Ordem crescente: {menor},{meio},{maior}')
        case 2:
            print(f'Ordem decrescente: {maior},{meio},{menor}')
        case 3:
            print(f'Ordem maior no meio: {menor},{maior},{meio}')

    continuar = ''
    while continuar != 's' and continuar != 'n':
        continuar = str(input('Deseja continuar - Digite S(Sim) | N(Não): ')).lower()
        if continuar != 's' and continuar != 'n':
            print(f'Você deve digitar somente: sim ou não!')

    if continuar == 'n':
        print(f'Você saiu do programa!')
        break
