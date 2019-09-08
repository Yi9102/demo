from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')

def about(request):
    return HttpResponse('<h1 style="color:red;">这是一个关于about的文件</h1>')


