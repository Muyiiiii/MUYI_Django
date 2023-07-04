from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    # 找到占位符，进行替换
    users = ["huhu", "haha", "hihi"]
    return render_template("index.html", title="哈哈", data_list=users)


if __name__ == '__main__':
    app.run()
