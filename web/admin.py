from django.contrib import admin
from models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Introduce)
admin.site.register(FriendLink)
admin.site.register(CollectBlog)
admin.site.register(CollectBlogCategory)
admin.site.register(CollectBlogTag)
admin.site.register(Tools)
admin.site.register(Photos)
