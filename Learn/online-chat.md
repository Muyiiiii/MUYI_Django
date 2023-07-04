# 1 轮询

- 用home访问聊天室
- 使用ajax使得数据返回到后台
- 定时获取消息，然后显示，会有小小的不同步



# 2 长轮询

- 用home访问聊天室
- 每个用户创建一个队列，上传的数据扔到队列里
- 使用ajax使得数据返回到后台
- 使用递归，获取消息，服务端持有连接会有压力



# 3 websocket

- pip install channels

- 配置

  - 注册channels

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'channels',
    ]
    ```

  - 在settings添加asgi_application

    ```python
    ASGI_APPLICATION = '项目名.asgi.application'
    ```

  - 修改asgi.py文件

    ```python
    import os
    from django.core.asgi import get_asgi_application
    from channels.routing import ProtocolTypeRouter,URLRouter
    from . import routing
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '项目名.settings')
    
    # application = get_asgi_application()
    application=ProtocolTypeRouter({
        "http":get_asgi_application(),
        "websocket":URLRouter(routing.websocket_urlpatterns),
    })
    ```

    

  - 在settings同级目录下创建routing文件

    ```python
    from django.urls import re_path
    from app01 import consumers
    
    websocket_urlpatterns = [
        re_path(r'room/(?P<group>\w+)/$', consumers.ChatConsumer.as_asgi()),
    ]
    
    ```

  - 在app01里创建consumers.py（里面实现对于websocket的请求的处理）

    ```python
    from channels.generic.websocket import WebsocketConsumer
    from channels.exceptions import StopConsumer
    from asgiref.sync import async_to_sync
    
    class ChatConsumer(WebsocketConsumer):
        def websocket_connect(self, message):
            # 接受客户端连接
            self.accept()
    
        def websocket_receive(self, message):
            print(message)
    
            self.send("不要回复不要回复不要回复")
    
        def websocket_disconnect(self, message):
            print("断开连接")
            raise StopConsumer()
    ```

- http

  ```
  urls.py
  views.py
  ```

- websocket

  ```
  routings.py
  consumers.py
  ```

  

- 要了解的
  - wsgi
  - asgi
    - 支持了异步和websocket

- routing类似于urls，consumers类似于views



# 群聊实现

## 1

用大数组

consumers.py

```python
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

CONN_LIST = []


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # 接受客户端连接
        print("有人来链接了")
        self.accept()

        CONN_LIST.append(self)

        # 给客户端发消息
        # self.send("来了呀客官")

    def websocket_receive(self, message):
        text = message['text']
        print("接收到的消息-->", text)  # {'type': 'websocket.receive', 'text': '123'}

        if text == "close":
            # 服务端主动关闭连接
            # 会执行websocket_disconnect函数，或者自己主动执行   raise StopConsumer()，使得下面的函数的只处理客户端的断开连接
            self.close()
            return

        res = "{}SB".format(text)

        for conn in CONN_LIST:
            conn.send(res)

    def websocket_disconnect(self, message):
        print("[连接断开]")
        CONN_LIST.remove(self)
        self.send("[连接断开]")
        raise StopConsumer()

```

index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .message {
            height: 300px;
            border: 1px solid #dddddd;
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="message" id="message"></div>
    <div>
        <input type="text" placeholder="请输入" id="txt">
        <input type="button" value="发送" onclick="sendMessage();">
        <input type="button" value="关闭" onclick="closeConn();">
    </div>

    <script>
        //创建websocket连接，用户向客户端发送
        socket = new WebSocket("ws://127.0.0.1:8000/room/123/");

        //连接刚连上时
        socket.onopen = function (event) {
            let tag = document.createElement("div");
            tag.innerText = '[连接成功]';
            document.getElementById("message").appendChild(tag);
        }

        socket.onclose = function (event) {
            let tag = document.createElement("div");
            tag.innerText = '[连接已关闭]';
            document.getElementById("message").appendChild(tag);
        }

        //接收服务端的数据
        socket.onmessage = function (event) {
            let tag = document.createElement("div");
            tag.innerText = event.data;
            document.getElementById("message").appendChild(tag);
        }

        //客户端向服务端发送信息
        function sendMessage() {
            let tag = document.getElementById("txt");
            text = tag.value;
            socket.send(text);
        }

        //关闭连接
        function closeConn() {
            socket.close();
        }
    </script>

</body>
</html>
```



## 2 

用channel layer

- setting中配置

  ```python
  CHANNEL_LAYERS = {
      "default": {
          "BACKEND": "channels.layers.InMemoryChannelLayer",
      }
  }
  ```

  - 或者可以换成redis（要先pip install channels-redis）
