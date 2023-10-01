# n = int(input())
# fib = [0, 1]

# while fib[-1] < n:
#     next_value = fib[-1] + fib[-2]
#     fib.append(next_value)

# print(*fib[:n], sep=' ')

def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            next_fib = fib[i - 1] + fib[i - 2]
            fib.append(next_fib)
        return fib

n = int(input())

# Calculate the first N Fibonacci numbers
fib_sequence = fib(n)
print(*fib_sequence, sep=' ')
# print(" ".join(map(str, fib_sequence)))

