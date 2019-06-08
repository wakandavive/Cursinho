from random import randint

matéria = input("escolha a matéria:")
print("você escolheu %s" % matéria)
print("VOCÊ ESTÁ PREPARADO!!!!....")
print("LOADING....//LOADING")

notas1 = randint(0, 10)
notas2 = randint(0, 10)



print('Notas 1:,', notas1)
print('Notas 2:,', notas2)




soma_divide = notas1  + notas2 / 2

média_para_passar = 7

if soma_divide > média_para_passar:
    print('aprovado')
else:
    print('reprovado')
