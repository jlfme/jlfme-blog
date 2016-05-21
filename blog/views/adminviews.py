#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2016-03-21 20:35:18
# ---------------------------------------


from django.shortcuts import render
from django.views import generic

from blog.utils.markdown import text_to_markdown


class AddArticleView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, template_name='madmin/admin_index.html', context={'name': 'ok'})

    def post(self, request, *args, **kwargs):
        content = request.POST.get('content')
        content = text_to_markdown(content)
        return render(request, template_name='madmin/preview.html', context={'content': content})
