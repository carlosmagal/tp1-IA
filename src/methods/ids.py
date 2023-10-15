from commons import get_new_state, available_moves, GOAL_STATE


def depth_limited_search(initial_state, depth_limit):
    if initial_state == GOAL_STATE:
        return [0]

    visited = set()
    stack = [(initial_state, [], 0)]

    while stack:
        current_state, path, depth = stack.pop()
        if current_state == GOAL_STATE:
            return path

        if depth < depth_limit:
            visited.add(tuple(current_state))
            moves = available_moves(current_state)

            for move in moves:
                new_state = get_new_state(current_state, move)
                if tuple(new_state) not in visited:
                    new_path = path + [move]
                    stack.append((new_state, new_path, depth + 1))
    return None


def ids(initial_state):
    limit = 0

    while True:
        result = depth_limited_search(initial_state, limit)
        if result is not None:
            return result
        limit += 1


def solve_ids(input):
    solution = ids(input)
    return solution
