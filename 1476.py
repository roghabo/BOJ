e, s, m = map(int, input().split())
result = 0
i,j,k=0,0,0
while True:
    if(i == 15):
        i = 1
    else:
        i += 1

    if(j == 28):
        j = 1
    else:
        j += 1

    if(k == 19):
        k = 1
    else:
        k += 1
    
    result +=1
    if(i==e and j==s and k==m):
        print(result)
        break
