def read_input(input_str):
    clean_input = input_str.replace("TP1 ", "")
    words = clean_input.split()

    algorithm = words[0].strip().upper()
    user_input = [int(word) for word in words[1:10]]
    print_flag = "PRINT" in words

    return algorithm, user_input, print_flag