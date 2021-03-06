"""stone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from views import home, about, cool_blog, article, join_activity, works, tools, index, post

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^(\d+)$', index, name='index'),
    # url(r'^about$', about, name='about'),
    # url(r'^cool_blog$', cool_blog, name='cool_blog'),
    # url(r'^article/(\w+).html$', article, name='article'),
    # url(r'^join_activity$', join_activity, name='join_activity'),
    # url(r'^works$', works, name='works'),
    # url(r'^tools$', tools, name='tools'),
    # url(r'^post/(.*)', post, name='post'),
]
