# TP1 - Inteligência Artificial

## Execução

Para executar o projeto, basta executar o comando a seguir dentro da pasta `src`

```sh
python main.py
```

## Algoritmos implementados

Nos algoritmos, a representação dos estados, função sucessora e teste objetivo foram implementados da seguinte forma:

1. **Estado:** Representado como uma lista de 9 números, onde 0 representa o espaço em branco e os números de 1 a 8 representam as peças do quebra-cabeça
2. **Função Sucessora:** A partir da função `available_moves` é possível determinar quais movimentos são válidos a partir de um estado atual. A função `get_new_state` aplica um movimento a um estado, produzindo um novo.
3. **Teste de Objetivo :** Para verificar se o estado objetivo foi alcançado, é feita uma comparação do estado atual com `[1, 2, 3, 4, 5, 6, 7, 8, 0]` que representa o estado objetivo.

### BFS

A BFS é um algoritmo que explora todos os estados em um nível antes de passar para o próximo. No contexto do 8-puzzle, a busca começa com o estado inicial e explora todas as configurações possíveis que podem ser alcançadas a partir desse estado. O algoritmo continua até que a solução seja encontrada ou até que todos os estados tenham sido explorados sem sucesso.

 **Fila para Exploração:** Uma fila é usada para armazenar os estados a serem explorados. A busca começa a partir do estado inicial e é expandida para os estados vizinhos, colocados na fila para exploração.

### IDS

O algoritmo IDS é uma estratégia de busca que combina a ideia de busca em profundidade com um controle de profundidade iterativa. Ele realiza buscas em profundidade com um limite mínimo e aumenta progressivamente esse limite. Isso permite que o algoritmo explore estados de forma eficiente, evitando o consumo excessivo de recursos.

**Busca em Profundidade (DFS):** A função `depth_limited_search` realiza uma busca em profundidade até um determinado limite de profundidade. Ela explora estados em profundidade. É mantida uma pilha de estados a serem explorados.
**Iterative Deepening Search (IDS):** A função `iterative_deepening_search` implementa o algoritmo IDS. Ela começa com um limite de profundidade zero e aumenta progressivamente esse limite até encontrar a solução. O IDS combina a ideia de uma busca em profundidade com o controle de profundidade iterativa.

### UCS

O UCS busca explorar o espaço de estados com base no custo de alcançar cada estado. Ele começa pela configuração inicial e se move para estados com menores custos acumulados, expandindo os estados com menor custo primeiro.

**Busca de Custo Uniforme (UCS):** A função `uniform_cost_search` implementa o algoritmo UCS. Ela utiliza uma fila de prioridade para expandir estados com base no custo acumulado até o momento(profundidade da busca).

### A\*

O algoritmo A\* avalia os estados com base no custo real do caminho percorrido até o estado e na estimativa do custo restante para alcançar a solução. O algoritmo seleciona estados com menores valores da função de avaliação primeiro.


**Heurística 1(Distância de Manhattan)**: A distância de Manhattan é a soma das distâncias horizontais e verticais que cada peça precisa se mover para alcançar sua posição correta no estado objetivo.
**Heurística 2(Número de Peças Fora do Lugar)**: A heurística do número de peças fora do lugar conta quantas peças no quebra-cabeça atual não estão na posição correta em relação ao estado objetivo. Quanto menor o número de peças fora do lugar, mais perto o estado está da solução.

### GBFS

O algoritmo Greedy Best-First Search é uma busca gulosa que seleciona estados com base apenas na heurística.

**Heurística 1(Distância de Manhattan)**: A distância de Manhattan é a soma das distâncias horizontais e verticais que cada peça precisa se mover para alcançar sua posição correta no estado objetivo.
**Heurística 2(Número de Peças Fora do Lugar)**: A heurística do número de peças fora do lugar conta quantas peças no quebra-cabeça atual não estão na posição correta em relação ao estado objetivo. Quanto menor o número de peças fora do lugar, mais perto o estado está da solução.

### Hill Climbing

O algoritmo Hill Climbing é uma busca heurística que faz movimentos aleatórios para estados vizinhos. O algoritmo avalia a qualidade de um estado com base em uma heurística e aceita movimentos que resultam em um estado melhor (heurística menor).

**Heurística 1(Distância de Manhattan)**: A distância de Manhattan é a soma das distâncias horizontais e verticais que cada peça precisa se mover para alcançar sua posição correta no estado objetivo.
**Heurística 2(Número de Peças Fora do Lugar)**: A heurística do número de peças fora do lugar conta quantas peças no quebra-cabeça atual não estão na posição correta em relação ao estado objetivo. Quanto menor o número de peças fora do lugar, mais perto o estado está da solução.


## Heurísticas

As heurísticas utilizadas são admissíveis para o problema do 8-Puzzle. Elas nunca geram um valor maior do que o custo real para chegar à solução, garantindo que o algoritmo de busca informada nunca superestime o custo do caminho.


## Análise de desempenho

1. **Qualidade da Solução:**
BFS, UCS e A* encontraram soluções ótimas em todos os casos testados.

2. **Tempo de Execução:**
O GBFS foi o algoritmo mais rápido em termos de tempo de execução. Isso se deve ao fato de que o GBFS é uma busca gulosa que considera apenas a heurística, ignorando o custo passado. Ele faz escolhas rápidas, mas não garante a solução mais curta.
O A* com distância de Manhattan foi o segundo mais rápido em nossos testes. O A* é uma busca informada que combina a busca em largura com uma função heurística. Ele é eficaz na busca de soluções de alta qualidade, mas pode ser mais lento do que o GBFS.

3. **Custo Benefício:**
O A* com distância de Manhattan destacou-se em termos de custo benefício. Embora possa ser ligeiramente mais lento que o GBFS, ele equilibra o tempo de execução com a qualidade da solução.


## Referências

- Material da disciplina
- http://science.slc.edu/~jmarshall/courses/2005/fall/cs151/lectures/heuristic-search/
- https://en.wikipedia.org/wiki/A*_search_algorithm
- http://www.decom.ufop.br/menotti/paa111/files/PCC104-111-ars-11.1-NelsonFlorencioJunior.pdf
- https://www.geeksforgeeks.org/greedy-best-first-search-algorithm/
- https://en.wikipedia.org/wiki/Hill_climbing