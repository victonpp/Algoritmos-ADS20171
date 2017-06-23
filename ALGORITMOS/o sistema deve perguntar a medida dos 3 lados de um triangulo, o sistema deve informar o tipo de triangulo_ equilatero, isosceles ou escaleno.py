A1=int(input("Informe a medida do triângulo:"))
A2=int(input("Informe a medida do triângulo:"))
A3=int(input("Informe a medida do triângulo:"))
if A1==A2==A3:
    print("Equilátero")
elif A1==A2 or A2==A3 or A1==A3:
    print("Isósceles")
else:
    print("Escaleno")

