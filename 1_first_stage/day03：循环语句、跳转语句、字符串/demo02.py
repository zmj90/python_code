"""
    for
"""
# range
# 不包含终点
# 写法1：range(起点,终点,间隔)
for item in range(1, 10, 1):
    print(item)  # 1 2 .... 9
# 写法2：range(终点)
for item in range(6):
    print(item)  # 0 1 2 .. 5
# 写法3：range(起点,终点)
for item in range(3, 9):
    print(item)  # 3 4 ... 8

message = "我是花果山水帘洞美猴王孙悟空"
for item in message:
    print(item)
