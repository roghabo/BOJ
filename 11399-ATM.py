height = []
for i in range(9):
    height.append(int(input()))
flag = False
num = sum(height) - 100
height.sort()

for i in range(9):
    for j in range(i + 1, 9):
        if height[i] + height[j] == num:
            for k in range(9):
                if i == k or j == k:
                    continue
                print(height[k])
            flag = True
            break
    if flag:
        break

