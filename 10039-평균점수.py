num = []
for i in range(5):
    check = int(input())
    if check < 40:
        check = 40
    num.append(check)
print(sum(num) // 5)

