# Comportamento por Dia da Semana

## Estrutura do projeto
```
.
├── diasSemana.py    # Definições do comportamento por dia da semana utilizando Strategy
├── main.py         
└── README.md
```

## Estrutura dos comportamentos

O projeto utiliza o padrão de projeto **Strategy Pattern**:

- `DiaStrategy` (em `diasSemana.py`) é a abstração que define como será a estrutura do comportamento de cada dia da semana através do `execute(user, info)` e retorna a prioridade através do `get_priority()`.
- Cada dia da semana possui uma estratégia própria (`SegundaStrategy`, `TercaStrategy` etc.) que implementa esse comportamento com sua mensagem e prioridade.

## Questões de reflexão