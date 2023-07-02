cube = lambda x: x**3

def fibonacci(n):
    fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
    fibonacci_list = []
    for i in range(n):
        fibonacci_list.append(fib(i))
    return fibonacci_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))