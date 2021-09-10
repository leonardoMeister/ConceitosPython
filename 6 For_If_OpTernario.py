if True:
    global maca
    maca = "Leonardo Margoti Meister"

if (len(maca)  < 10    and len(maca) > 0): #Enta entre 10 e 0
    #nada
    pass
elif (len(maca)  > 10   or len (maca) < 10):   #Entra se for maior que 10 ou menor que 10
    print ("Entrou aqui baby")
else:
    #Nada
    pass

x = 10                                              # OPERADOR TERNARIO
#        Condição      ?            :
x = (  (x % 2 == 0)   and "verdade" or "false")
print (x)


x = "leonardo"
a = ""
for c in x:
    print (a+c)
    a = c

