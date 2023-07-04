from flask import Flask,render_template

app = Flask(__name__)  # 实例化了Flask类


# 创建了网址 /show/info 和 index函数的对应关系
# 以后进入网址，就会自动执行index函数
@app.route("/show/info")
def index():
    # return "中国联通"
    # 会自动打开这个文件，并读取内容，将内容返回（默认去当前项目的templates文件夹中找）
    return render_template("index.html")

@app.route("/get/news")
def get_news():
    # 会自动打开这个文件，并读取内容，将内容返回（默认去当前项目的templates文件夹中找）
    return render_template("get_news.html")

@app.route("/goods/list")
def goods_list():
    # 会自动打开这个文件，并读取内容，将内容返回（默认去当前项目的templates文件夹中找）
    return render_template("goods_list.html")

@app.route("/user/list")
def user_list():
    # 会自动打开这个文件，并读取内容，将内容返回（默认去当前项目的templates文件夹中找）
    return render_template("user_list.html")

@app.route("/register")
def register():
    # 会自动打开这个文件，并读取内容，将内容返回（默认去当前项目的templates文件夹中找）
    return render_template("register.html")

if __name__ == '__main__':
    app.run()