#!/usr/bin/python
# coding=utf-8

from django.db import models
from django.contrib.auth.models import User
import django.template.defaultfilters
from HTMLParser import HTMLParser
from django.core.urlresolvers import reverse


# @brief : 文章
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
class Post(models.Model):

    STATUS_CHOICES = (
        ('d', u'草稿'),
        ('p', u'发布'),
    )
    title = models.CharField(u'标题', max_length=150, db_index=True, unique=True)
    link = models.CharField(u'链接', max_length=150, default='')
    snippet = models.CharField(u'摘要', max_length=150, default='')
    mk_content = models.TextField(u'原始Markdown内容', default='')
    content = models.TextField(u'内容', default='')

    add_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    publish_time = models.DateTimeField(u'发表时间', null=True)
    update_time = models.DateTimeField(u'修改时间', auto_now=True)
    status = models.CharField(u'状态', max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    is_public = models.BooleanField(u'公开', default=True)
    is_top = models.BooleanField(u'置顶', default=False)
    access_count = models.IntegerField(u'浏览量', default=1, editable=False)
    category = models.ForeignKey('Category', verbose_name=u'所属分类')
    tags = models.ManyToManyField('Tag', verbose_name=u'标签集合', blank=True)
    author = models.ForeignKey(User, verbose_name=u'作者')

    @staticmethod
    def strip_tags(html):
        html = html.strip()
        html = html.strip("\n")
        result = []
        parse = HTMLParser()
        parse.handle_data = result.append
        parse.feed(html)
        parse.close()
        return "".join(result)

    def save(self, *args, **kwargs):
        import markdown
        self.content = markdown.markdown(self.mk_content, ['codehilite'])
        self.link = django.template.defaultfilters.slugify(self.link)
        self.snippet = Post.strip_tags(self.content)[:321]
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'


# @brief : 分类
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
class Category(models.Model):
    title = models.CharField(u'名称', max_length=50, db_index=True, unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title', ]
        verbose_name = u'文章分类'
        verbose_name_plural = u'文章分类'


# @brief : 标签
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
class Tag(models.Model):
    title = models.CharField(u'名称', max_length=50, db_index=True, unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签'


# @brief : 我的介绍
# @author: stone-jin
# @time  : 2015-10-08
# @email : 1520006273@qq.com
class Introduce(models.Model):
    mk_content = models.TextField(u'Markdown内容', default='')
    content = models.TextField(u'内容')
    net_name = models.CharField(u'网名', default='', max_length=32)
    work = models.CharField(u'职业', default='', max_length=64)
    home = models.CharField(u'籍贯', default='', max_length=64)
    tel = models.CharField(u'电话', max_length=16, default='')
    email = models.CharField(u'邮箱', max_length=32, default='')

    def save(self, *args, **kwargs):
        import markdown
        self.content = markdown.markdown(self.mk_content, ['codehilite'])
        super(Introduce, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'个人介绍'

    class Meta:
        verbose_name = u'我的介绍'
        verbose_name_plural = u'我的介绍'


# @brief : 友情链接
# @author: stone-jin
# @time  : 2015-10-08
# @email : 1520006273@qq.com
class FriendLink(models.Model):
    name = models.CharField(u'名称', max_length=150)
    link = models.URLField(u'链接')

    is_top = models.BooleanField(u'是否置顶')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'友情链接'
        verbose_name_plural = u'友情链接'


# @brief : 收藏的博客
# @author: stone-jin
# @time  : 2015-10-08
# @email : 1520006273@qq.com
class CollectBlog(models.Model):
    name = models.CharField(u'博客的名称', max_length=150)
    link = models.URLField(u'链接')
    description = models.TextField(u'博客介绍', default='')

    category = models.ForeignKey('CollectBlogCategory', verbose_name=u'所属分类')
    tag = models.ManyToManyField('CollectBlogTag', verbose_name=u'标签')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'收藏的博客'
        verbose_name_plural = u'收藏的博客'


# @brief : 收藏的博客分类
# @author: stone-jin
# @time  : 2015-10-08
# @email : 1520006273@qq.com
class CollectBlogCategory(models.Model):
    name = models.CharField(u'类型', unique=True, max_length=150)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'收藏的博客分类'
        verbose_name_plural = u'收藏的博客分类'


# @brief : 收藏的博客的标签
# @author: stone-jin
# @time  : 2015-10-08
# @email : 1520006273@qq.com
class CollectBlogTag(models.Model):
    name = models.CharField(u'标签名', unique=True, max_length=150)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'收藏的博客的标签'
        verbose_name_plural = u'收藏的博客的标签'


# @brief : 工具集
# @author: stone-jin
# @time  : 2015-10-09
# @email : 1520006273@qq.com
class Tools(models.Model):
    name = models.CharField(u'工具名', unique=True, max_length=150)
    link = models.URLField(u'链接')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'工具集'
        verbose_name_plural = u'工具集'


class Photos(models.Model):
    name = models.CharField(u'图片名称', max_length=150)
    path = models.CharField(u'图片路径', unique=True, max_length=150)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'随机图片'
        verbose_name_plural = u'随机图片'