class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        rotated=[[0]* rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                rotated[c][rows-1-r]=matrix[r][c]
        matrix[:]=rotated