from django.shortcuts import render


# Create your views here.

def index(request):
    num = request.GET.get('num')
    return render(request, 'index.html', {'num': num})
