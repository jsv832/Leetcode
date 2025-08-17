def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    M = len(matrix)
    N = len(matrix[0])

    l = 0
    r = M*N -1

    while l <= r:
        m = (l + r) // 2
        mid_x = (m // N)
        mid_y = (m % N)
        if matrix[mid_x][mid_y] == target:
            return True
        elif matrix[mid_x][mid_y] > target:
            r = m - 1
        else:
            l = m + 1
            
    return False