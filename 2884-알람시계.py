h, m = map(int, input().split())

if m >= 45:
    m -= 45
else:
    m = m + 60 - 45
    if h == 0:
        h = 23
    else:
        h -= 1

print(h, m)
