from solver import Solver
from utils.utils import read_input


def main():

    str = input()
    algorithm, user_input, print_flag = read_input(str)

    solver = Solver(algorithm, user_input, print_flag)
    solver.run()


if __name__ == "__main__":
    main()
