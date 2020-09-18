import collections
n = int(input())
points = [[] for i in range(n)]
for i in range(n):
    points[i] = list(map(int, input().split()))
print(points)

ans = 0
for i in range(n):
    dic = collections.defaultdict(int)
    for j in range(n):
        if i == j:
            continue
        distance = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
        dic[distance] += 1
    for k in dic:
        ans += dic[k] * (dic[k]-1)
print(ans)

