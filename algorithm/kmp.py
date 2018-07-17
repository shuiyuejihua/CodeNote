def prefix_table(ss):
    i, k, m = 0, -1, len(ss)
    pnext = [-1]*m
    while i<m-1:
        if k==-1 or ss[i]==ss[k]:
            k, i = k+1, i+1
            if ss[i]==ss[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext

def kmp(t,p):
    i, j, m, n = 0, 0, len(t), len(p)
    pnext = prefix_table(p)
    while i<m and j<n:
        if j==-1 or t[i]==p[j]:
            i, j = i+1, j+1
        else:
            j = pnext[i]
    if j==m:
        return i-j
    else:
        return -1
