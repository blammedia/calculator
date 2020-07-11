from add import add
from input import input_integer


def main():
    a, b = input_integer()
    c = add(a, b)
    print(c)


if __name__ == '__main__':
    main()