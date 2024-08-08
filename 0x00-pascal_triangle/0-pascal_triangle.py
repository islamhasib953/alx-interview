def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        traingle = [[1]]
        for i in range(1, n):
            row = [1]
            row += (traingle[i - 1][j - 1] + traingle[i - 1][j] for j in range(1, i))
            row.append(1)
            traingle.append(row)
        return traingle

