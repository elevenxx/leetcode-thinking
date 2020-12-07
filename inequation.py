def inequation(k, n, W):
    res = []
    backtrack([], 0, k, n, res, W)
    return res


def backtrack(path, cursum, k, n, res, W):
    if len(path) == k:
        if cursum <= n:
            res.append(path[:])
        return

    for i in range(0, 7):
        path.append(i)
        backtrack(path, cursum + i*W[len(path)-1], k, n, res, W)
        path.pop()


k = 3
n = 12
W = [3, 4, 2] ## 3*x1 + 4*x2 + 2*x3 <= 12 
ans = inequation(k, n, W)
print(ans)
print(len(ans))
