#!/usr/bin/python
# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import RequestContext
from models import Post


# @brief : 首页
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
def home(request):
    assert isinstance(request, HttpRequest)

    posts = Post.objects.all()

    return render(
        request,
        'layout.html',
        RequestContext(request, {
            'title': 'Home Page',
            'posts': posts,
        })
    )


# @brief : 联系
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
def contact(request):
    assert isinstance(request, HttpRequest)
    return HttpResponse('Contact')


# @brief : 关于
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
def about(request):
    assert isinstance(request, HttpRequest)
    return HttpResponse('about')


# @brief : 优质的博客
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
def cool_blog(request):
    assert isinstance(request, HttpRequest)
    return HttpResponse('Cool blog')
