def transpose(*args, **kwargs):
    tr_matrix = []
    for j in range(m):
        tr_matrix.append([])
        for i in range(n):
            tr_matrix[j].append(matrix[i][j])

    return tr_matrix


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in transpose(n, m, matrix):
    print(*i)
