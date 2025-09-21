import random

def ataque_mordida():
    resultado = random.randint(1, 20)
    total = resultado + 2
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    d4 = random.randint(1, 6)
    d5 = random.randint(1, 6)
    print(f"Você usou Mordida! HD:{total}")
    if total != (resultado == 1):
        print(f"Dano: {d1 + d2 + d3 + d4 + d5} (5d6)")
    elif resultado == 1:
        print("Falha crítica!")
    elif resultado == 20:
        print("Crítico!")

def ataque_cusparada():
    print("Você usou Cusparada! Resistência Sabedoria CD:13")

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
        print("1. Mordida")
        print("2. Cusparada")
        print("3. Mordida e Cusparada")
        tipo = input("Digite o número do ataque: ").strip()
        if tipo == '1':
            ataque_mordida()
        elif tipo == '2':
            ataque_cusparada()
        elif tipo == '3':
            ataque_mordida()
            ataque_cusparada()
        else:
            print("Opção de ataque inválida.")
    else:
        print("Opção inválida. Escolha vida, ataque ou parar.")