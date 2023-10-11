def funct(matrix, t1, t2) -> int:

    def dist(pos, t1, t2):
        d1 = abs(pos[0] - t1[0]) + abs(pos[1] - t1[1])
        d2 = abs(pos[0] - t2[0]) + abs(pos[1] - t2[1])
        return max(d1, d2)

    exp_ht = max(matrix[t1[0]][t1[1]], matrix[t2[0]][t2[1]])
    min_dist = float("infinity")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i,j) == t1 or (i,j) == t2:
                continue
            elif matrix[i][j] >= exp_ht:
                if min_dist > dist((i,j), t1, t2):
                    ans_pos = (i, j)
                    min_dist = dist((i,j), t1, t2)

    return matrix[ans_pos[0]][ans_pos[1]]


if __name__ == "__main__":
    matrix= [
        [9,1,7,3],
        [1,6,5,3],
        [1,6,4,3]
    ]
    t1 = (1,2)
    t2 = (2,1)
    print(funct(matrix, t1, t2))