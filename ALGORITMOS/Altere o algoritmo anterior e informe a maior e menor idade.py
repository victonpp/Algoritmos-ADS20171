x=int(input("Informe quantas idades vai digitar? "))
cont=0
maior=0
menor=1000
while (cont<x):
    i=int(input("Informe a idade: "))
    if(i>maior):
        maior=i
    if(i<menor):
        menor=i
    cont=cont+1
print(maior)
print(menor)
