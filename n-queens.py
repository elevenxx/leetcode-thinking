def bfs(num):
    global count
    global ans
    ans = []
    queues = []   # 皇后点的队列
    # 初始化所有可能的点  也就是第一行中的所有点
    for i in range(num):
        queues.append(tuple((0, i, [0], [i], [0+i], [0-i]))) # 点x, 点y，行，列，xy_sum, xy_dif
    while queues:
        row, col, rows, cols, xy_sum, xy_dif = queues.pop(0)
        if row == num-1:  # 到达最后一行了，将结果加1，直接下一轮
            count += 1
            ans.append(cols)
            continue
        row += 1
        for col in range(num):  # 判断每个位置是否可以存放
            if row not in rows and col not in cols and row+col not in xy_sum and row-col not in xy_dif:
                queues.append(tuple((row, col, rows+[row], cols+[col], xy_sum+[row+col], xy_dif+[row-col])))
    return count

global count
global ans
count = 0
bfs(8)
print(count)
print(ans)
