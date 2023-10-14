# vai retornar o valor que é necessário para que a posição atual o zero seja movida
# -3 = cima
#  3 = baixo
#  1 = direita
# -1 = esquerda
def available_moves(state):
    moves = []
    index_0 = state.index(0)

    if index_0 >= 3:
        moves.append(-3)
    if index_0 < 6:
        moves.append(3)
    if index_0 % 3 > 0:
        moves.append(-1)
    if index_0 % 3 < 2:
        moves.append(1)

    return moves

# faz a troca do 0 com algum número
# o novo índice do 0 vai ser a soma do move + o índice atual


def get_new_state(state, move):
    new_state = state.copy()
    index_0 = new_state.index(0)
    target_index = index_0 + move

    aux = new_state[target_index]
    new_state[target_index] = 0
    new_state[index_0] = aux

    return new_state

# estado objetivo
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def print_puzzle(data):
    print(f'{data[0]} {data[1]} {data[2]}')
    print(f'{data[3]} {data[4]} {data[5]}')
    print(f'{data[6]} {data[7]} {data[8]}')
    print()


def print_solution(solution_path, initial_state):
    current_state = initial_state
    print_puzzle(current_state)

    for move in solution_path:
        current_state = get_new_state(current_state, move)

        print_puzzle(current_state)
