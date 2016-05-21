#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2016-03-21 20:41:18
# ---------------------------------------


from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.views import generic
from django.views.generic.dates import MonthArchiveView
from django.core.cache import caches
from django.contrib import auth
from django.utils.datastructures import MultiValueDict
from blog.models import Article, Column, Logs, FriendLinks
from blog.views.mixins.info import BaseInfoMinxin


data_cache = caches['default']    # 开启缓存


class ArticleView(generic.DetailView):
    template_name = 'blog/article.html'
    queryset = Article.published.all()
    context_object_name = 'article'
    slug_field = 'pk'

    def get(self, request, *args, **kwargs):
        # 获取真实的访问IP
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        article_pk = kwargs.get('pk')
        visited_ip_list = data_cache.get(article_pk, [])   # 获取当前文章(10*60)时间内访问的所有IP地址

        # 如果当前IP地址不在缓存内，文章访问量增加１
        if ip not in visited_ip_list:
            try:
                article = self.queryset.get(pk=article_pk)
                print(article.get_tags())
            except Article.DoesNotExist:
                raise Http404
            else:
                article.visit_total += 1
                article.save()
            # 更新IP缓存
            visited_ip_list.append(ip)
            data_cache.set(article_pk, visited_ip_list, 10*60)
        return super(ArticleView, self).get(request, *args, **kwargs)


class ArchivesView(generic.TemplateView):
    template_name = 'blog/archives.html'

    # 根据年和月查询文章总数和文章列表
    def get_articles(self, year, month):
        articles = Article.objects.filter(
            create_time__year=year,
            create_time__month=month,
            status=0)
        return articles

    def get_context_data(self, **kwargs):
        date_list = Article.objects.filter(status=0).dates('create_time', 'month', order='DESC')
        dct = MultiValueDict()
        for date_obj in date_list:
            year = date_obj.year
            month = date_obj.month
            articles = self.get_articles(year, month)
            dct.appendlist(year, {'month': month, 'articles': articles})

        archives_list = [(key, dct.getlist(key)) for key in dct]
        archives_list = sorted(archives_list, reverse=True)  # 根据年逆序排序　[(2017, [(6, 2), (5, 2)]), ...]
        kwargs.update({'archives_list': archives_list})
        return kwargs


class TagDetailView(generic.ListView):
    template_name = 'blog/tag_detail.html'
    context_object_name = 'article_list'
    paginate_by = 2

    def get_queryset(self):
        tag = self.kwargs.get('tag', '')
        article_list = Article.objects.filter(tags__icontains=tag)
        return article_list

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        return BaseInfoMinxin.get_context_data(context)


class TagAllView(generic.TemplateView):
    template_name = 'blog/tag_all.html'

    def get_context_data(self, **kwargs):
        article_list = Article.objects.all().filter(status=0)
        tag_set = set()
        for article in article_list:
            tag_list = article.get_tags()
            tag_set.update(set(tag_list))
        tag_css_list = ['btn-primary', 'btn-success', 'btn-info', 'btn-warning', 'btn-danger']  # 用于显示tag的css类名
        kwargs.update({'tag_set': tag_set, 'tag_css_list': tag_css_list})
        return kwargs


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    paginate_by = 10

    def get_queryset(self):
        article_list = Article.published.all()
        return article_list

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return BaseInfoMinxin.get_context_data(context)


class ColumnView(generic.ListView):
    template_name = 'blog/column_detail.html'
    context_object_name = 'article_list'
    paginate_by = 5

    def get_queryset(self):
        column = self.kwargs.get('column', '')
        article_list = Article.objects.filter(column__name=column, status=0)
        print(article_list, article_list.count())
        return article_list
