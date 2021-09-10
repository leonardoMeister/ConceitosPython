
#FUNÇÕES ANONIMAS
r =  lambda a , b: a+b
print( r(10,20))

multiplica = lambda a,b,c: (a+b)*c
print(multiplica(10,10,2))

#JÁ EXECUTA A FUNÇÃO
res = (lambda a,b: a+b)(3,2)
print(res)


#UMA LAMBDA QUE TEM COMO PARAMETRO UMA FUNÇÃO FUNC
porcentagem = lambda    x,func     :     x+func(x)
#IMPRIMINDO A LAMBDA 
#PASSANDO 100 E UMA EXPRESSAO, A VAR VALOR SE REFERE A X      e na primeira lambda ele usa o X dentro de func
print( porcentagem(100       ,           lambda VALOR    :    VALOR*0.1  ))