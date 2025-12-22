from typing import List
from character import Monster, AttackResult
from dice import Dice

class Minotaur(Monster):
    def __init__(self):
        super().__init__("Minotauro", 76) # Ajustei para 76 (média D&D) ou mantenho 67 do user? Vou usar 67 para ser fiel.
        self.max_hp = 67
        self.hp = 67

    def get_attacks(self) -> List[str]:
        return ["Machado Grande", "Chifrada", "Investida"]

    def perform_attack(self, attack_index: int) -> AttackResult:
        d20 = Dice.d20()
        hit_bonus = 6
        total_hit = d20 + hit_bonus
        
        if attack_index == 0: # Machado Grande
            damage = Dice.d12(2) + 4
            desc = "Golpe poderoso com o machado!"
        elif attack_index == 1: # Chifrada
            damage = Dice.d8(2) + 4
            desc = "Ataque perfurante com os chifres."
        elif attack_index == 2: # Investida
            damage = Dice.d8(2)
            desc = "Investida violenta! (CD 14 Força para não cair)"
            return AttackResult("Investida", 0, damage, False, False, desc)
        else:
            return AttackResult("Erro", 0, 0, False, True, "Ataque inválido")

        if d20 == 1:
            return AttackResult(self.get_attacks()[attack_index], d20, 0, False, True, "Falha Crítica!")
        elif d20 == 20:
            return AttackResult(self.get_attacks()[attack_index], total_hit, damage * 2, True, False, f"CRÍTICO! {desc}")
        else:
            return AttackResult(self.get_attacks()[attack_index], total_hit, damage, False, False, desc)

class GibberingMouther(Monster):
    def __init__(self):
        super().__init__("Abocanhador Matraqueante", 67)

    def get_attacks(self) -> List[str]:
        return ["Mordida", "Cusparada Cegante", "Ataque Múltiplo"]

    def perform_attack(self, attack_index: int) -> AttackResult:
        if attack_index == 0: # Mordida
            return self._bite()
        elif attack_index == 1: # Cusparada
            return AttackResult("Cusparada", 0, 0, False, False, "Cusparada química! CD 13 Sabedoria ou fica cego.")
        elif attack_index == 2: # Multi
            # Simplificação: Retorna o resultado da mordida e avisa da cusparada
            bite = self._bite()
            bite.description += " E também usou Cusparada!"
            return bite
        return AttackResult("Erro", 0, 0)

    def _bite(self) -> AttackResult:
        d20 = Dice.d20()
        hit_bonus = 2
        damage = Dice.d6(5)
        
        if d20 == 1:
            return AttackResult("Mordida", d20, 0, False, True, "Errou feio a mordida!")
        elif d20 == 20:
            return AttackResult("Mordida", d20 + hit_bonus, damage * 2, True, False, "CRÍTICO! Muitas bocas mordendo!")
        
        return AttackResult("Mordida", d20 + hit_bonus, damage, False, False, "Muitas bocas mordem o alvo.")

class Manes(Monster):
    def __init__(self):
        super().__init__("Manes", 25) # User script said 25

    def get_attacks(self) -> List[str]:
        return ["Garras"]

    def perform_attack(self, attack_index: int) -> AttackResult:
        d20 = Dice.d20()
        hit_bonus = 4
        damage = Dice.d8(2)
        
        if d20 == 1:
            return AttackResult("Garras", d20, 0, False, True, "Tropeçou nas próprias garras.")
        elif d20 == 20:
            return AttackResult("Garras", d20 + hit_bonus, damage * 2, True, False, "CRÍTICO! Rasgou fundo.")
            
        return AttackResult("Garras", d20 + hit_bonus, damage, False, False, "Arranhão simples.")
