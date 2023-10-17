from commons import get_new_state, available_moves, GOAL_STATE, heuristics, print_state
import sys
import random

sys.path.append('methods')
sys.path.append('utils')


def hill_climbing(initial_state, max_iterations=10000):
    if initial_state == GOAL_STATE:
        return initial_state, 1, [initial_state.copy()]

    current_state = initial_state
    current_heuristic = heuristics(current_state)
    explored_states = [current_state.copy()]
    steps = 0
    
    for _ in range(max_iterations):
        moves = available_moves(current_state)
        random.shuffle(moves)
        
        # vizinhos
        new_states = []
        for move in moves:
            new_state = get_new_state(current_state, move)
            new_states.append(new_state)

        def gg(n):
          return heuristics(n)
        
        # ordenando pela heuristica
        y = sorted(new_states, key=gg,reverse=True)
        
        for u in y:
          n_HHH = heuristics(u)
          
          if n_HHH < current_heuristic:
                
              current_state = u
              current_heuristic = n_HHH
              explored_states.append(current_state.copy())
              steps += 1
              
              if current_heuristic == 0:
                  return current_state, steps, explored_states
    
    #TENTATIVA DE REINICIO ALEATORIO
    # moves = available_moves(current_state)
    # random.shuffle(moves)
    # new_state = get_new_state(current_state, moves[0])
    
    # hill_climbing(new_state)
    return current_state, steps, explored_states

  
def solve_hill_climbing(input, should_print):
    final_state,steps, path = hill_climbing(input)
    
    if not final_state == GOAL_STATE:
        print("Solução não encontrada")

    print("Número de passos: ", steps)
    if should_print:
        for state in path:
            print_state(state)

    return None
