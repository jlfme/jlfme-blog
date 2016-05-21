#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2016-03-21 20:36:18
# ---------------------------------------


import json
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse, Http404, JsonResponse
from django.views import generic
from blog.models import Article


class ArticleRestfulView(generic.DetailView):
    context_object_name = 'article'
    slug_field = 'pk'
    queryset = Article.published.all()

    def get(self, request, *args, **kwargs):
        super(ArticleRestfulView, self).get(request, *args, **kwargs)
        article = self.get_context_data(**kwargs).get('article')
        print('--------------', article)
        data = json.loads(serialize('json',[article])[1:-1])

        # data = serialize('json',[article])[1:-1]
        #
        #
        # print(type(data))
        return JsonResponse(data=data)

    # def post(self, request, *args, **kwargs):
    #     content = request.POST.get('content')
    #     content = text_to_markdown(content)
    #     return render(request, template_name='madmin/preview.html', context={'content': content})