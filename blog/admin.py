#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2016-03-21 20:48:18
# ---------------------------------------


from django.contrib import admin
from django.utils.html import format_html
from tinymce.widgets import TinyMCE, AdminTinyMCE
from markdown import markdown
from django.db import models
from blog.models import Article, Column, FriendLinks, Category, Comment


class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0
    fields = ('id', 'title', 'status')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    fieldsets = (
        ('SEO信息设置', {
            'fields': ('title', 'keywords', 'description')
        }),
        ('内容', {
            'fields': ('summary', 'content', 'tags')
        }),
        ('发布时间', {
            'fields': ('pub_time',)
        }),
        ('栏目设置', {
            'fields': ('column', )
        }),
    )

    date_hierarchy = 'create_time'    # 以创建时间分类显示
    search_fields = ('title',)
    list_display = ('id', 'title', 'status', 'visit_total', 'rank',
                    'create_time', 'pub_time', 'column', 'show_comment', 'preview', 'show_test')
    list_filter = ('create_time', 'column__name', 'status')

    admin_order_field = ('show_comment')
    # raw_id_fields = ('column',)    # 显示栏目的详细信息(外键)
    list_per_page = 10
    actions = ['make_published']
    list_select_related = ('column',)
    list_editable = ('status', )    # 设定list页面可以编辑
    list_display_links = ('title', 'id', 'show_comment')

    # 更改控件类型
    # formfield_overrides = {models.CharField: {'widget': widgets.Textarea}}
    #
    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     if db_field.name == 'content':
    #         return db_field.formfield(widget=TinyMCE(
    #             attrs={'cols': 280, 'rows': 310},
    #             # mce_attrs={'external_link_list_url': reverse('tinymce-linklist')
    #             #            },
    #         ))
    #     return super(ArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    # 自定义列表显示项目,　list_display
    def preview(self, instance):
        # print('dddddddddddd', type(instance))
        response = format_html("<a href='http://www.baidu.com'>dddddddddddddd</a>")
        return response
    preview.short_description = '预览'

    # 显示评论数
    def show_comment(self, instance):
        return instance.comment_set.all().__len__()
    show_comment.short_description = "评论数"  # 用于admin界面list_display

    # boolean测试
    def show_test(self, instance):
        return True
    show_test.short_description = 'boolean测试'
    show_test.boolean = True

    # 自定义动作
    def make_published(self, request, queryset):
        rows_updated = queryset.update(status=2)
        if rows_updated == 1:
            message_bit = "１篇文章"
        else:
            message_bit = "{}篇文章".format(rows_updated)
        self.message_user(request, "{}成功被删除".format(message_bit))
    make_published.short_description = "设置为删除状态"                # 这里的短描述是action下拉框中显示的描述

    # 重写save操作, 自动处理一些数据信息
    def save_model(self, request, obj, form, change):
        obj.keywords = 'keywords'
        obj.save()


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):

    fields = ('name', 'summary', 'seo_title', 'seo_keywords', 'seo_description')
    search_fields = ('name',)
    list_display = ('name', 'create_time')
    inlines = [ArticleInline]
    list_filter = ('name',)
    list_per_page = 5


@admin.register(FriendLinks)
class FriendLinksAdmin(admin.ModelAdmin):
    fields = ('title', 'link', 'nofollow', 'image')
    search_fields = ('title',)
    list_display = ('title', 'link', 'nofollow', 'image', 'create_time')
    list_filter = ('title', 'nofollow')
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'parent', 'rank', 'status')
    search_fields = ('name',)
    list_display = ('name', 'parent', 'rank', 'status', 'create_time')
    list_filter = ('parent',)
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('article', 'text', 'parent', 'status')
    search_fields = ('article',)
    list_display = ('id', 'text', 'create_time', 'article', 'status', 'parent')
    list_filter = ('parent', 'article')
    list_per_page = 10
