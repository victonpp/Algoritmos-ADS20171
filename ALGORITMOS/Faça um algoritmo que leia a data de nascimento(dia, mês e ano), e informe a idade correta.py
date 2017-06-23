DATAnasc=input("Informe a data de nascimento [dd/mm/aaaa]: ")
DATAatual=input("Informe a data atual [dd/mm/aaaa]: ")
i=int(DATAatual[6:10])-int(DATAnasc[6:10])
if DATAatual[3:5]>DATAnasc[3:5]:
    print(i,"anos")
elif DATAatual[3:5]<DATAnasc[3:5]:
    (print(i-1,"anos"))
elif DATAatual[3:5]==DATAnasc[3:5]:
    if DATAatual[0:2]>=DATAnasc[0:2]:
        print(i,"anos")
    else:
        (print(i-1,"anos"))