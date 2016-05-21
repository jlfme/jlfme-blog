#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2016-03-21 20:24:18
# ---------------------------------------


from django.conf.urls import url
from django.views.generic import TemplateView

from blog.views import views, adminviews, restful

urlpatterns = [
    url(r'^timeline/$', TemplateView.as_view(template_name='blog/timeline.html'), name='timeline_view'),
    url(r'^search/$', TemplateView.as_view(template_name='blog/search.html'), name='search_view'),
    url(r'^archives/$', views.ArchivesView.as_view(), name='archives_view'),
    url(r'^article/(?P<pk>\d+)/$', views.ArticleView.as_view(), name='article_detail_view'),
    url(r'^tags/$', views.TagAllView.as_view(), name='tag_all_view'),
    url(r'^tag/(?P<tag>\w+)/$', views.TagDetailView.as_view(), name='tag_detail_view'),
    url(r'^column/(?P<column>\w+)/$', views.ColumnView.as_view(), name='column_detail_view'),
    url(r'^$', views.IndexView.as_view(), name='index_view'),

    # post
    url(r'^madmin/$', adminviews.AddArticleView.as_view(), name='add_article_view'),

    # restful api
    url(r'api/v1/article/(?P<pk>\d+)/$', restful.ArticleRestfulView.as_view(), name='article_restful_view')
]
