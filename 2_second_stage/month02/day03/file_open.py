"""
打开文件示例
"""

# 打开文件
# f = open("3.txt",'r',encoding='utf-8') # 读  默认

# f = open('file','w')  # 写方式 (文件不存在创建，存在清空)

f = open('file','a') # 追加


print(f)
# 读写文件


# 关闭文件
f.close()
