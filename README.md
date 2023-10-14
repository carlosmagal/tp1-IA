# TP1 - Inteligência Artificial

## BFS

1. **Estado:** Representado como uma lista de 9 números, onde 0 representa o espaço em branco e os números de 1 a 8 representam as peças do quebra-cabeça
2. **Função Sucessora:** A partir da função `available_moves` é possível determinar quais movimentos são válidos a partir de um estado atual. A função `apply_move` aplica um movimento a um estado, produzindo um novo estado.
3. **Teste de Objetivo :** Para verificar se o estado objetivo foi alcançado, é feita uma comparação do estado atual com `[1, 2, 3, 4, 5, 6, 7, 8, 0]` que reprsenta o estado objetivo.
4. **Fila para Exploração:** Uma fila é usada para armazenar os estados a serem explorados. A busca começa a partir do estado inicial e é expandida para os estados vizinhos, colocados na fila para exploração.

