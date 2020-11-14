from django.contrib import admin
from .models import *


# Register your models here.
class UserProfileFilter(admin.SimpleListFilter):
    title = '性别'
    parameter_name = 'sex'

    def lookups(self, request, model_admin):
        return (
            ('0', '男'),
            ('1', '女')
        )

    def queryset(self, request, queryset):
        if self.value() in ['0', '1']:
            return queryset.filter(sex=self.value())


class UserProfileAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('user', 'birth', 'phone', 'description', 'sex',)
    list_filter = (UserProfileFilter, 'sex')
    # 搜索框,
    search_fields = ('user',)
    # 选中条目的设置
    actions_selection_counter = True
    actions_on_bottom = False
    actions_on_top = True
    # 不允许点击跳转
    #list_display_links = None
    # 按时间过滤
    date_hierarchy = 'birth'
    list_per_page = 10
    readonly_fields = ('user',)

    actions = ["sex_0", "sex_1"]

    def sex_0(self, request, queryset):
        row_updated = queryset.update(sex=0)
        self.message_user(request, "修改了{}个字段".format(row_updated))

    sex_0.short_description = "性别改为男"

    def sex_1(self, request, queryset):
        row_updated = queryset.update(sex=1)
        self.message_user(request, "修改了{}个字段".format(row_updated))

    sex_1.short_description = "性别改为女"

admin.site.register( UserProfile, UserProfileAdmin, )

class User(admin.ModelAdmin):
    list_display = ('username', 'email', 'data_joined', 'is_active',)


# class EmailAdmin(admin.ModelAdmin):
#     list_display = ['code', 'email', 'send_time', 'email_type']
#     search_fields = ['code', 'email']
#     list_filter = ['send_time', 'exprie_time']
#
# admin.site.register(EmailVeriRecord, EmailAdmin)

