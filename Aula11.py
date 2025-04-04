tamanhoPizza= input("Digite o tamanho da pizza:[G][M][P] ").upper().strip()[0]
valortamanhoPizza=0
if(tamanhoPizza=="G"):
    valortamanhoPizza=30
elif(tamanhoPizza=="M"):
    valortamanhoPizza=25
elif(tamanhoPizza=="P"):
    valortamanhoPizza=15 
else:
    print("Tamanho de pizza inválido!")

saborPizza= int(input("Digite o sabor da pizza: [1]Calabresa [2]frango [3]portuguesa[4]mussarela [5]bacon"))
valorsaborPizza=0
if(saborPizza==1):
    valorsaborPizza=0
elif(saborPizza==2):
    valorsaborPizza=0
elif(saborPizza==3):
    valorsaborPizza=0
elif(saborPizza==4):
    valorsaborPizza=8
elif(saborPizza==5):
    valorsaborPizza=8
else:
    print("Sabor de pizza inválido!")
    
bordaPizza=int(input("Digite a borda da pizza: [1]sem borda [2]com borda")) 
valorbordaPizza=0

if(bordaPizza==1):
    valorbordaPizza=0
elif(bordaPizza==2):
    valorbordaPizza=4
else:
    print("borda de pizza inválido!")
    
fretePizza= int(input("Digite o frete da pizza: [1]sem frete [2]com frete"))
valorfretePizza=0

if(fretePizza==1):
    valorfretePizza=0
elif(fretePizza==2):
    valorfretePizza=5
else:
    print("frete de pizza inválido!")
    
valortotalpizza=valortamanhoPizza+valorsaborPizza+valorbordaPizza+valorfretePizza
print(f"O valor da pizza eh:{valortotalpizza}")