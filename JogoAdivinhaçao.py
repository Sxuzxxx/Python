from random import randint
from time import sleep

computador = randint(0, 5) #faz o computador pensar

print('-=-' * 20)

print('Vou pensar em um número entre 0 e 5. Tente')

print('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print(f'Parabéns, você acertou! Eu pensei no número {computador}')
    
else:
    print(f'Você errou! Eu pensei no número {computador} e não no {jogador}')
