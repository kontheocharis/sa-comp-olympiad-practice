N, W = map(int, input().split())

trees = [ tuple(map(int, input().split())) for l in range(N) ]

corners = [
    (0,0), (0, W-1), (W-1, 0), (W-1, W-1)
]

def main():
    max_side_length = 0

    # odd length squares (so we do not consider edges)
    for x in range(1, W-1):
        for y in range(1, W-1):
            if (x, y) in trees:
                continue

            l = get_max_side_length_at(x, y)

            if l > max_side_length:
                max_side_length = l

    # even length squares
    for x in range(W-1):
        for y in range(W-1):
            pass

    return max_side_length
