numeropar = []
numeroimpar=[]
for i in range(0,10):
    adicionar= int(input("digite um numero"))
    if(adicionar%2==0):
     numeropar.append(adicionar)
    else:
     numeroimpar.append(adicionar)
print(numeropar)    
print(len(numeropar))
