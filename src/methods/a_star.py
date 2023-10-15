import heapq
from commons import get_new_state, available_moves, GOAL_STATE, heuristics


def a_star_search(initial_state):
    if initial_state == GOAL_STATE:
        return [0]

    visited = set()
    priority_queue = [(0 + heuristics(initial_state), 0, initial_state, [])]

    while priority_queue:
        _, cost, current_state, path = heapq.heappop(priority_queue)

        if current_state == GOAL_STATE:
            return path

        if tuple(current_state) not in visited:
            visited.add(tuple(current_state))
            moves = available_moves(current_state)
            for move in moves:
                new_state = get_new_state(current_state, move)
                heuristic = heuristics(new_state)

                new_path = path + [move]
                new_cost = cost + 1
                heapq.heappush(priority_queue, (new_cost +
                               heuristic, new_cost, new_state, new_path))


def solve_a_star(input):
    solution = a_star_search(input)
    return solution
