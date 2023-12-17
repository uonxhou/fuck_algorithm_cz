# 牛客网 HJ16
# https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4


from collections import defaultdict

# 处理输入
n, m = map(int, input().split())
n //= 10  # 价格总为 10 的倍数，优化空间复杂度
prices = defaultdict(lambda: [0, 0, 0])  # 主从物品的价格
values = defaultdict(lambda: [0, 0, 0])  # 主从物品的价值

for i in range(m):      # i 代表第 i + 1 个物品
    v, p, q = map(int, input().split())
    v //= 10            # 价格总为 10 的倍数，优化空间复杂度
    if q == 0:          # 追加主物品
        prices[i + 1][0] = v
        values[i + 1][0] = v * p
    elif prices[q][1]:  # 追加从物品
        prices[q][2] = v
        values[q][2] = v * p
    else:
        prices[q][1] = v
        values[q][1] = v * p

# 处理输出
dp = [0] * (n + 1)  # 初始化 dp 数组

for i, v in prices.items():
    for j in range(n, v[0] - 1, -1):
        p1, p2, p3 = v
        v1, v2, v3 = values[i]
        # 处理主从组合的四种情况
        dp[j] = max(dp[j], dp[j - p1] + v1)
        dp[j] = max(dp[j], dp[j - p1 - p2] + v1 + v2) if j >= p1 + p2 else dp[j]
        dp[j] = max(dp[j], dp[j - p1 - p3] + v1 + v3) if j >= p1 + p3 else dp[j]
        dp[j] = max(dp[j], dp[j - p1 - p2 - p3] + v1 + v2 + v3) if j >= p1 + p2 + p3 else dp[j]

print(dp[n] * 10)
