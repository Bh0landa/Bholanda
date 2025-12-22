import random

class Dice:
    """Utilitário para rolagem de dados de RPG."""
    
    @staticmethod
    def roll(sides: int, count: int = 1) -> int:
        """Rola 'count' dados de 'sides' lados e retorna a soma."""
        total = 0
        for _ in range(count):
            total += random.randint(1, sides)
        return total

    @staticmethod
    def d4(count: int = 1) -> int: return Dice.roll(4, count)
    
    @staticmethod
    def d6(count: int = 1) -> int: return Dice.roll(6, count)
    
    @staticmethod
    def d8(count: int = 1) -> int: return Dice.roll(8, count)
    
    @staticmethod
    def d10(count: int = 1) -> int: return Dice.roll(10, count)
    
    @staticmethod
    def d12(count: int = 1) -> int: return Dice.roll(12, count)
    
    @staticmethod
    def d20(count: int = 1) -> int: return Dice.roll(20, count)
