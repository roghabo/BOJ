n, k = map(int, input().split())
coins = []
ans = 0
for _ in range(n):
    coins.append(int(input()))
for i in range(1, n + 1):
    if k >= coins[n - i]:
        while k >= coins[n - i]:
            k -= coins[n - i]
            ans += 1
print(ans)
