
import random

lista = [0]

quantidade = int(input('digite a quantidade de pessoas que participarão do sorteio: '))

if quantidade == 2:
    lista.append(str(input('Digite o primeiro nome: ')))
    lista.append(str(input('Digite o segundo nome: ')))

elif quantidade == 3:
    lista.append(str(input('Digite o primeiro nome: ')))
    lista.append(str(input('Digite o segundo nome: ')))
    lista.append(str(input('Digite o terceiro nome: ')))

elif quantidade == 4:
    lista.append(str(input('Digite o primeiro nome: ')))
    lista.append(str(input('Digite o segundo nome: ')))
    lista.append(str(input('Digite o terceiro nome: ')))
    lista.append(str(input('Digite o quarto nome: ')))

elif quantidade == 5:
    lista.append(str(input('Digite o primeiro nome: ')))
    lista.append(str(input('Digite o segundo nome: ')))
    lista.append(str(input('Digite o terceiro nome: ')))
    lista.append(str(input('Digite o quarto nome: ')))
    lista.append(str(input('Digite o quinto nome: ')))

elif quantidade == 6:
    lista.append(str(input('Digite o primeiro nome: ')))
    lista.append(str(input('Digite o segundo nome: ')))
    lista.append(str(input('Digite o terceiro nome: ')))
    lista.append(str(input('Digite o quarto nome: ')))
    lista.append(str(input('Digite o quinto nome: ')))
    lista.append(str(input('Digite o sexto nome: ')))
    
elif quantidade == 7:
    lista.append(str(input('Digite o primeiro nome: ')))
    lista.append(str(input('Digite o segundo nome: ')))
    lista.append(str(input('Digite o terceiro nome: ')))
    lista.append(str(input('Digite o quarto nome: ')))
    lista.append(str(input('Digite o quinto nome: ')))
    lista.append(str(input('Digite o sexto nome: ')))
    lista.append(str(input('Digite o sétimo nome: ')))

elif quantidade == 8:
    lista.append(str(input('Digite o primeiro nome: ')))
    lista.append(str(input('Digite o segundo nome: ')))
    lista.append(str(input('Digite o terceiro nome: ')))
    lista.append(str(input('Digite o quarto nome: ')))
    lista.append(str(input('Digite o quinto nome: ')))
    lista.append(str(input('Digite o sexto nome: ')))
    lista.append(str(input('Digite o sétimo nome: ')))
    lista.append(str(input('Digite o oitavo nome: ')))

elif quantidade == 9:
    lista.append(str(input('Digite o primeiro nome: ')))
    lista.append(str(input('Digite o segundo nome: ')))
    lista.append(str(input('Digite o terceiro nome: ')))
    lista.append(str(input('Digite o quarto nome: ')))
    lista.append(str(input('Digite o quinto nome: ')))
    lista.append(str(input('Digite o sexto nome: ')))
    lista.append(str(input('Digite o sétimo nome: ')))
    lista.append(str(input('Digite o oitavo nome: ')))
    lista.append(str(input('Digite o nono nome: ')))

elif quantidade == 10:
    lista.append(str(input('Digite o primeiro nome: ')))
    lista.append(str(input('Digite o segundo nome: ')))
    lista.append(str(input('Digite o terceiro nome: ')))
    lista.append(str(input('Digite o quarto nome: ')))
    lista.append(str(input('Digite o quinto nome: ')))
    lista.append(str(input('Digite o sexto nome: ')))
    lista.append(str(input('Digite o sétimo nome: ')))
    lista.append(str(input('Digite o oitavo nome: ')))
    lista.append(str(input('Digite o nono nome: ')))
    lista.append(str(input('Digite o décimo nome: ')))



'''
else: 
    print('Você só pode escolher até 30 pessoas para o sorteio !')
'''

lista.remove(0)

sorteado = random.choice(lista)
print('='*55)
print('\n')
print(f'Os participantes do sorteio foram: {lista}.')
print('Destes, a pessoa sortuda foi',  sorteado.upper())
lista.remove(sorteado)
print('\n')
print(f'Continuam participando do sorteio: {lista}.' )
print('='*55)


while len(lista) != 1:

    print("Pressione enter para realizar um novo sorteio.")
    input()  # O algoritmo para aqui até você apertar Enter
    sorteado = random.choice(lista)
    print(f'Os participantes do sorteio de amigo secreto foram: {lista}.')
    print('Destes, o amigo secreto sorteado é:',  sorteado.upper())
    lista.remove(sorteado)
    print('\n')
    print(f'Continuam participando do sorteio de amigo secreto: {lista}.' )
    print('='*55)