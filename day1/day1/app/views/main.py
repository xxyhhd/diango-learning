from django.shortcuts import render, HttpResponse 
# render：渲染模板，HttpReponse：响应

# Create your views here.


def index(req):
    return HttpResponse('Hello, 你好')

def test(req):
    return HttpResponse('测试')