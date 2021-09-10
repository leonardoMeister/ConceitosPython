import pandas , numpy
from pandas.core.construction import array

baseDados = pandas.read_csv('athlete_events.csv')

#print (baseDados.head(10))    #PARA IMPRIMIR APENAS O INICIO 

# USANDO DICIONARIO E CONVERTENDO PARA DATAFRAME
dicionarioAlunos = {'Nome':["leonardo","verônica","Clemir"],
                    'Nota':[10,9.5,7],
                    'idade':[20,41,43]}
objetoPandas3 = pandas.DataFrame(dicionarioAlunos)

# SERIES USANDO PANDAS
objetoPandas1 = pandas.Series([ 2 ,4 ,7, 8, 6])

# ARRAY USANDO NUMPAY
array1 = numpy.array([1,2,3,4])
array2 = numpy.array([(1,2,3,4), (11,22,33,44) ])

# CONVERTENDO UM ARRAY NUMPAY PARA PANDAS SERIES
objetoPandas2 = pandas.Series(array1) 

print(objetoPandas3)
print("----------------------")
print(objetoPandas1)
print("----------------------")
print(array1)
print("----------------------")
print(array2)
print("----------------------")
print(objetoPandas2)
