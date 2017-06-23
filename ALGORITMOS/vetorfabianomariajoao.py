from random import randint
l=["fabiano","joão","maria"]
s=["1","2","3"]
x=randint(0,2)
cont=0
print(x)
print(l[x])
while cont<3:
    resp=input("Digite a senha:")
    if resp==s[x]:
        print("Acesso Liberado")
        break
    cont=cont+1
