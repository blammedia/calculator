def input_integer():
    input_string = input()
    input_list = input_string.split(' ')
    a, b = map(int, input_list)
    return a, b