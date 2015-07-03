def fib(n):
    a, b = 0, 1
    count = 0
    while count < n:
        count += 1
        yield a
        a, b = b, a + b

x = [x**3 for x in fib(5)]
print(x)
