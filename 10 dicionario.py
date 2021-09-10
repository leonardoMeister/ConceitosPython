import os

print("______________________________")


carro = {
    #key    =   value
    "fabricante" : "Honda",
    "Modelo" : "Hrmv",
    "Ano": "2021"
}
#ADICIONANDO UM NOVO ITEM
carro["jacare"] = "gosta de agua"

#REMOVENDO ITENS DICIONARIO
#carro.pop("Modelo")
del(carro["Modelo"])

#CONDIÇÕES EM DICIONARIOS
if "2021" in carro.values():
    print ("Existe o valor 2021 em carros")

if "Ano" in carro.keys():
    print ("Existe o ANO EM CARROS")

#PERCORRENDO VALORES USANDO FOR EM DICIONARIOS
print ("\nTodos os valores:")
for x in carro.values():
    print(x)

print("\nTodas as Chaves: ")
for x in carro.keys():
    print(x)

print("\nTanto chave e valor: ")
for x in carro.keys():
    print(x +" "+ carro[x])

print("\nTanto chave e valor: ")
for c,v in carro.items():
    print( c + " "+ v)


#ACESSANDO VALORES 
print(carro["Ano"])
print( carro.get("Modelo") )

#ALTERANDO VALORES
carro["Ano"] = "2031"

print (carro["Ano"])

