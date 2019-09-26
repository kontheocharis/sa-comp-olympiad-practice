import copy
import math

N, M, Q = map(int, input().split())

grid = [ list(map(int, input().split())) for _ in range(N) ]

queries = [ list(map(int, input().split())) for _ in range(Q) ]

def calculate_no_of_steps(orig_grid, tower_coords):
    a, b, K = tower_coords
    steps = 0
    curr_grid = copy.deepcopy(orig_grid)

    for stone in range(K):
        # first we calculate a cost grid
        cost_grid = create_grid(N, M, math.inf)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if curr_grid[i][j] > 0:
                    cost_grid[i][j] = max(abs(a-i), abs(b-j))


        # then we get the min cost
        min_cost, min_i, min_j = get_2d_min(cost_grid)

        # infinty cost means there are no more stones (and we have not finished building the tower yet)
        if min_cost == math.inf:
            return -1

        # otherwise we take a stone from here
        else:
            curr_grid[min_i][min_j] -= 1
            steps += 2 * min_cost

    return steps

def get_2d_min(a):
    current_min = math.inf
    current_i = -1
    current_j = -1

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] < current_min:
                current_min = a[i][j]
                current_i, current_j = i, j

    return current_min, current_i, current_j

def create_grid(x, y, content):
    return [[content for _ in range(y)] for _ in range(x)]

def main():
    for q, query in enumerate(queries):
        # this is a type 1 query
        if query[0] == 1:
            i, j, s = query[1:]
            grid[i][j] = s

        # this is a type 0 query
        elif query[0] == 0:
            a, b, K = query[1:]
            print(calculate_no_of_steps(grid, (a, b, K)))

main()
