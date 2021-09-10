num1 = num2 = num3 = res = 10
"""
Todas as variaveis tem o mesmo valor
"""

def declaraVarGlobal():
    global variavelGlobal
    variavelGlobal = "Essa eh uma var global que foi declarada e instanciada dentro da funcao"


#Chamando a função para fazer a declaração
declaraVarGlobal()
print (variavelGlobal)
