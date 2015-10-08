#!/usr/bin/python
# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from django.template import RequestContext
from models import Post, Introduce
from config import my_domain


# @brief : 首页
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
def home(request, page_index='1'):
    assert isinstance(request, HttpRequest)

    try:
        page_index = int(page_index)
    except Exception, e:
        print(e.message)
        page_index = 1

    # 计算总页数
    post_num = Post.objects.count()
    post_page = post_num / 6 + 1

    if page_index > post_page or page_index <= 0:
        page_index = 1

    post_page_list = range(1, post_page + 1)

    posts = Post.objects.filter(status='p', is_public=True)\
        .order_by('-is_top', '-publish_time')[5 * (page_index - 1): 5*page_index]

    return render(
        request,
        'index.html',
        RequestContext(request, {
            'my_domain': my_domain,
            'title': 'Home Page',
            'posts': posts,
            'post_page_list': post_page_list,
        })
    )


# @brief : 文章阅读
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
def article(request, link):
    assert isinstance(request, HttpRequest)

    try:
        post = Post.objects.get(link=link)
    except Exception, e:
        print(e.message)
        return Http404

    return render(
        request,
        'article.html',
        RequestContext(request, {
            'my_domain': my_domain,
            'title': post.title,
            'article': post,
        })
    )


# @brief : 关于
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
def about(request):
    assert isinstance(request, HttpRequest)

    try:
        my_introduce = Introduce.objects.all()
        my_introduce_num = Introduce.objects.count()
    except Exception, e:
        print(e.message)
        return Http404

    if my_introduce_num != 1:
        return Http404

    return render(
        request,
        'about.html',
        RequestContext(request, {
            'my_domain': my_domain,
            'title': 'About me',
            'my_introduce': my_introduce[0],
        })
    )


# @brief : 优质的博客
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
def cool_blog(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'cool_blog.html',
        RequestContext(request, {
            'my_domain': my_domain,
            'title': '收藏的博客',
        })
    )


# @brief : 参加过的活动
# @author: stone-jin
# @time  : 2015-10-08
# @email : 1520006273@qq.com
def join_activity(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'join_activity.html',
        RequestContext(request, {
            'my_domain': my_domain,
            'title': '参加过的活动',
        })
    )


# @brief : 我的作品
# @author: stone-jin
# @time  : 2015-10-08
# @email : 1520006273@qq.com
def works(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'works.html',
        RequestContext(request, {
            'my_domain': my_domain,
            'title': '我的作品',
        })
    )
