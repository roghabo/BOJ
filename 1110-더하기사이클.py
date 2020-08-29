num = int(input())
if num < 10:
    num = "0" + str(num)
    num = int(num)
new_num = (num % 10) * 10 + ((num // 10 + num % 10) % 10)
cnt = 1
while num != new_num:
    new_num = (new_num % 10) * 10 + ((new_num // 10 + new_num % 10) % 10)
    cnt += 1
    if num == new_num:
        break
print(cnt)
