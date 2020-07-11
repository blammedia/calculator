def add(input_list):
    sum = 0
    for i in input_list:
        sum += i
    return sum


if __name__ == '__main__':
    print("[INFO] Start test for add")
    assert(add([3, 5]) == 8)
    assert(add([1, -1]) == 0)
    assert(add([10000, 2000]) == 12000)
    assert(add([1, 2, 3]) == 6)
    print("[INFO] Test success")