carros = ["Fusca", "Gol", "Uno", "Focus"]

marcas = ("Fiat", "Ford", "Honda")

print (carros , marcas)
print("---------------------------------------------------------")

carros.append("Sandeiro")       # Para adicionar valores em uma lista

print (   len(carros)   )             # Para Saber o comprimento

carros.remove(carros[1])
carros.remove("Uno")        #Caso não tenha esse item na lista ele retorna um Erro
#carros.pop()               #Remove o ultimo item da lista
#del carros[2]              #remove o indice especifico da lista
#carros.clear()             #Limpa a lista
print("---------------------------------------------------------")

if("Tesla" in carros):
    carros.remove("Tesla")
else:
    print ("Don\'t have a Tesla in list Carros\n")

print (carros)
print("\n---------------------------- CLONAGEM OU APONTAR PARA O MESMO OBJETO")
carrosApotadorDeVar = carros      #Não copia e sim aponta para o mesmo objeto
carrosClonado = list(carros)      #Clona a lista
carros.clear()
print (carrosApotadorDeVar)
print(carrosClonado)

print("\n---------------------------- FUNDINDO DUAS LISTAS")

carrosFundido = carrosClonado + carrosClonado   
print (carrosFundido)

carrosFundido =  carrosClonado + carrosClonado
print (carrosFundido)

lista = {1, 2, 3}
lista2 = {2, 3 , 4, 5}

lista.update(lista2)    

print (lista)

"""
A |= B para juntar dois conjuntos em Python.
A.update(B) para juntar dois conjuntos em Python.
A.union(B) para juntar dois conjuntos em Python.
reduce(operator.or_, [A, B]) para unir dois conjuntos em Python.
"""