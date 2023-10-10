def read_input(input_str):
    clean_input = input_str.replace("TP1 ", "")
    words = clean_input.split()

    algorithm = words[0].strip().upper()
    user_input = [int(word) for word in words[1:10]]
    print_flag = "PRINT" in words

    return algorithm, user_input, print_flag


def define_method(algorithm, user_input):
    match algorithm:
        case "B":
            print()
        case "I":
            print()
        case "U":
            print()
        case "A":
            print()
        case "G":
            print()
        case "H":
            print()


def main():

    str = input()
    algorithm, user_input, print_flag = read_input(str)

    define_method(algorithm, user_input)

    print("algorithm:", algorithm)
    print("user_input:", user_input)
    print("Print:", print_flag)


if __name__ == "__main__":
    main()
