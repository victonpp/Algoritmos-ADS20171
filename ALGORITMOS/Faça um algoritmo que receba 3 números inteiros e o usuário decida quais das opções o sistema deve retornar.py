n1=float(input("Digite o primeiro número: "))
n2=float(input("Digite o segundo número: "))
n3=float(input("Digite o terceiro número: "))
op=int(input("Escolha 1 para a soma dos números, 2 para o maior número, 3 para o menor número e 4 para a média dos números: "))
op1=n1+n2+n3
op4=op1/3

if op==1:
    print("Soma dos números:",op1)
elif op==4:
    print("Média dos números:",op4)
elif op==2:
    if n1>n2 and n1>n3:
        print("Maior número:",n1)
    elif n2>n1 and n2>n3:
        print("Maior número:",n2)
    elif n3>n1 and n3>n2:
        print("Maior número:",n3)
else:
    if n1<n2 and n1<n3:
        print("Menor número:",n1)
    elif n2<n1 and n2<n3:
        print("Menor número:",n2)
    elif n3<n1 and n3<n2:
        print("Menor número:",n3)
