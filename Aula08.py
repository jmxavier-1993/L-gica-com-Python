nota01=float(input("Digite a primeira nota:"))
nota02=float(input("Digite a segunda nota:"))
media=(nota01+nota02)/2
if(media>=7):
    print("Aprovado")
elif(media>=4):
        print("Recuperacao")
else:
    print("Reprovado")