nota1 = int(input('Insira a PRIMEIRA nota: '))
nota2 = int(input('Insira a SEGUNDA nota: '))
nota3 = int(input('Insira a TERCEIRA nota: '))

media = (nota1 + nota2 + nota3) / 3
media_pontoExtra = ((nota1 + nota2 + nota3) / 3) + 1

if media_pontoExtra > 10:
    print('Média 10.')
elif nota3 > 8:
    print(f'A média do aluno é {media + 1}.')
elif media < 8:
    print(media)
