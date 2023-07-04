import pymysql

# 连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root123", charset="utf8", db='unicom')

# 收发数据的"手"
# 参数可以不写
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 发送指令，千万不要用字符串格式化去写SQL拼接，会有SQL注入的隐患
# 如下使用sql自己的才可以
sql = "update admin set mobile=%s where id=%s"
cursor.execute(sql, ["1888", 1])

# # 另一种写法，要用字典
# sql = "insert into admin(name,password,mobile) values(%(n1)s,%(n2)s,%(n3)s)"
# cursor.execute(sql, {"n1": "uhuh", "n2": "098", "n3": "19999999"})

# 提交
conn.commit()

# 关闭
cursor.close()
conn.close()
