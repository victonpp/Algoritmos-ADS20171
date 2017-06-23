ano=int(input("Digite o ano: "))
x=ano%4
if x==0:
    c=ano%100
    if c!=0:
        d=ano%400
        if d==0:
            print("Ano bissexto")
        else:
            print("Ano bissexto")
else:
    print("Não é bissexto")
