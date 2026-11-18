total_despesa = 0
contador = 0


while True:    
    valor_despesa = float(input('Informe a despesa: '))   

    total_despesa = total_despesa + valor_despesa 
    contador += 1

    resposta = input('\nQuer continuar [S/N]?: ').upper()

    if resposta == 'N':
        break



print(f'Valor total da despesa {total_despesa}')
print(f'Quantidade de despesa {contador}')



