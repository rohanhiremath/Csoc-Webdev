def print_center_aligned_triangle(n):
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        print(' ' * spaces + '*' * stars)
        
n = int(input("Input: "))
print("Output:")
print_center_aligned_triangle(n)
