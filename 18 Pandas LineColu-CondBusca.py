import pandas

dicionarioAlunos = {'Nome':["leonardo","verônica","Clemir"],
                    'Nota':[10,9.5,7],
                    'idade':[20,41,43]}

alunosDF = pandas.DataFrame(dicionarioAlunos)


print(alunosDF.describe())      #Funciona para campos numericos, e realiza varias contas com eles
print( alunosDF.shape)          #tamanho Linhas / Colunas
print("-------------------")    
print(alunosDF)


print("-------------------")    
print(alunosDF['Nome'])         # Usar o nome da coluna para puxar apenas essa coluna

print("-------------------")    
print(alunosDF.loc[   [0,2]   ]  )    # Seleciona apenas uma lista determinada, ou apenas um indece 
print(alunosDF.loc[1:2]  )            # Seleciona uma faixa de itens do dataFrame

print("-----------------------------")

print(alunosDF.loc[  'leonardo' == alunosDF["Nome"] ])    # Passando uma condição de busca

print("-----------------------------------------------")

        #Axis = 1 COLUNA ,    Axis =0 LINHA
alunosDF = alunosDF.drop('Nome',axis=1)             #DELETANDO COLUNAS 
print(alunosDF)
print("-----------------------------------------------")
alunosDF = alunosDF.drop( 0, axis=0 )               #DELETANDO LINHAS
print(alunosDF)
