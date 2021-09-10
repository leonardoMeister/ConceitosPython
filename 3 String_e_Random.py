import random

x = [
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60)
]


print(x[0])
print(x[1])
print(x[2])
print(x[3])

print("----------------------------------------------------------- STRING")

umaString = "    leonardo Margoti Meister        "

print ( x[0:3] )
print (umaString.strip()[ 0 : 8 ])
print (umaString.lower())
print(umaString.upper())

print (umaString.replace("leo" , "Ber"))
print (umaString.split ( " " ))

print("---------------------------------------")

nome = "Leonardo Margoti Meister"

res = "Leonardo" in nome
print (res)

res = "Leonardo" not in nome
print (res)