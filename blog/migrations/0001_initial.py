# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2016-03-21 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('keywords', models.CharField(blank=True, max_length=100, verbose_name='关键词')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='描述')),
                ('tags', models.CharField(blank=True, help_text='可以有多个标签，用逗号分隔', max_length=200, null=True, verbose_name='标签')),
                ('summary', models.TextField(blank=True, verbose_name='摘要')),
                ('content', models.TextField(verbose_name='正文')),
                ('visit_total', models.IntegerField(default=10, verbose_name='访问次数')),
                ('votes', models.IntegerField(default=0, verbose_name='点赞')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.IntegerField(choices=[(0, '发布'), (1, '草稿'), (2, '删除')], default=2, verbose_name='状态')),
                ('pub_time', models.DateTimeField(blank=True, null=True, verbose_name='发布时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name_plural': '文章管理',
                'verbose_name': '文章',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='名称')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='上级分类')),
            ],
            options={
                'verbose_name_plural': '分类',
                'verbose_name': '分类',
                'ordering': ['rank', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='栏目名称')),
                ('summary', models.TextField(verbose_name='栏目摘要')),
                ('seo_title', models.CharField(max_length=100, verbose_name='SEO标题')),
                ('seo_keywords', models.CharField(help_text='关键词用逗号分割', max_length=100, verbose_name='SEO关键词')),
                ('seo_description', models.CharField(help_text='不要超过100个字符', max_length=100, verbose_name='SEO描述')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '栏目管理',
                'verbose_name': '栏目',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('status', models.BooleanField(default=True, verbose_name='审核状态')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='所属文章')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment', verbose_name='引用')),
            ],
            options={
                'verbose_name_plural': '评论管理',
                'verbose_name': '评论',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='FriendLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='链接标题')),
                ('link', models.CharField(max_length=100, verbose_name='网址')),
                ('nofollow', models.IntegerField(choices=[(0, '是'), (1, '否')], default=0, verbose_name='nofollow')),
                ('image', models.ImageField(blank=True, default='/ddddd.jpg', upload_to='img', verbose_name='图片路径')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '友情链接',
                'verbose_name': '友情链接',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='用户')),
                ('action', models.CharField(max_length=20, verbose_name='操作')),
                ('action_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Column', verbose_name='所属栏目'),
        ),
    ]
