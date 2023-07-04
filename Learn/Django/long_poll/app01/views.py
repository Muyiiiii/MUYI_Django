from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
import queue

# Create your views here.

USER_QUEUE = {}


def home(request):
    uid = request.GET.get('uid')
    USER_QUEUE[uid] = queue.Queue()
    return render(request, 'home.html', {'uid': uid})


def send_msg(request):
    text = request.GET.get('text')
    for uid, q in USER_QUEUE:
        q.put(text)

    return HttpResponse("OK")


def get_msg(request):
    uid = request.GET.get('uid')
    q = USER_QUEUE[uid]

    result = {'status': True, 'data': None}
    try:
        data = q.get(timeout=10)  # 若队列为空，等待十秒
        result['data'] = data
    except queue.Empty as e:
        result['status'] = False

    return JsonResponse(result)
