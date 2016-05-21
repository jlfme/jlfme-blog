#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2016-03-21 20:47:18
# ---------------------------------------


from markdown import markdown
from django.db import models


class ArticlePublishedManager(models.Manager):

    def get_queryset(self):
        queryset = super(ArticlePublishedManager, self).get_queryset()
        # return queryset.filter(models.Q(status=0) | models.Q(status=1))
        return queryset.filter(status=0)
