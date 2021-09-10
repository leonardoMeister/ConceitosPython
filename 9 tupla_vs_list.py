tupla = ("carro", "moto", "bicicleta")

for x in tupla:
    print(x)

#Itens de tupla não podem ser modificados nem adicionados.

print ("______________________________________________")

l_secundaria = list(tupla)
l_secundaria.append("nada a ver")

tupla = tuple(l_secundaria)

for x in tupla:
    print(x)
