for _ in range(int(input())):
    x, y = input().split()
    try:
        print(int(x) // int(y))
    except BaseException as error:
        print(f'Error Code: {error}')