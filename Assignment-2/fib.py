def print_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
n = int(input("Input: "))
print("Output:", end=' ')
print_fibonacci(n)
