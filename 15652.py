import sys
n,m = map(int, input().split())
c = [False] * (n+1)
a = [0] * m

def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(1, n+1):
        if index > 0:
            if a[index-1] > i:
                continue
        a[index] = i
        go(index+1, n, m)

go(0, n, m)