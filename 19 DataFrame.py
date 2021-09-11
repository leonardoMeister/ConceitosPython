import pandas
from pandas.core.frame import DataFrame

baseDados = pandas.read_csv('athlete_events.csv')
            
            #Como renomear COLUNAS DATA FRAME
selecaoOuro =  baseDados.loc[ baseDados['Medal'] == "Gold" ].rename(columns={   'Name' : 'Nome' , 'Sex':'Genero' , 'City':'Coidade' })
            #Forma Idependente
#selecaoOuro =  selecaoOuro.rename(columns={   'Name' : 'Nome' , 'Sex':'Genero' , 'City':'Coidade' })

age = selecaoOuro['Age']
# usando list Comprehesion para mudar valores 
ageAlterado = DataFrame ([ (x * 2)    for x in age])
ageAlterado = ageAlterado.rename( columns = {0:"Age"} )


print( baseDados['Medal'].value_counts()   )                            #Group by usando value_counts
print("-------------------------------------------------------------")

print ( type(baseDados['Medal']) )
print("-------------------------------------------------------------")

print(selecaoOuro.head(4))
print(type(selecaoOuro))
print("-------------------------------------------------------------")

print(age.head(4)) 
print (type(age))
print("-------------------------------------------------------------")

print(ageAlterado.head(4))
print(type(ageAlterado))
