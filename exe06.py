from math import pi

while True:
    print(f'{"Menu":=^30}')
    print(f'T - Cálculo área do triângulo')
    print(f'Q - Cálculo área do quadrado')
    print(f'R - Cálculo área do retângulo')
    print(f'C - Cálculo área do círculo')
    print(f'S - Sair')
    print(f'{"":=^30}')

    opcao = ''
    while opcao != 't' and opcao != 'q' and opcao != 'r' and opcao != 'c' and opcao != 's':
        opcao = str(input('Digite sua opção: ')).lower()
        if opcao != 't' and opcao != 'q' and opcao != 'r' and opcao != 'c' and opcao != 's':
            print(f'Você só pode escolher: T, Q, R, C ou S!')

    match opcao:
        case 't':
            print(f'{"Cálculo área Triângulo":=^30}')
            while True:
                base = float(input('Digite o valor da base: '))
                if base <= 0:
                    print(f'Não são permitidos valores negativos ou iguais a zero!')
                else:
                    break
            while True:
                altura = float(input('Digite o valor da altura: '))
                if altura <= 0:
                    print(f'Não são permitidos valores negativos ou iguais a zero!')
                else:
                    break
            area = (base * altura) / 2
            print(f'Área do Triangulo: ({base} x {altura})/2 = {area:.2f} ')
        case 'q':
            print(f'{"Cálculo área Quadrado":=^30}')
            while True:
                lado = float(input('Digite o valor do lado: '))
                if lado <= 0:
                    print(f'Não são permitidos valores negativos ou iguais a zero!')
                else:
                    break
            area = lado ** 2
            print(f'Área do Quadrado: ({lado})² = {area:.2f} ')
        case 'r':
            print(f'{"Cálculo área Retângulo":=^30}')
            while True:
                base = float(input('Digite o valor da base: '))
                if base <= 0:
                    print(f'Não são permitidos valores negativos ou iguais a zero!')
                else:
                    break
            while True:
                altura = float(input('Digite o valor da altura: '))
                if altura <= 0:
                    print(f'Não são permitidos valores negativos ou iguais a zero!')
                else:
                    break
            area = base * altura
            print(f'Área do Retângulo: ({base} x {altura}) = {area:.2f} ')
        case 'c':
            print(f'{"Cálculo área Círculo":=^30}')
            while True:
                raio = float(input('Digite o valor do raio: '))
                if raio <= 0:
                    print(f'Não são permitidos valores negativos ou iguais a zero!')
                else:
                    break
            area = pi * (raio ** 2)
            print(f'Área do Retângulo: ({pi:.2f} x {raio}²) = {area:.2f} ')

    if opcao == 's':
        print(f'Você saiu do programa!')
        break



