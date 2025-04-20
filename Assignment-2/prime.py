def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_till_n(n):
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=' ')

n = int(input("Input: "))
print("Output:", end=' ')
print_primes_till_n(n)
