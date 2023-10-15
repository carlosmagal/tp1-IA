import heapq
from commons import get_new_state, available_moves, GOAL_STATE, heuristics


def gbfs(initial_state):
    if initial_state == GOAL_STATE:
        return [0]

    visited = set()
    priority_list = [(heuristics(initial_state), initial_state, [])]

    while priority_list:
        _, current_state, path = heapq.heappop(priority_list)

        if current_state == GOAL_STATE:
            return path

        if tuple(current_state) not in visited:
            visited.add(tuple(current_state))
            moves = available_moves(current_state)
            for move in moves:
                new_state = get_new_state(current_state, move)
                new_path = path + [move]
                heapq.heappush(priority_list, (heuristics(
                    new_state), new_state, new_path))


def solve_gbfs(input):
    solution = gbfs(input)
    return solution
