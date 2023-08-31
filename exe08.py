paisA = 80000
paisB = 200000
taxaA = 3/100
taxaB = 1.5/100

anos = 0
while paisA <= paisB:
    paisA += paisA * taxaA
    paisB += paisB * taxaB
    #paisA *= 1 + taxaA
    #paisB *= 1 + taxaB
    anos += 1

print(f'Serão necessários {anos} anos para o país A ultrapassar ou igualar a população do país B.')