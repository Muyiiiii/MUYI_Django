from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


# 添加用户
@app.route("/add/user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")

    user = request.form.get("user")
    pwd = request.form.get("pwd")
    mobile = request.form.get("mobile")

    # 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root123", charset="utf8", db='unicom')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 执行SQL
    sql = "insert into admin(name,password,mobile) values(%s,%s,%s)"
    cursor.execute(sql, [user, pwd, mobile])
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()

    return "添加成功"


@app.route("/show/user")
def show_user():
    # 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root123", charset="utf8", db='unicom')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 执行SQL
    sql = "select * from admin"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    print(data_list)

    # 关闭连接
    cursor.close()
    conn.close()

    return render_template("show_user.html", data_list=data_list)


if __name__ == '__main__':
    app.run()
