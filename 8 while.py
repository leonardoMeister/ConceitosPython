import os

#Limpando a tela
os.system('cls')

valor = int(input("Informe um numero de 1 a 10:"))

while 10 > valor:
    print ('asd')
    if valor == 8:
        print ("passando pelo valor 8")
    valor+=1
    if valor == 9:
        break

os.system('pause')
os.system('cls')

while(True):
    parada = input("Insira sim para sair: ")
    if parada.lower() == "sim":
        break
    print("Voce não informou sim")

os.system('pause')
os.system('cls')

carros = []
nomeCarro = input("Informe um carro:")
while nomeCarro != "-1":
    carros.append(nomeCarro)
    nomeCarro = input("Informe um novo carro:")

print ("\n-------------------------------------\n")
for x in carros:
    print(x)