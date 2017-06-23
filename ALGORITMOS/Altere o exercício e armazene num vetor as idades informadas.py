x=int(input("Informe Quantas idades vai digitar? "))
cont=0
Maior=0
menor=1000
i=[]
while (cont<x):
    i.append(int(input("Informe a idade")))
    if(i>Maior):
        Maior=i[cont]
    if(i<menor):
        menor=i[cont]
    cont=cont+1
print(Maior)
print(menor)

