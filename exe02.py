from random import randint

nome1 = str(input('Digite o 1º nome: '))
nome2 = str(input('Digite o 2º nome: '))
nome3 = str(input('Digite o 3º nome: '))
nome4 = str(input('Digite o 4º nome: '))

sorteado = randint(1, 4)
print(sorteado)

match sorteado:
    case 1:
        print(f'O aluno sorteado foi: {nome1.title()}')
    case 2:
        print(f'O aluno sorteado foi: {nome2.title()}')
    case 3:
        print(f'O aluno sorteado foi: {nome3.title()}')
    case 4:
        print(f'O aluno sorteado foi: {nome4.title()}')
