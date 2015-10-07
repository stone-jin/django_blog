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
    tags = models.ManyToManyField('Tag', verbose_name=u'标签集合', null=True, blank=True)
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

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=(self.id, self.link))

    def __unicode__(self):
        return self.title


# @brief : 分类
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
class Category(models.Model):
    title = models.CharField(u'名称', max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ['title', ]

    def __unicode__(self):
        return self.title


# @brief : 标签
# @author: stone-jin
# @time  : 2015-10-07
# @email : 1520006273@qq.com
class Tag(models.Model):
    title = models.CharField(u'名称', max_length=50, db_index=True, unique=True)

    def __unicode__(self):
        return self.title
