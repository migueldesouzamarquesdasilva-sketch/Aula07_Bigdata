atingimento = 1
resposta = 'S'
meta = 2000
while resposta == 'S':
    vendas = float(input('\nDigite o número de vendas: '))
    

    atingimento = (vendas / meta) * 100

    print(f'\nValor vendido: {vendas}')
    print(f'\nPercentual de atingimento: {atingimento}%')

    resposta = input('\nQuer continuar: [S/N]: ').upper()

print('\nPrograma encerrado')
    




