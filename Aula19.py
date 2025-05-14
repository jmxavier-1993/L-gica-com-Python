soma=0
i=1
valorespares=[]

while(i!=0):
    i=int(input("Digite um numero:"))
    soma= soma+i
    if(i%2==0):
     valorespares.append(i)

print(f"{valorespares}") 
print(sum(valorespares))