valorespares=[]   

for i in range(1,6):
  numero=int(input("Digite um numero: "))
  if(numero%2==0):
     valorespares.append(numero)

print(f"{valorespares}") 