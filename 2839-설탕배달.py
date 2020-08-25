num = int(input())
result = 0
while True:
    if (num % 5) == 0:
        result = result + num // 5
        break
    num = num - 3
    result += 1
    if num < 0:
        result = -1
        break
print(result)
