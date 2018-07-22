from django.shortcuts import render
# 载入库
from django.http import HttpResponse


import json
# from __future__ import unicode_literals
# Create your views here.

from .forms import AddForm

# 一个响应变量
# def index(request):

#     return HttpResponse('欢迎回来, jackyu')


def index(request):
    return render(request, 'home.html')

# 单选


def table(request):
    return render(request, '单选.html')

# 多选


def table1(request):
    return render(request, '复选.html')


def index1(request):
    return render(request, 'home1.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def home(request):
    string = '我在学习 django, 用来构建网站.'
    return render(request, 'home.html', {'string': string})


def home_list(request):
    tutor_list = ['html', 'css', 'javastript', 'python']
    string = '我在学习 django, 用来构建网站.'
    info_dict = {'a': [1, 2, 3], 'b': '哈哈'}
    return render(request, 'home.html', {"tt": tutor_list,
                                         'string': string, 'info': info_dict,
                                         'List': json.dumps(tutor_list),
                                         'Dict': json.dumps(info_dict)})


def home_1(request):
    List = map(str, range(2))
    return render(request, 'home.html', {'List': List})


def value(request, var):
    # var = 4
    return render(request, 'home.html', {"var": float(var)})
