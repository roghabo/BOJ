n = input()
sum = 0
a = 1
for i in range(1, len(n)+1):
    if i < len(n):
        sum += (((10 * a - 1) - a) + 1) * i
        a *= 10
    else:
        n = int(n)
        sum += (n - a + 1) * i
print(sum)



# 파이썬은 len()으로 자리수를 구함