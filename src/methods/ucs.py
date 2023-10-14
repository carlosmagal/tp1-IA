import heapq
from commons import get_new_state, available_moves, GOAL_STATE


def uniform_cost_search(initial_state):
    if initial_state == GOAL_STATE:
        return [0]

    visited = set()
    priority_queue = [(0, initial_state, [])]

    while priority_queue:
        cost, current_state, path = heapq.heappop(priority_queue)

        if current_state == GOAL_STATE:
            return path

        if tuple(current_state) not in visited:
            visited.add(tuple(current_state))
            moves = available_moves(current_state)
            for move in moves:
                new_state = get_new_state(current_state, move)
                new_path = path + [move]
                new_cost = cost + 1
                heapq.heappush(priority_queue, (new_cost, new_state, new_path))


def solve_ucs(input):
    solution = uniform_cost_search(input)
    return solution
