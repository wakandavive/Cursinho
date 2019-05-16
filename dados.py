from random import randint

dado1 = randint(1, 6)
dado2 = randint(1, 6)
dado3 = randint(1, 6)
dado4 = randint(1, 6)

jogador1 = dado1 + dado2
jogador2 = dado3 + dado4

print("Jogador 1")
print("primeiro dado:", dado1)
print("segundo dado:", dado2)
print("\tTotal:", jogador1)

print("\nJogador 2")
print("Primeiro dado:", dado3)   
print("Segundo dado:", dado4)
print("\tTotal:", jogador2)

if jogador1 > jogador2:
    print("Jogador 1 venceu.")
elif jogador2 > jogador1:
    print("Jogaador 2 vendeu")
else:
    print("Houve empate")    