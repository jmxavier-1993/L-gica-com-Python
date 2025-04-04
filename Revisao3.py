soma_notas = 0
for i in range(0,4):
  nota = float(input(f"Digite a  nota do aluno: "))
  soma_notas += nota
               
        
media = soma_notas / 4

if media >= 7:
    print("Aprovado")
elif 5 <= media <= 6.9:
    print("Recuperação")
else:
    print("Reprovado")