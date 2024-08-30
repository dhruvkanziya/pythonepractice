def print_diamond(n):
    # Upper half of the diamond
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i * 2 + 1):
            print("*", end="")
        print()

    # Lower half of the diamond
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i * 2 + 1):
            print("*", end="")
        print()

# Example usage
n = 5  # Number of rows (should be an odd number for a symmetric diamond)
print_diamond(n)