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