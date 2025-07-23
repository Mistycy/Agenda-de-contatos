import os
import json


arquivo = "agenda.json"


def carregar_agendas():
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
                return json.load(f)

def salvar_agendas(agendas):
    with open (arquivo, "w", encoding="utf-8") as f:
        json.dump(agendas, f, indent=4, ensure_ascii=False)

def adicionar_contato(agendas=None):
            agenda = carregar_agendas()
            nome = input("nome do contato: ")
            email = input("email do contato: ")
            telefone = input("telefone do contato: ")
            pessoa = {'nome': nome, "email": email, 'telefone': telefone}
            agenda.append(pessoa)
            salvar_agendas(agenda)
            print("contato adicionado com sucesso!")


def listar_contatos():
        agendas = carregar_agendas()
        print("\nLista de Contatos:")
        for i, contato in enumerate(agendas, 1):
            nome = contato.get("nome", "")
            email = contato.get("email", "")
            telefone = contato.get("telefone", "")
            print(f"{i}. Nome: {nome} | Email: {email} | Telefone: {telefone}")

def apagar_contato(agendas=None):

    try:
        agendas = carregar_agendas()
        indice = int(input("digite qual contato deseja remover: "))
        if 1 <= indice <= len(agendas):
            contato_removido = agendas.pop(indice - 1)
            salvar_agendas(agendas)
            print(f"contato: '{contato_removido}' removido com sucesso.")
        else:
            print("Número inválido.")
    except ValueError:
            print("Entrada inválida. Digite um número.")


def menu():
      while True:
        print("---------------------------")
        print("1 - Adicionar novo contato")
        print("2 - Deletar contato")
        print("3 - Listar contatos")
        print("4 - Sair")
        print("---------------------------")
        escolha = int(input("qual opção você deseja? "))

        if escolha == 1:
             adicionar_contato()
        elif escolha == 2:
             apagar_contato()
        elif escolha == 3:
             listar_contatos()
        elif escolha == 4:
             break
menu()