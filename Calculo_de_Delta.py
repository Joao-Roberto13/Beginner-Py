#O programa deve achar os X de uma equação quadratica
#A pessoa deve introduzir os valores de a, b e c.
#No final a aplição deve informar os valores dos X

import math

print('*********************************')
print('Bem vindo ao calculo do X1 e X2')
print('*********************************')

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO: Usuário preferiu não digitar.\033[m')
            return 0
        else:
            return n

print('________________________________________')
a = leiaInt('Digite o valor de `a´ aqui: ')
print('________________________________________')
b = leiaInt('Digite o valor de `b´ aqui: ') 
print('________________________________________')
c = leiaInt('Digite o valor de `c´ aqui: ') 
print('________________________________________')

D = (b) * (b) - 4 * (a) * (c)

if D >= 0:
    num = D
    raiz = math.sqrt(num)

    X1 = (-1 * (b) + raiz) / (2 * a)
    X2 = (-1 * (b) - raiz) / (2 * a)

    print('O valor de Delta = %.1f'
    %(D))

    print('O valor de X1 = %.1f'
    %(X1))

    print('O valor de X2 = %.1f'
    %(X2))
    K = input('Clique Enter para Terminar: ')

else:
    print('O valor de Delta = %.1f'%(D))
    print('A equação não tem solução')
    K = input('Clique Enter para Terminar: ')
