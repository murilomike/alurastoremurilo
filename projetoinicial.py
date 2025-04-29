mensagem = "Bem vindo ao Challenge Alura Store - By Murilo"

def exibir_mensagem():
    print(mensagem)
    print("Esse projeto foi desenvolvido para o desafio Alura Store")


lista = [Ana, Bia, Caio, Davi, Eva, Fabi, Gabi, Helo, Ivo, Ju]
def exibir_lista():
    for i in range(len(lista)):
        print(f"{i+1} - {lista[i]}")
        print(f"Nome: {lista[i].nome}")
        print(f"Idade: {lista[i].idade}")
        print(f"Sexo: {lista[i].sexo}")
        print(f"Endereço: {lista[i].endereco}")
def exibir_menu():
    print("Escolha uma opção:")