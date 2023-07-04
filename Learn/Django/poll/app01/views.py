from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json

# Create your views here.

# 全部消息的数据库
DB = []


def home(request):
    return render(request, 'home.html')


def send_msg(request):
    print("接收到的客户端的请求", request.GET)
    text = request.GET.get('text')
    DB.append(text)

    return HttpResponse("OK")


def get_msg(request):
    index = request.GET.get('index')
    index = int(index)
    context = {
        'data': DB[index:],
        'max_index': len(DB),
    }
    # data_string = json.dumps(DB[index:], ensure_ascii=False)
    # 自动转json
    return JsonResponse(context)
