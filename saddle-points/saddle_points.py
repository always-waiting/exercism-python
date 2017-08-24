def saddle_points(matrix):
    ret = set()
    rows = len(matrix)
    if rows == 0:
        return ret
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            try:
                a = matrix[i][j]
                if a  == max(matrix[i]):
                    if a == min([matrix[k][j] for k in range(rows)]):
                        ret.add((i,j))
            except IndexError,e:
                raise ValueError(e)
    return ret
