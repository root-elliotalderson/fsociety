import sys
import os
from datetime import datetime

# ========================
# UTILIDADES
# ========================


def limpar_tela():
    os.system('clear')


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("❌ Digite um número válido.")


def pausar():
    input("\nPressione ENTER para continuar...")


# ========================
# SISTEMA PRINCIPAL
# ========================

historico = []


def registrar(acao):
    horario = datetime.now().strftime("%H:%M:%S")
    historico.append(f"[{horario}] {acao}")


# ========================
# FUNÇÕES DAS OPÇÕES
# ========================

def somar():
    limpar_tela()
    print("=== SOMA ===")

    a = ler_int("Primeiro número: ")
    b = ler_int("Segundo número: ")

    resultado = a + b
    print(f"\nResultado: {resultado}")

    registrar(f"Soma: {a} + {b} = {resultado}")
    pausar()


def mensagem():
    limpar_tela()
    print("=== MENSAGEM ===")

    nome = input("Digite seu nome: ").strip() or "Visitante"
    msg = f"Olá, {nome}! Tudo certo por aí?"

    print("\n" + msg)

    registrar(f"Mensagem exibida para {nome}")
    pausar()


def ver_historico():
    limpar_tela()
    print("=== HISTÓRICO ===")

    if not historico:
        print("Nenhuma ação registrada.")
    else:
        for item in historico:
            print(item)

    pausar()


def submenu_operacoes():
    while True:
        limpar_tela()
        print("=== OPERAÇÕES ===")
        print("1 - Somar")
        print("2 - Voltar")

        escolha = input("Escolha: ")

        if escolha == "1":
            somar()
        elif escolha == "2":
            break
        else:
            print("❌ Opção inválida")
            pausar()


def sair():
    print("\nEncerrando sistema...")
    sys.exit()


# ========================
# MENU PRINCIPAL
# ========================

def menu_principal():
    opcoes = {
        "1": submenu_operacoes,
        "2": mensagem,
        "3": ver_historico,
        "4": sair
    }

    while True:
        limpar_tela()
        print("===== SISTEMA =====")
        print("1 - Operações")
        print("2 - Mensagem")
        print("3 - Histórico")
        print("4 - Sair")

        escolha = input("Escolha: ")

        acao = opcoes.get(escolha)

        if acao:
            acao()
        else:
            print("❌ Opção inválida")
            pausar()


# ========================
# EXECUÇÃO
# ========================

if __name__ == "__main__":
    menu_principal()