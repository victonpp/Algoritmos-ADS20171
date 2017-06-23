from random import randint
n1=randint(1,9)
n2=int(input("Tente adivinhar um número entre 0 e 10: "))
while  n2<n1:
    n2=int(input("O número secreto é maior. Digite novamente um número entre 0 e 10: "))
while n2>n1:
    n2=int(input("O número secreto é menor. Digite novamente um número entre 0 e 10: "))
if n2==n1:
    print("Acertou!!!")
