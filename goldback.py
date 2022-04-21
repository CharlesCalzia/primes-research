
# solve goldbach conjecture
def solve_goldbach(n):
    for i in range(2, n):
        if is_prime(i):
            for j in range(2, n):
                if is_prime(j) and i + j == n:
                    return True
    return False

