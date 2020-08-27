t = int(input())
result = []
for i in range(t):
    a, b = map(int, input().split())
    result.append(a + b)

for i in range(t):
    print(result[i])

"""
t = int(input())
result = []
while t:
    a, b = map(int, input().split())
    result.append(a + b)
    t -= 1
for i in range(t):
    print(result[i])
"""
