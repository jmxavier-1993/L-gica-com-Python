altura= float(input("Digite sua altura: ")) 

if(altura>1.45):
    print("Acesso liberado")
    idade= float(input("Digite sua idade: "))
    
    if(idade<12):
      print("Seu valor de ingresso custará R$ 5,00")
    elif(idade <18 ):
     print("Seu valor de ingresso custara R$ 10,00")
    else:
     print("Seu valor de ingresso custara R$ 15,00")
    
else:
    print("Nao pode entrar")