def add(a, b):
    return a + b


if __name__ == '__main__':
    print("[INFO] Start test for add")
    assert(add(3, 5) == 8)
    assert(add(1, -1) == 0)
    assert(add(10000, 2000) == 12000)
    print("[INFO] Test success")