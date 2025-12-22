from abc import ABC, abstractmethod
from typing import List, Tuple
from dice import Dice

class Character(ABC):
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount: int):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp})"

class AttackResult:
    def __init__(self, name: str, hit_roll: int, damage: int, is_critical: bool = False, is_fail: bool = False, description: str = ""):
        self.name = name
        self.hit_roll = hit_roll
        self.damage = damage
        self.is_critical = is_critical
        self.is_fail = is_fail
        self.description = description

class Monster(Character):
    def __init__(self, name: str, hp: int):
        super().__init__(name, hp)

    @abstractmethod
    def get_attacks(self) -> List[str]:
        """Retorna lista de nomes de ataques disponíveis."""
        pass

    @abstractmethod
    def perform_attack(self, attack_index: int) -> AttackResult:
        """Executa um ataque baseado no índice."""
        pass
