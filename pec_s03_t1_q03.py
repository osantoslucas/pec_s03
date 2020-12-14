print('CORES DO SINAL'
      '[V] Verde'
      '[A] Amarelo'
      '[E] Vermelho')
sinal = str(input('Qual a cor do sinal? ').upper())
if sinal == 'V':
    print('SIGA!')
elif sinal == 'A':
    print('ATENÇÃO!')
elif sinal == 'E':
    print('PARE!')
else:
    print('Comando Inválido. Tente Novamente.')
