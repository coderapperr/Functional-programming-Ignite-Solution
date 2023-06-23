
# cnt = 0


def generate_solutions(grid, row_sums, col_sums, i, j, total_sum):
    """Generate all valid solutions using backtracking."""
    # Stop if current sum is more than 18 or if remaining spots cannot reach a total of 18
    if total_sum > 18 or (24 - i*6 - j + total_sum) < 18:
        return

    if i == 4:
        if total_sum == 18 and all(sum % 2 == 0 for sum in row_sums + col_sums):
            for row in grid:
                print(row)
            print()
            # global cnt
            # cnt += 1
        return

    if j == 6:
        generate_solutions(grid, row_sums, col_sums, i + 1, 0, total_sum)
        return

    for value in [0, 1]:
        grid[i][j] = value
        row_sums[i] += value
        col_sums[j] += value
        total_sum += value

        generate_solutions(grid, row_sums, col_sums, i, j + 1, total_sum)

        # Backtrack
        grid[i][j] = 0
        row_sums[i] -= value
        col_sums[j] -= value
        total_sum -= value


grid = [[0 for _ in range(6)] for _ in range(4)]
row_sums = [0 for _ in range(4)]
col_sums = [0 for _ in range(6)]
generate_solutions(grid, row_sums, col_sums, 0, 0, 0)
# print(cnt)
