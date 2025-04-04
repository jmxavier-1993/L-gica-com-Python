ano=2025
maioresdeidade=[]   
menoresdeidade=[]

for i in range(1,8):
  numero=int(input("Digite seu ano de nascimento: "))
  idade=ano-numero
  if(idade>=18):
     maioresdeidade.append(numero)
  else:
     menoresdeidade.append(numero)

print(f"{len(maioresdeidade)}") 