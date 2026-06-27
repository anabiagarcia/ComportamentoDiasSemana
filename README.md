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

1. Em vez de o StrategySelector retornar None quando o dia não existe (forçando o main a fazer if estrategia is not None antes de cada chamada), ele sempre retorna um objeto de strategy válido. Quando não tem dia correspondente, retorna uma strategy InvalidoStrategy que implementa a mesma interface. Assim o main chama estrategia.execute(...) e estrategia.get_priority() direto, sem checar nulo.
