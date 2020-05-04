a = int(input('請輸入'))

def fibonacci(n, fib = [0, 1]):
    if n >= len(fib):
        for i in range(len(fib), n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

fibonacci2 = []


for i in range(0, 100):
    if fibonacci(i)%2==1:
        fibonacci2(i=fibonacci(i)
        print(fibonacci2(i), end=' ')
 
