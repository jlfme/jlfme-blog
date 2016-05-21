#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2016-03-21 20:48:18
# ---------------------------------------


from django.db import models
from django.shortcuts import reverse
from blog.managers import ArticlePublishedManager


STATUS = {
        0: '正常',
        1: '草稿',
        2: '删除',
}

ARTICLE_STATUS_CHOICES = (
    (0, '发布'),
    (1, '草稿'),
    (2, '删除')
)

LINKS_NOFOLLOW_CHOICES = (
    (0, '是'),
    (1, '否')
)


COMMENT_STATUS_CHOICES = (
    (0, '已审核'),
    (1, '未审核')
)


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='名称')
    parent = models.ForeignKey('self', default=None, blank=True, null=True, verbose_name='上级分类')
    rank = models.IntegerField(default=0, verbose_name='排序')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='状态')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = verbose_name = '分类'
        ordering = ['rank', '-create_time']
        # app_label = string_with_title('blog', "博客管理")
    #
    # def get_absolute_url(self):
    #     from django.core.urlresolvers import reverse
    #     return reverse('category-detail-view', args=(self.name,))

    def __str__(self):
        if self.parent:
            return '%s-->%s' % (self.parent, self.name)
        else:
            return self.name


class Column(models.Model):
    name = models.CharField(max_length=50, verbose_name='栏目名称')
    summary = models.TextField(verbose_name='栏目摘要')
    seo_title = models.CharField(max_length=100, verbose_name='SEO标题')
    seo_keywords = models.CharField(max_length=100, verbose_name='SEO关键词', help_text='关键词用逗号分割')
    seo_description = models.CharField(max_length=100, verbose_name='SEO描述', help_text='不要超过100个字符')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '栏目管理'
        verbose_name = '栏目'
        ordering = ['id']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    keywords = models.CharField(max_length=100, verbose_name='关键词', blank=True)
    description = models.CharField(max_length=100, verbose_name='描述', blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True,
                            verbose_name='标签', help_text='可以有多个标签，用逗号分隔')
    summary = models.TextField(verbose_name='摘要', blank=True)
    content = models.TextField(verbose_name='正文')
    column = models.ForeignKey(Column, verbose_name='所属栏目')
    visit_total = models.IntegerField(default=10, verbose_name='访问次数')
    votes = models.IntegerField(default=0, verbose_name='点赞')
    rank = models.IntegerField(default=0, verbose_name='排序')
    status = models.IntegerField(default=2, choices=ARTICLE_STATUS_CHOICES, verbose_name='状态')
    pub_time = models.DateTimeField(null=True, blank=True, verbose_name='发布时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    # 自定义管理器
    objects = models.Manager()
    published = ArticlePublishedManager()

    class Meta:
        verbose_name_plural = '文章管理'
        verbose_name = '文章'
        ordering = ['id']

    def __str__(self):
        return self.title

    def is_visible(self):
        return self.status == 0
        # return False

    @property
    def markdown(self):
        """
        将content格式化成markdown
        """
        from blog.utils.markdown import text_to_markdown
        return text_to_markdown(self.content)

    @property
    def next_article(self):
        """
        Returns the next published entry if exists
        """
        return self.previous_next_articles[1]

    @property
    def previous_article(self):
        """
        Returns the previous published entry if exists
        """
        return self.previous_next_articles[0]

    @property
    def previous_next_articles(self):
        """
        Returns and caches a tuple containing the next
        and previous published entries.
        """
        previous_next = getattr(self, 'previous_next', None)
        if previous_next is None:
            if not self.is_visible():
                previous_next = (None, None)
            else:
                article_list = list(self.__class__.published.all().filter(column=self.column))
                index = article_list.index(self)
                try:
                    previous = article_list[index + 1]
                except IndexError:
                    previous = None
                if index:
                    _next = article_list[index - 1]
                else:
                    _next = None
                previous_next = (previous, _next)
            setattr(self, 'previous_next', previous_next)
        return previous_next

    def get_absolute_url(self):
        return reverse('blog:article_detail_view', kwargs={'pk': self.pk})

    def get_tags(self):
        if self.tags:
            tags_list = self.tags.split(',')
            while '' in tags_list:
                tags_list.remove('')
            return tags_list
        else:
            return []

    def save(self, *args, **kwargs):
        print('-----------------------------override article save------------------------------------')
        super(Article, self).save(*args, *kwargs)


class FriendLinks(models.Model):
    title = models.CharField(max_length=100, verbose_name='链接标题')
    link = models.CharField(max_length=100, verbose_name='网址')
    nofollow = models.IntegerField(default=0, choices=LINKS_NOFOLLOW_CHOICES, verbose_name='nofollow')
    image = models.ImageField(upload_to='img', default='/ddddd.jpg', blank=True, verbose_name='图片路径')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '友情链接'
        verbose_name = '友情链接'
        ordering = ['id']

    def __str__(self):
        return self.title


class Comment(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户')
    article = models.ForeignKey(Article, verbose_name='所属文章')
    text = models.TextField(verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    status = models.BooleanField(default=True, verbose_name='审核状态')
    parent = models.ForeignKey('self', default=None, blank=True, null=True, verbose_name='引用')

    class Meta:
        verbose_name_plural = '评论管理'
        verbose_name = '评论'
        ordering = ['-create_time']

    def __str__(self):
        return self.article.title + '_' + str(self.pk)


class Logs(models.Model):

    user = models.CharField(max_length=20, verbose_name='用户')
    action = models.CharField(max_length=20, verbose_name='操作')
    action_time = models.DateTimeField(auto_now=True, verbose_name='操作时间')
