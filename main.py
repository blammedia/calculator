from add import add


def input_two_integer():
    input_string = input()
    input_list = input_string.split(' ')
    a, b = map(int, input_list)
    return a, b


if __name__ == '__main__':
    a, b = input_two_integer()
    c = add(a, b)
    print(c)