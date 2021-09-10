
quadrado = lambda x: x*x
dezPorcentoDoQuadrado = lambda func,x : (func(x)*0.1)

resultado = dezPorcentoDoQuadrado(quadrado, 10)
print(resultado)

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
listaResultado = []

#APLICANDO A FUNÇÃO EM TODOS OS DADOS COM A FUNÇÃO MAP
resultadoMap = list (map( lambda x: ((x*x)*0.1) , lista))
resultadoMap2 = list (map( quadrado , lista))

# APLICANDO A FUNÇÃO EM TODOS OS DADOS COM FOR  
for x in lista:
    listaResultado.append(dezPorcentoDoQuadrado(quadrado , x))

#RESULTADOS IGUALS MESMO USANDO FOR OU MAP
print("--------------------")
print (lista)
print(listaResultado)
print (resultadoMap)
print (resultadoMap2)