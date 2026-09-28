class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:

        freq = {}

        # Store all rows
        for row in grid:
            row = tuple(row)
            freq[row] = freq.get(row, 0) + 1

        count = 0

        # Check every column
        for j in range(len(grid)):
            column = []

            for i in range(len(grid)):
                column.append(grid[i][j])

            column = tuple(column)

            if column in freq:
                count += freq[column]

        return count