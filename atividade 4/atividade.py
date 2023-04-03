
lista_compras = []


def exibir_lista_compras():
    print("Lista de Compras:")
    for item in lista_compras:
        print("-", item)

def adicionar_item():
    item = input("Digite o nome do item que deseja adicionar: ")
    lista_compras.append(item)
    print("Item adicionado com sucesso!")

def remover_item():
    item = input("Digite o nome do item que deseja remover: ")
    if item in lista_compras:
        lista_compras.remove(item)
        print("Item removido com sucesso!")
    else:
        print("O item não está na lista de compras.")

while True:
    
    print("\nO que você deseja fazer?")
    print("1. Exibir lista de compras")
    print("2. Adicionar item à lista de compras")
    print("3. Remover item da lista de compras")
    print("4. Sair do programa")
    
    escolha = input("Digite o número da opção desejada: ")
    
    if escolha == "1":
        exibir_lista_compras()
    elif escolha == "2":
        adicionar_item()
    elif escolha == "3":
        remover_item()
    elif escolha == "4":
        print("Obrigado por usar a lista de compras!")
        break
    else:
        print("Opção inválida. Tente novamente.")