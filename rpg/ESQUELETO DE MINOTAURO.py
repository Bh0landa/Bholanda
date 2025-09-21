import random

def Machado_Grande():
    resultado = random.randint(1, 20)
    total = resultado + 6
    d1 = random.randint(1, 12)
    d2 = random.randint(1, 12)
    print(f"Você usou Machado Grande! HD:{total}")
    if total != (resultado == 1):
        print(f"Dano: {d1 + d2 + 4} (2d12+4)")
    if resultado == 1:
        print("Falha crítica!")
    elif resultado == 20:
        print("Crítico!")

def chifrada():
    resultado = random.randint(1, 20)
    total = resultado + 6
    d1 = random.randint(1, 8)
    d2 = random.randint(1, 8)
    print(f"Você usou Chifrada! HD:{total}")
    if total != (resultado == 1):
        print(f"Dano: {d1 + d2 + 4} (2d8+4)")
    if resultado == 1:
        print("Falha crítica!")
    elif resultado == 20:
        print("Crítico!")


def investida():
    d1 = random.randint(1, 8)
    d2 = random.randint(1, 8)
    print(f"Você usou Investida! HD:{d1 + d2} Resistência Força CD:14")

tamanho = int(input("Digite o número de monstros: "))
lista = [67] * tamanho
print(lista)

while True:
    acao = input("O que deseja fazer? (vida/ataque/parar): ").strip().lower()
    if acao == 'parar':
        break
    elif acao == 'vida':
        indice = int(input(f"Digite o número do monstro (1 a {tamanho}): "))
        valor = int(input("Digite o valor a somar ou subtrair: "))
        lista[indice - 1] += valor
        print("Lista atualizada:", lista)
    elif acao == 'ataque':
        print("Escolha o tipo de ataque:")
        print("1. Machado Grande")
        print("2. Chifrada")
        print("3. Investida")
        tipo = input("Digite o número do ataque: ").strip()
        if tipo == '1':
            Machado_Grande()
        elif tipo == '2':
            chifrada()
        elif tipo == '3':
            investida()
        else:
            print("Opção de ataque inválida.")
    else:
        print("Opção inválida. Escolha vida, ataque ou parar.")