import time


def tictoc(func):
    def wrapper(n):
        t1 = time.time()
        func(n)
        t2 = time.time()
        runtime = t2 - t1
        print(f"Function {func.__name__} took {runtime} second to execute")

    return wrapper


@tictoc
def fib1(n):
    a, b = 0, 1
    fib_list = [a]
    for i in range(1,n):
        a, b = b, a + b
        fib_list.append(a)

    # print(fib_list)


@tictoc
def fib2(n):
    a, b = 0, 1
    fib_list = [a]
    while len(fib_list) != n:
        a, b = b, a + b
        fib_list.append(a)

    # print(fib_list)

for i in range(10):
    fib1(10000)
    fib2(10000)
    print('-'*50)
