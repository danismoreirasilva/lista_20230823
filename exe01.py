while True:

    while True:
        num = int(input('Digite um número inteiro e positivo: '))
        if num < 0:
            print(f'Não são permitidos números negativos!')
        else:
            break

    if num > 1:
        #parte inteira da divisão num//2
        for i in range(2, num//2 + 1):
            if num % i == 0:
                print(f'O número {num} não é primo!')
                break
        else:
            print(f'O número {num} é primo!')
    else:
        print(f'O número {num} não é primo!')

    while True:
        continuar = str(input('Deseja realizar nova consulta: (S)im | (N)ao: ')).lower()
        if continuar != 's' and continuar != 'n':
            print(f'Você deve digitar (S) para Sim ou (N) para Não!')
        else:
            break


    if continuar == 'n':
        print(f'Você saiu do programa!')
        break
