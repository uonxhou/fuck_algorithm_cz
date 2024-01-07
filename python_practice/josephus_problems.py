class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def josephus(n, k, m):
    head = Node(1)
    current = head

    # 构造链表
    for i in range(2, n + 1):
        current.next = Node(i)
        current = current.next

    # 连接链表的头和尾巴
    current.next = head

    # 找到起始点
    for i in range(1, k + 1):
        current = current.next

    out_li = []
    while n > 0:
        for i in range(1, m + 1):
            current = current.next

        out_li.append(current.value)
        current.value = current.next.value
        current.next = current.next.next

        n -= 1

    return out_li


# 示例
n = 7  # 有7个人
k = 3  # 从第3个人开始报数
m = 4  # 报到第4个人出列

result = josephus(n, k, m)
print("出列顺序:", result)
