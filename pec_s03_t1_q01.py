nome = input('Insira o nome: ')
print('''SEXO:
[1] MASCULINO
[2] FEMININO
''')
sexo = int(input('Qual o sexo? '))
if sexo ==1:
    print(f'Ilmo Sr.{nome}')
elif sexo == 2:
    print(f'Ilma Sra.{nome}')
else:
    print('Código Inválido. Tente Novamente.')
