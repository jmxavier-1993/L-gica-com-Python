import sys

preco_ovos = 22
preco_manteiga = 10
preco_trigo = 6
preco_acucar = 5
preco_leite = 3
preco_fermento = 2

def tem_ingrediente(tem_ovos, tem_manteiga, tem_trigo, tem_acucar, tem_leite, tem_fermento):
    preco_ingredientes = 0
    if tem_ovos:
        preco_ingredientes += preco_ovos
    if tem_manteiga:
        preco_ingredientes += preco_manteiga
    if tem_trigo:
        preco_ingredientes += preco_trigo
    if tem_acucar:
        preco_ingredientes += preco_acucar
    if tem_leite:
        preco_ingredientes += preco_leite
    if tem_fermento:
        preco_ingredientes += preco_fermento
    return preco_ingredientes

if __name__ == "__main__":
    if len(sys.argv) != 7:  # Verifica se tem 6 argumentos + o nome do script (sys.argv[0])
        print("Erro: Você deve passar 6 argumentos (true/false para cada ingrediente).")
        print("Exemplo: python somaIngrediente.py true false true true false true")
        sys.exit(1)  # Encerra o programa com erro

    terminal_tem_ovos = sys.argv[1].lower() == "true"
    terminal_tem_manteiga = sys.argv[2].lower() == "true"
    terminal_tem_trigo = sys.argv[3].lower() == "true"
    terminal_tem_acucar = sys.argv[4].lower() == "true"
    terminal_tem_leite = sys.argv[5].lower() == "true"
    terminal_tem_fermento = sys.argv[6].lower() == "true"
    
    soma_ingredientes = tem_ingrediente(
        terminal_tem_ovos,
        terminal_tem_manteiga,
        terminal_tem_trigo,
        terminal_tem_acucar,
        terminal_tem_leite,
        terminal_tem_fermento,
    )
    print(soma_ingredientes)