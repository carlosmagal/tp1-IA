from collections import deque
from commons import get_new_state, available_moves, GOAL_STATE
import sys
sys.path.append('../')


def bfs(initial_state):
    if initial_state == GOAL_STATE:
        return [0]

    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state == GOAL_STATE:
            return path

        visited.add(tuple(current_state))
        moves = available_moves(current_state)

        for move in moves:
            new_state = get_new_state(current_state, move)
            if tuple(new_state) not in visited:
                new_path = path + [move]
                queue.append((new_state, new_path))

    return False


def solve_bfs(input):
    solution = bfs(input)
    return solution
