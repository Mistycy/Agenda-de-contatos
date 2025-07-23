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
            nome = input("Nome do contato: ")
            email = input("Email do contato: ")
            telefone = input("Telefone do contato: ")
            pessoa = {'Nome': nome, "Email": email, 'Telefone': telefone}
            agenda.append(pessoa)
            salvar_agendas(agenda)
            print("Contato adicionado com sucesso!")


def listar_contatos():
        agendas = carregar_agendas()
        print("\nLista de Contatos:")
        for i, contato in enumerate(agendas, 1):
            nome = contato.get("Nome", "")
            email = contato.get("Email", "")
            telefone = contato.get("Telefone", "")
            print(f"{i}. Nome: {nome} | Email: {email} | Telefone: {telefone}")

def apagar_contato(agendas=None):

    try:
        agendas = carregar_agendas()
        indice = int(input("Digite a numeração do contato que deseja remover: "))
        if 1 <= indice <= len(agendas):
            contato_removido = agendas.pop(indice - 1)
            salvar_agendas(agendas)
            print(f"contato: '{contato_removido}' Removido com sucesso.")
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
        escolha = int(input("Qual opção você deseja? "))

        if escolha == 1:
             adicionar_contato()
        elif escolha == 2:
             apagar_contato()
        elif escolha == 3:
             listar_contatos()
        elif escolha == 4:
             break
menu()
