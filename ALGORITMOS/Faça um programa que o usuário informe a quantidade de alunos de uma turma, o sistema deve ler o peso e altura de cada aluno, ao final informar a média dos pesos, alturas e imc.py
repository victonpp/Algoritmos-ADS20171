N=int(input("Digite a quantidade de alunos:"))
x=0
PT=0
HT=0
IMCT=0
while x<N:
    x=x+1
    P=int(input("Digite o peso do aluno:"))
    H=float(input("Digite a altura do aluno:"))
    IMC=P/H**2
    print(IMC)
    PT=PT+P
    HT=HT+H
    IMCT=IMCT+IMC
print("Média do peso dos alunos= %2.2f" %(PT/N))
print("Média da altura dos alunos= %2.2f" %(HT/N))
print("Média do imc dos alunos= %2.2f" %(IMCT/N))
