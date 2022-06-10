print('\nBem vindo a calculadora de média!')
n1 = float(input('\nInsira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
n3 = float(input('Insira a segunda nota: '))
n4 = float(input('Insira a segunda nota: '))
s = n1 + n2 + n3 +n4
média = (n1 + n2 + n3 + n4) / 4
print('A soma das notas {}, {}, {} e {} é: {}!\nA média do aluno é: {:.2f}!'.format(n1, n2, n3, n4, s, média))
if(média>=7):
    print('Parabéns, você está aprovado!🥳\u2764\uFE0F')
else:
    print('Que pena, você está reprovado!\U0001f494\U0001f972')
