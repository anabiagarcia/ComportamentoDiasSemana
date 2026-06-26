from abc import ABC, abstractmethod
from enum import Enum

class Prioridade(Enum):
    BAIXA = "Baixa"
    MEDIA = "Média"
    ALTA = "Alta"

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

    @abstractmethod
    def execute(self, user: str, info: str) -> str:
        return f"{user}, Segunda-feira é dia de organizar sua rotina e a principal entrega da semana é \"{info}\"."

    @abstractmethod
    def get_priority(self) -> Prioridade:
        return Prioridade.MEDIA
    
class TercaStrategy(DiaStrategy):
    """Comportamento para Terça-feira"""

    @abstractmethod
    def execute(self, user: str, info: str) -> str:
        return f"{user}, Terça-feira é dia de dar um gás nas pendências. Principalmente na \"{info}\" que tem o prazo mais curto."

    @abstractmethod
    def get_priority(self) -> Prioridade:
        return Prioridade.ALTA
    
class QuartaStrategy(DiaStrategy):
    """Comportamento para Quarta-feira"""

    @abstractmethod
    def execute(self, user: str, info: str) -> str:
        return f"{user}, Quarta-Feira é dia de revisar o andamento das atividades. Lembre-se de preparar o material sobre \"{info}\" para Weekly."

    @abstractmethod
    def get_priority(self) -> Prioridade:
        return Prioridade.MEDIA
    
class QuintaStrategy(DiaStrategy):
    """Comportamento para Quinta-feira"""

    @abstractmethod
    def execute(self, user: str, info: str) -> str:
        return f"{user}, Quinta-Feira é dia de auxiliar alguém da equipe no projeto \"{info}\"."

    @abstractmethod
    def get_priority(self) -> Prioridade:
        return Prioridade.BAIXA
    
class SextaStrategy(DiaStrategy):
    """Comportamento para Sexta-feira"""

    @abstractmethod
    def execute(self, user: str, info: str) -> str:
        return f"{user}, Sexta-Feira é dia repassar o que foi concluído e metas cumpridas com o(a) \"{info}\"."

    @abstractmethod
    def get_priority(self) -> Prioridade:
        return Prioridade.BAIXA
    
class SabadoStrategy(DiaStrategy):
    """Comportamento para Sábado"""

    @abstractmethod
    def execute(self, user: str, info: str) -> str:
        return f"{user}, Sábado é dia livre, aproveite para descansar e ler o livro que estava querendo: \"{info}\"."

    @abstractmethod
    def get_priority(self) -> Prioridade:
        return Prioridade.BAIXA
    
class DomingoStrategy(DiaStrategy):
    """Comportamento para Domingo"""

    @abstractmethod
    def execute(self, user: str, info: str) -> str:
        return f"{user}, Domingo é dia de se preparar para a semana. Não esqueça que essa semana terá o evento da \"{info}\"."

    @abstractmethod
    def get_priority(self) -> Prioridade:
        return Prioridade.BAIXA