import random

def ataque_garras():
    resultado = random.randint(1, 20)
    total = resultado + 4
    d1 = random.randint(1, 8)
    d2 = random.randint(1, 8)
    print(f"Você usou Garras! HD:{total}")
    if resultado not in (1, 20):
        print(f"Dano: {d1 + d2} (2d8)")
    elif resultado == 1:
        print("Falha crítica!")
    elif resultado == 20:
        print("Crítico!")
        print(f"Dano x2: {(d1 + d2) * 2} (2d8)")

tamanho = int(input("Digite o número de monstros: "))
lista = [25] * tamanho
print(lista)

while True:
    acao = input("O que deseja fazer? (V-vida/A-ataque/P-parar): ").strip().upper()
    if acao == 'P':
        break
    elif acao == 'V':
        if tamanho == 1:
            valor = int(input("Digite o valor a somar ou subtrair: "))
            lista[0] += valor
            print("Lista atualizada:", lista)
        else:
            indice = int(input(f"Digite o número do monstro (1 a {tamanho}): "))
            valor = int(input("Digite o valor a somar ou subtrair: "))
            lista[indice - 1] += valor
            print("Lista atualizada:", lista)
    elif acao == 'A':
        print("ataque:")
        ataque_garras()
    else:
        print("Opção inválida. Escolha vida, ataque ou parar.")