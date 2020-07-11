def input_infinite_integer():
    input_string = input()
    input_list = input_string.split(' ')
    output_list = []
    for i in input_list:
        output_list.append(int(i))
    return output_list


if __name__ == '__main__':
    a = input_infinite_integer()
    print(a)