#Media escolar

print('#################################################')
print('Bem Vindo ao programa de cálculo de média escolar')
print('#################################################')
nome = input('Digite seu nome: ') 
materia = input('Digite o nome da matéria: ')
print('Agora voce precisa informar as quatro notas')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4
if media < 10:
    print('Aluno %s, voce foi REPROVADO. Sua média em %s foi de %.1f.'
    %(nome, materia, media)) 

else:
    print('Parabens!!!')
    print('Aluno(a) %s, voce foi APROVADO. Sua média em %s foi de %.1f.'
    %(nome, materia, media))

