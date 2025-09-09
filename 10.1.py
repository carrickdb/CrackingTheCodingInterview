def merge(A,B):
    lena, lenb = len(A), len(B)
    pa,pb,pc = lena-lenb-1,lenb-1,lena-1
    while pb >= 0:
        if pa >= 0 and A[pa] > B[pb]:
            A[pc] = A[pa]
            pa -= 1
        else:
            A[pc] = B[pb]
            pb -=1
        pc -= 1


A = [1,4,5]
B = [2,3,7,9]
A.extend([0] * len(B))
merge(A,B)
print(A)