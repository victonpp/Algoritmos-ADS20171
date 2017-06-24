numero=[]
par=[]
impar=[]
for i in range (4):
    digito=int(input("Digite um número: "))
    numero.append(digito)
    if (digito%2)==0:
        par.append(digito)
    else:
        impar.append(digito)
print(numero)
print(par)
print(impar)