import math

a, n, m = map(int, input().split())

def main(a, n, m):
    if m <= n:
        return n - m

    elif m % a == 0:
        return 1 + main(a, n, m / a)

    else:
        return 1 + main(a, n, m + 1)

print(int(main(a, n, m)))
