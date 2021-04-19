heights = []
for i in range(9):
    heights.append(int(input()))

sum = 0
flag = False
for i in range(9):
    sum+=heights[i]

for i in range(9):
    for j in range(9):
        if (i!=j) and ((sum-heights[i]-heights[j])==100):
            heights[i]=101
            heights[j]=101
            flag = True
            break
    if flag:
        break

heights.sort()
for i in range(7):
    print(heights[i])