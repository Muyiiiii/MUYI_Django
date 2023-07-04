from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route("/register", methods=['GET'])
# def register():
#     return render_template("register.html")
#
#
# @app.route("/post/reg", methods=["POST"])
# def post_register():
#     # 接收到数据
#     print(request.form)
#
#     user = request.form.get("user")
#     pwd = request.form.get("pwd")
#     gender = request.form.get("gender")
#     hobby_list = request.form.getlist("hobby")
#     city = request.form.get("city")
#     skill_list = request.form.getlist("skill")
#     more = request.form.get("more")
#
#     print(user, pwd, gender, hobby_list, city, skill_list, more)
#     # 返回数据
#     return "POST方式 注册成功"

# 可以将上述两个函数合并
# 需要将register的action改成自己
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        print(request.form)

        user = request.form.get("user")
        pwd = request.form.get("pwd")
        gender = request.form.get("gender")
        hobby_list = request.form.getlist("hobby")
        city = request.form.get("city")
        skill_list = request.form.getlist("skill")
        more = request.form.get("more")

        print(user, pwd, gender, hobby_list, city, skill_list, more)

        return "POST方式 注册成功"


# 登陆界面
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        print(request.form)
        user = request.form.get("username")
        pwd = request.form.get("password")
        print(user, pwd)
        return "登陆成功"


if __name__ == '__main__':
    app.run()
