from abc import ABC, abstractmethod
from enum import Enum

class Prioridade(Enum):
    BAIXA = "Baixa"
    MEDIA = "Média"
    ALTA = "Alta"
    INDEFINIDA = "Indefinida"

class DiaStrategy(ABC):
    """Abstração para cada dia da semana"""

    @abstractmethod
    def execute(self, user: str, info: str) -> str:
        """Retorna o comportamento do dia da semana"""
        pass

    @abstractmethod
    def get_priority(self) -> Prioridade:
        """Retorna a prioridade do dia: ALTA, MÉDIA ou BAIXA"""
        pass

class SegundaStrategy(DiaStrategy):
    """Comportamento para Segunda-feira"""

    def execute(self, user: str, info: str) -> str:
        return f"{user}, Segunda-feira é dia de organizar sua rotina e a principal entrega da semana é \"{info}\"."

    def get_priority(self) -> Prioridade:
        return Prioridade.MEDIA
    
class TercaStrategy(DiaStrategy):
    """Comportamento para Terça-feira"""

    def execute(self, user: str, info: str) -> str:
        return f"{user}, Terça-feira é dia de dar um gás nas pendências. Principalmente na \"{info}\" que tem o prazo mais curto."

    def get_priority(self) -> Prioridade:
        return Prioridade.ALTA
    
class QuartaStrategy(DiaStrategy):
    """Comportamento para Quarta-feira"""

    def execute(self, user: str, info: str) -> str:
        return f"{user}, Quarta-Feira é dia de revisar o andamento das atividades. Lembre-se de preparar o material sobre \"{info}\" para Weekly."

    def get_priority(self) -> Prioridade:
        return Prioridade.MEDIA
    
class QuintaStrategy(DiaStrategy):
    """Comportamento para Quinta-feira"""

    def execute(self, user: str, info: str) -> str:
        return f"{user}, Quinta-Feira é dia de auxiliar alguém da equipe no projeto \"{info}\"."

    def get_priority(self) -> Prioridade:
        return Prioridade.BAIXA
    
class SextaStrategy(DiaStrategy):
    """Comportamento para Sexta-feira"""

    def execute(self, user: str, info: str) -> str:
        return f"{user}, Sexta-Feira é dia repassar o que foi concluído e metas cumpridas com o(a) \"{info}\"."

    def get_priority(self) -> Prioridade:
        return Prioridade.BAIXA
    
class SabadoStrategy(DiaStrategy):
    """Comportamento para Sábado"""

    def execute(self, user: str, info: str) -> str:
        return f"{user}, Sábado é dia livre, aproveite para descansar e ler o livro que estava querendo: \"{info}\"."

    def get_priority(self) -> Prioridade:
        return Prioridade.BAIXA
    
class DomingoStrategy(DiaStrategy):
    """Comportamento para Domingo"""

    def execute(self, user: str, info: str) -> str:
        return f"{user}, Domingo é dia de se preparar para a semana. Não esqueça que essa semana terá o evento da \"{info}\"."

    def get_priority(self) -> Prioridade:
        return Prioridade.BAIXA

class InvalidoStrategy(DiaStrategy):
    """Dia inválido ou sem estratégia"""

    def execute(self, user: str, info: str) -> str:
        return f"Dia inválido ou sem estratégia. Nenhuma ação executada, {user}."

    def get_priority(self) -> Prioridade:
        return Prioridade.INDEFINIDA

class StrategySelector:
    def __init__(self):
        self.strategies = {
            "segunda-feira": SegundaStrategy(),
            "terca-feira": TercaStrategy(),
            "quarta-feira": QuartaStrategy(),
            "quinta-feira": QuintaStrategy(),
            "sexta-feira": SextaStrategy(),
            "sabado": SabadoStrategy(),
            "domingo": DomingoStrategy()
        }

    def get_strategy(self, dia: str) -> DiaStrategy:
        return self.strategies.get(dia.lower(), InvalidoStrategy())
