import sys
import time
from typing import List, Optional
from character import Monster
from monsters import Minotaur, GibberingMouther, Manes

class Battle:
    def __init__(self):
        self.monsters: List[Monster] = []
        self.turn_count = 1

    def setup(self):
        print("=== SISTEMA DE BATALHA RPG (Refatorado) ===")
        print("Escolha seus oponentes:")
        print("1. Minotauro")
        print("2. Abocanhador Matraqueante")
        print("3. Manes")
        
        while True:
            try:
                choice = int(input("Digite o ID do monstro: "))
                count = int(input("Quantos monstros? "))
                
                for i in range(count):
                    if choice == 1:
                        m = Minotaur()
                    elif choice == 2:
                        m = GibberingMouther()
                    elif choice == 3:
                        m = Manes()
                    else:
                        print("Opção inválida.")
                        continue
                    
                    m.name = f"{m.name} {i+1}"
                    self.monsters.append(m)
                break
            except ValueError:
                print("Por favor, digite números válidos.")

    def start(self):
        self.setup()
        print(f"\nCombate iniciado contra {len(self.monsters)} inimigos!")
        
        while True:
            print(f"\n--- TURNO {self.turn_count} ---")
            self.show_status()
            
            action = input("\nAção (A-Atacar / V-Vida / S-Sair): ").upper().strip()
            
            if action == 'S':
                print("Encerrando combate.")
                break
            elif action == 'V':
                self.manage_health()
            elif action == 'A':
                self.manage_attack()
            else:
                print("Ação desconhecida.")
            
            self.turn_count += 1

    def show_status(self):
        print("Status dos Monstros:")
        for i, m in enumerate(self.monsters):
            status = "VIVO" if m.is_alive() else "MORTO"
            print(f"{i+1}. {m} [{status}]")

    def manage_health(self):
        try:
            idx = int(input("Qual monstro (número)? ")) - 1
            if 0 <= idx < len(self.monsters):
                val = int(input("Valor de cura (positivo) ou dano (negativo): "))
                if val > 0:
                    self.monsters[idx].heal(val)
                    print(f"{self.monsters[idx].name} curado em {val}.")
                else:
                    self.monsters[idx].take_damage(abs(val))
                    print(f"{self.monsters[idx].name} sofreu {abs(val)} de dano.")
            else:
                print("Monstro inválido.")
        except ValueError:
            print("Entrada inválida.")

    def manage_attack(self):
        try:
            idx = int(input("Qual monstro vai atacar (número)? ")) - 1
            if 0 <= idx < len(self.monsters):
                monster = self.monsters[idx]
                if not monster.is_alive():
                    print(f"{monster.name} está morto e não pode atacar.")
                    return

                print(f"\nAtaques de {monster.name}:")
                attacks = monster.get_attacks()
                for i, atk in enumerate(attacks):
                    print(f"{i+1}. {atk}")
                
                atk_choice = int(input("Escolha o ataque: ")) - 1
                if 0 <= atk_choice < len(attacks):
                    result = monster.perform_attack(atk_choice)
                    print(f"\n>>> {monster.name} usa {result.name}!")
                    print(f"Rolagem de Ataque: {result.hit_roll}")
                    if result.is_critical:
                        print(f"DANO CRÍTICO: {result.damage}")
                    elif result.is_fail:
                        print("FALHA CRÍTICA!")
                    else:
                        print(f"Dano: {result.damage}")
                    print(f"Efeito: {result.description}")
                else:
                    print("Ataque inválido.")
            else:
                print("Monstro inválido.")
        except ValueError:
            print("Entrada inválida.")
