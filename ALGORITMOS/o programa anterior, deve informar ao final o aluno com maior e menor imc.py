N=int(input("Digite a quantidade de alunos:"))
x=0
PT=0
HT=0
IMCT=0
IMCmaior=0
IMCmenor=10000
while x<N:
    x=x+1
    P=int(input("Digite o peso do aluno:"))
    H=float(input("Digite a altura do aluno:"))
    IMC=P/H**2
    if IMC>IMCmaior:
        IMCmaior=IMC
    if IMC<IMCmenor:
        IMCmenor=IMC
    PT=PT+P
    HT=HT+H
    IMCT=IMCT+IMC
print("Média do peso dos alunos= %2.2f" %(PT/N))
print("Média da altura dos alunos= %2.2f" %(HT/N))
print("Média do imc dos alunos= %2.2f" %(IMCT/N))
print("Aluno com maior imc= %2.2f" %(IMCmaior))
print("Aluno com menor imc= %2.2f" %(IMCmenor))
