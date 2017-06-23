from random import randint
l=[["fabiano","joão","maria"],["1","2","3"]]
x=randint(0,2)
cont=0
print(x)
print(l)

print(l[0][x])
print(l[1][x])
while cont<3:
    resp=input("Digite a senha:")
    if resp==l[1][x]:
        print("Acesso Liberado")
        break
    cont=cont+1
