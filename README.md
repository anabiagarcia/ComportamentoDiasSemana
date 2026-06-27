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

2. O padrão é o Null Object. Ele é um caso especial do próprio Strategy, ao invés de devolver null quando o dia não tem comportamento, criamos uma estratégia "vazia" (InvalidoStrategy) que segue a mesma interface DiaStrategy e responde de um jeito neutro. Pra quem chama, ela é só mais uma strategy.

3. A InvalidoStrategy é o null object. Ela herda de DiaStrategy, então tem o execute e o get_priority igual qualquer dia normal, e por isso pode ser usada no lugar de qualquer um deles. A diferença é o conteúdo: o execute só avisa que o dia é inválido e que nada foi executado, e o get_priority devolve indefinida. A ligação acontece no get_strategy do selector, que usa ela como valor padrão quando o dia não está no dicionário. No fim o programa não trava com um dia inválido e o main não precisa de nenhum if extra pra esses casos.
