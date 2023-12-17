# 面试中准备01背包和完全背包就够了

# 01背包

# 二维DP数组解法
# n, v 分别代表物品数量, 背包容积
# acm 模式
n, v = map(int, input().split())
# w为物品价值, c为物品体积(花费)
w, cost = [0], [0]
for i in range(n):
    cur_c, cur_w = map(int, input().split())
    w.append(cur_w)
    cost.append(cur_c)

# 该初始化代表背包不一定要装满
dp = [[0 for j in range(v+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, v+1):
        if j < cost[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-cost[i]] + w[i], dp[i-1][j-cost[i]])

print(dp[n][v])





# 完全背包
