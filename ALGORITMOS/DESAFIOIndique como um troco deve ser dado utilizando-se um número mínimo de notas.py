conta=int(input("Digite o valor da conta: "))
pago=int(input("Digite o valor pago: "))
troco=pago-conta
cinquenta=0
vinte=0
dez=0
cinco=0
dois=0
um=0
if troco==0:
    print("Não tem troco")
if troco<0:
    print("Valor pago menor que o valor da conta")
if troco>0:

    if troco//50>0:
        cinquenta=troco//50
        troco=troco-(cinquenta*50)

    if troco//20>0:
        vinte=troco//50
        troco=troco-(vinte*20)

    if troco//10>0:
        dez=troco//10
        troco=troco-(dez*10)

    if troco//5>0:
        cinco=troco//5
        troco=troco-(cinco*5)

    if troco//2>0:
        dois=troco//2
        troco=troco-(dois*2)

    if troco//1>0:
        um=troco//1
        troco=troco-(um*1)
        print(cinquenta,"notas de 50")
        print(vinte,"notas de 20")
        print(dez,"notas de 10")
        print(cinco,"notas de 5")
        print(dois,"notas de 2")
        print(um,"notas de 1")
