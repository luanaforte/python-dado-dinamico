import random 

resultados = [0] * 6

for _ in range(100):
    roll = random.randint(1, 6)
    resultados[roll - 1] += 1

# exibir o número de vezes que cada valor apareceu
for i, contagem in enumerate(resultados, start=1):
    print(f'{i} | {contagem}')
    