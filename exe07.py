
while True:

    print(f'{"":=^45}')
    while True:
        num = int(input('Digite um valor inteiro entre 1 e 10: '))
        if 1 <= num <= 10:
            break
        else:
            print(f'Erro: Você deve digitar um valor inteiro entre 1 e 10!')

    while True:
        print(f'{"Menu":=^45}')
        print(f'(a) - Tabuada da Multiplicação')
        print(f'(b) - Tabuada da Divisão')
        print(f'(c) - Tabuada da Soma')
        print(f'(d) - Tabuada da Subtração')
        print(f'{"":=^45}')

        opcao = str(input('Escolha a opção desejada: ')).lower()
        if 'a' <= opcao <= 'd':
            break
        else:
            print(f'Erro: Você deve digitar uma opção entre "a" e "d"!')

    match opcao:
        case 'a':
            print(f'Tabuada da Multplicação')
            for i in range(1, 11):
                print(f'{num} x {i} = {num * i}')
        case 'b':
            print(f'Tabuada da Divisão')
            final = (num * 10) + 1
            for i in range(num, final, num):
                print(f'{i} / {num} = {i / num:.0f}')
        case 'c':
            print(f'Tabuada da Soma')
            for i in range(1, 11):
                print(f'{num} + {i} = {num + i}')
        case 'd':
            print(f'Tabuada da Subtração')
            for i in range(1, 11):
                print(f'{num + i} - {num} = {(num + i) - num}')


    while True:
        sair = str(input('\nDeseja sair do programa: S ou N: ')).lower()
        if sair != 's' and sair != 'n':
            print(f'Erro: Você deve digitar S ou N!')
        else:
            break

    if sair == 's':
        print(f'Você saiu do programa!')
        break