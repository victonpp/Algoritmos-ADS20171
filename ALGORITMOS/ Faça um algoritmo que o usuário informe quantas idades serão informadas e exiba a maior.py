x=int(input("Informe quantas idades vai digitar? "))
cont=0
maior=0
while (cont<x):
    i=int(input("Informe a idade: "))
    if(i>maior):
        maior=i
    cont=cont+1
print("Maior idade= ",maior)
