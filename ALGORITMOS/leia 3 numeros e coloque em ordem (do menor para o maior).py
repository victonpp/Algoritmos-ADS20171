N1=int(input("Digite o primeiro número:"))
N2=int(input("Digite o segundo número:"))
N3=int(input("Digite o terceiro número"))
if  N1<=N2<=N3:
   print(N1,+N2,+N3)
elif N2<=N1<=N3:
   print(N2,+N1,+N3)
elif N3<=N1<=N2:
   print(N3,+N1,+N2)
elif N1>=N2>=N3:
   print(N3,+N2,+N1)
elif N2>=N1>=N3:
   print(N3,+N1,+N2)
elif N3>=N1>=N2:
   print(N2,+N1,+N3)