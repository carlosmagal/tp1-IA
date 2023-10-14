from methods.bfs import solve_bfs


class Solver:
    def __init__(self, method, input, should_print):
        self.method = method
        self.input = input
        self.should_print = should_print

    def run(self):
        match self.method:
            case "B":
                solve_bfs(self.input, self.should_print)
            case "I":
                print('1')
            case "U":
                print()
            case "A":
                print()
            case "G":
                print()
            case "H":
                print()
