def rotateMatrix(m):
    lm = len(m)
    for i in range(lm//2):
        for j in range(i, lm-i-1):
            ci,cj = i,j
            tmp = m[ci][cj]
            for _ in range(4):
                ni,nj = cj,lm-ci-1
                next = m[ni][nj]
                m[ni][nj] = tmp
                tmp = next
                ci,cj = ni,nj


def printMatrix(m):
    for row in m:
        print(' '.join(map(str, row)))

for n in range(1,6):
    m = [[i*n+j for j in range(n)] for i in range(n)]
    printMatrix(m)
    rotateMatrix(m)
    print()
    printMatrix(m)
    print()

