nfinal = 0
while (nfinal <= 0):
  nfinal = int(input('Você quer que a série de Fibonacci vá até qual número '))
  if (nfinal <= 0):
    print('O número deve ser positivo!')
f1 = 1
print (f1)
f2 = 1
for i in range(1, nfinal):
  print(f2)
  f3 = f1 + f2
  f1 = f2
  f2 = f3
