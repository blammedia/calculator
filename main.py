from add import add
from input import input_infinite_integer


def main():
    input_list = input_infinite_integer()
    sum = add(input_list)
    print(sum)


if __name__ == '__main__':
    main()