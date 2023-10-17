import sys
sys.path.append('methods')
sys.path.append('utils')

from utils.utils import read_input
from solver import Solver

def main():
    str = input()
    method, initial_state, should_print = read_input(str)

    solver = Solver(method, initial_state, should_print)
    solver.run()


if __name__ == "__main__":
    main()
