from methods.bfs import solve_bfs
from methods.ids import solve_ids
from methods.ucs import solve_ucs

from methods.commons import print_solution


class Solver:
    def __init__(self, method, input, should_print):
        self.method = method
        self.input = input
        self.should_print = should_print

    def run(self):
        solution = self.get_solution()

        if solution:
            print("Número de passos: ", len(solution))
            if self.should_print:
                print_solution(solution, self.input)

        else:
            print("Nenhuma solução encontrada.")

    def get_solution(self):
        match self.method:
            case "B":
                return solve_bfs(self.input)
            case "I":
                return solve_ids(self.input)
            case "U":
                return solve_ucs(self.input)
            case "A":
                print()
            case "G":
                print()
            case "H":
                print()
