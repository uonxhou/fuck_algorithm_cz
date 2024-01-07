def can_reach_destination(matrix, k):
    rows, cols = len(matrix), len(matrix[0])

    def dfs(i, j, walls):
        # Check if the current position is out of bounds or a wall
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return False

        # If the number of walls demolished exceeds the limit k, return False
        if walls > k:
            return False

        # If we reach the bottom-right corner, return True
        if i == rows - 1 and j == cols - 1:
            return True

        # Mark the current cell as visited (temporarily set it to 1)
        original_value = matrix[i][j]
        matrix[i][j] = 1

        # Explore all possible directions
        result = (dfs(i + 1, j, walls + original_value) or
                  dfs(i - 1, j, walls + original_value) or
                  dfs(i, j + 1, walls + original_value) or
                  dfs(i, j - 1, walls + original_value))

        # Restore the original value of the cell after exploration
        matrix[i][j] = original_value

        return result

    # Start DFS from the top-left corner
    return dfs(0, 0, 0)


# Example usage:
map_matrix = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0]
]

k = 3

result = can_reach_destination(map_matrix, k)
print(result)


list().__iter__()
