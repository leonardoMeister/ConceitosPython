lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


#MAP
resultadoMap = list (map( lambda x: ((x*x)*0.1) , lista))

#LIST COMPREHENSION
#                              O que fazer            onde fazer
resultadoListComprehension = [ ((x*x)*0.1)          for x in lista]

def decodificar(x):
    x += x+"/"
    return x

meuNomeSoletrado = [decodificar(x)  for x in "Leonardo Margoti Meister"]

print (resultadoMap)
print("-----------------------")
print(resultadoListComprehension)
print(meuNomeSoletrado)