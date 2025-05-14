senha=123
contador=0
while(True):
    senha=int(input("Digite a senha: "))
    if(senha==123):
        print("Senha correta")
        break
    else:
        print("Senha incorreta")
        contador=contador+1
        if(contador==5):
            print("Tentativas esgotadas")
            break


