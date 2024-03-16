"""
文件偏移量
"""

# 读写方式打开
f = open('file','wb+')

f.write("Hello world\n".encode())
f.flush()

# 查看文件偏移量位置
print("文件偏移位置：",f.tell())

# 操作文件偏移量
re = f.seek(-11,2)

print("读取内容：",f.read())
print(re)

f.close()
