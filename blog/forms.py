#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2016-03-21 20:47:18
# ---------------------------------------


from django import forms
from blog.models import Article
from django.forms import formsets


class ArticleForm(forms.ModelForm):
    module = Article


class MyForm(forms.Form):

    name = forms.CharField()
    pub_date = forms.DateTimeField()


MyFormSet = formsets.formset_factory(MyForm, extra=5)
