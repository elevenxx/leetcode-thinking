import collections
n = int(input())
lists = [[] for _ in range(n)]
#优秀建设者，可靠接班人
for i in range(n):
    lists[i] = list(map(int, input().split()))
print(lists)

A, B, C, D = lists[0], lists[1], lists[2], lists[3]
dic = collections.Counter()
ans = 0
for a in A:
    for b in B:
        dic[a+b] += 1
for c in C:
    for d in D:
        ans += dic[-c-d]
print(ans)
