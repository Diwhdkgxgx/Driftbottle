from django.contrib import admin
from .models import *
# Register your models here.

# class BottleArticlesAdmin(admin.ModelAdmin):
#     list_display = ("title", "author", "publish")
#     list_filter = ("publish", "author")
#     search_fields = ('title', "body") #设置搜索
#     raw_id_fields = ("author",) #我也没搞懂这个有啥用
#     date_hierarchy = "publish" #按年份查询
#     ordering = ['-publish', 'author'] #排序

# admin.site.register(BottleArticles, BottleArticlesAdmin)

class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = ('id','author', 'slug','title', 'body', 'created', 'updated')
    list_filter = ('artitag',)
    actions_selection_counter = True
    actions_on_bottom = False
    actions_on_top = True
    date_hierarchy = 'updated'

admin.site.register( ArticleInfo, ArticleInfoAdmin )