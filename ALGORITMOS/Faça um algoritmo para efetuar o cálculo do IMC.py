S=(input("Você é H ou M?:"))
P=float(input("Digite seu peso:"))
Ha=float(input("Digite sua altura:"))
imc=P/(Ha**2)
print("imc= %2.2f"%(imc))
if S==M and imc<19.1:
    print("abaixo do peso")
elif imc<25.8:
    print("no peso normal")
elif imc<27.3:
    print("marginalmente acima do peso")
elif imc<=32.3:
    print("acima do peso ideal")
if S==H and imc<20.7:
    print("abaixo do peso")
elif imc<26.4:
    print("no peso normal")
elif imc<27.8:
    print("marginalmente acima do peso")
elif imc<=31:
    print("acima do peso ideal")

