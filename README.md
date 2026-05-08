# Pokémon TCG Monte Carlo Simulator

Simulador estadístico para analizar consistencia, recuperación y presión en mazos de Pokémon TCG utilizando simulaciones tipo Monte Carlo.

El objetivo principal del proyecto es comparar listas competitivas y medir objetivamente:

- Setup inicial
- Setup óptimo
- Brick rate
- Recovery rate
- Presión temprana
- Impacto de techs
- Análisis por turno inicial (primero/segundo)
- Performance contra arquetipos específicos (futuro)

---

# Objetivo del Proyecto

Este proyecto busca crear un entorno flexible para:

- Comparar listas competitivas
- Evaluar cambios de pocas cartas
- Simular matchups
- Medir consistencia
- Analizar impacto del turno inicial
- Experimentar con IA heurística (futuro)
- Escalar a simulaciones más avanzadas (futuro)

Actualmente, el enfoque está en:

- N's Zoroark ex, con 2 versiones principales en mente:
    - Mega Lopunny ex
    - Cornerstone Mask Ogerpon ex

- Matchups contra Team Rocket, Mega Venusaur y Mega Lucario (futuro)

---

# Estructura del Proyecto

```txt
pokemon_tcg_sim/
│
├── main.py
├── listas.py
├── sim.py
├── utilidades.py
│
├── matchups/ (Futuro)
│   ├── rocket.py
│   ├── venusaur.py
│   └── lucario.py
│
├── ai/ (Futuro)
│   └── heuristics.py
│
├── metrics/ (Futuro)
│   └── metrics.py
│
└── README.md
```

---

# Arquitectura del Sistema

```mermaid
flowchart TD

    A[Listas de Mazos] --> B[Simulador]
    B --> C[Motor de Juego]
    C --> D[Evaluación de Mano]
    C --> E[Disrupción]
    C --> F[Simulación de Turnos]

    D --> G[Métricas]
    E --> G
    F --> G

    G --> H[Resultados]
```

---

# Flujo de una Simulación

```mermaid
sequenceDiagram

    participant Deck
    participant Sim
    participant Matchup
    participant Metrics

    Deck->>Sim: Construir mazo
    Sim->>Sim: Shuffle
    Sim->>Sim: Robo inicial
    Sim->>Sim: Mulligan

    Sim->>Matchup: Aplicar presión/disrupción
    Matchup->>Sim: Estado modificado

    Sim->>Metrics: Evaluar setup
    Sim->>Metrics: Evaluar recovery
    Sim->>Metrics: Evaluar pressure

    Metrics->>Sim: Resultados
```

---

# Métricas Implementadas

## Setup Rate

Probabilidad de abrir una mano funcional.

Ejemplo:
- Básico + buscador
- Básico + soporte de robo

---

## Setup Rate Óptimo

Probabilidad de abrir una mano óptima y favorable.

Ejemplo:
- Básico óptimo + buscador + energía
- Básico + buscador + energía + soporte de robo

---

## Recovery Rate

Probabilidad de recuperarse luego de una disrupción.

Ejemplos:
- Judge
- Unfair Stamp
- Hand reset

---

## Pressure Rate

Probabilidad de:
- setear
- y además devolver presión

Ejemplos:
- Judge temprano
- Unfair Stamp
- ataque temprano
- estadios (futuro)

---

## Métricas por Turno Inicial

El simulador ahora calcula métricas separadas para escenarios donde el jugador va primero o segundo, permitiendo análisis más detallado de la consistencia.

### Setup Rate si va primero
Probabilidad de setup asumiendo que el jugador va primero.

### Setup Rate si va segundo
Probabilidad de setup asumiendo que el jugador va segundo.

### Análisis Comparativo
Diferencias entre métricas de "va primero" vs "va segundo" para identificar ventajas/desventajas por turno inicial.

# Lógica Actual de Evaluación

```mermaid
graph LR

    A[Mano Inicial] --> B{¿Tiene Básico?}

    B -- No --> C[Mulligan]
    B -- Sí --> D[Evaluar Setup]

    D --> E{¿Tiene Search o Draw?}

    E -- Sí --> F[Setup Exitoso]
    E -- No --> G[Brick]
```

---

# Categorías de Cartas

Actualmente, el simulador clasifica cartas en:

- Pokémon básicos
- Evoluciones
- Search
- Draw
- Recovery
- Utility
- Disruption
- Stadiums
- Energy

---

# Posibles Mejoras Futuras

## Motor de Juego Completo

- Bench real
- Prize cards
- Sistema de daño
- Evoluciones reales
- Estados especiales

---

## IA Heurística

Sistema de decisiones automáticas:

```python
if "Lillie" in hand:
    play("Lillie")
```

---

## Monte Carlo Tree Search (MCTS)

Permitir que la IA:
- explore jugadas
- compare líneas
- optimice decisiones

---

## Reinforcement Learning

Posible integración con:

- Gymnasium
- Stable-Baselines3
- PyTorch

---

# Ideas de Matchups

## Team Rocket

- Disrupción
- Debilidad Planta
- Setup rápido

## Mega Venusaur

- Alto HP
- Debilidad Planta
- Matchup de daño

## Mega Lucario

- Presión agresiva
- Tempo rápido

---

# Documentación Recomendada

## Docstrings

Ejemplo:

```python
def evaluate_setup(hand):
    """
    Evalúa si una mano inicial es funcional.

    Parameters
    ----------
    hand : list
        Lista de cartas en mano.

    Returns
    -------
    tuple
        (setup, pressure)
    """
```

---

# Tipado Recomendado

```python
def draw(deck: list[str], n: int) -> list[str]:
```

---

# Logging Recomendado

Agregar logs para debug:

```python
print(f"Hand: {hand}")
print(f"Recovery: {recovery}")
```

o usar:

```python
import logging
```

---

# Testing Recomendado

Usar:

```txt
tests/
```

Ejemplo:

```python
def test_has_basic():
    hand = ["Zorua", "Energy"]

    assert has_basic(hand) is True
```

---

# Roadmap

```mermaid
journey
    title Desarrollo del Simulador

    section Base
      Decklists: 5: Usuario
      Simulación simple: 5: Usuario
      Métricas: 4: Usuario

    section Intermedio
      Matchups reales: 3: Usuario
      Sistema de daño: 2: Usuario
      Simulación de tempo: 2: Usuario

    section Avanzado
      IA heurística: 1: Usuario
      MCTS: 1: Usuario
      RL completo: 1: Usuario
```

---

# Ideas de Investigación

- ¿Qué tech mejora más el recovery rate?
- ¿Cuántos buscadores necesita Zoroark?
- ¿Cuál es el costo real de jugar más energías?
- ¿Qué porcentaje de manos son "jugables"?
- ¿Cómo afecta Judge a cada arquetipo?