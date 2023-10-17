import sys
import time
sys.path.append('methods')
sys.path.append('utils')

from methods.bfs import solve_bfs
from methods.ids import solve_ids
from methods.ucs import solve_ucs
from methods.a_star import solve_a_star
from methods.gbfs import solve_gbfs
from methods.hc import solve_hill_climbing
from methods.commons import print_solution



class Solver:
    def __init__(self, method, input, should_print):
        self.method = method
        self.input = input
        self.should_print = should_print

    def run(self):
        # begin = time.time()
        solution = self.get_solution()
        # end = time.time()
        
        # print("Tempo decorrido: {:.4f}".format(end - begin).replace(".",","))
        if self.method == 'H':
            return

        if solution:
            print("Número de passos: ", len(solution))
            if self.should_print:
                print_solution(solution, self.input)

        else:
            print("Nenhuma solução encontrada.")

    def get_solution(self):
        if self.method == "B":
            return solve_bfs(self.input)
        if self.method == "I":
            return solve_ids(self.input)
        if self.method == "U":
            return solve_ucs(self.input)
        if self.method == "A":
            return solve_a_star(self.input)
        if self.method == "G":
            return solve_gbfs(self.input)
        if self.method == "H":
            return solve_hill_climbing(self.input, self.should_print)
