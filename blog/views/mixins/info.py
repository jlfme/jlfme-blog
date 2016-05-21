#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2016-03-21 20:43:18
# ---------------------------------------


from blog.models import FriendLinks


class BaseInfoMinxin(object):
    """加载基本信息"""

    @staticmethod
    def get_context_data(context):
        try:
            context['flink_list'] = FriendLinks.objects.all()
        except Exception as e:
            print("加载基本信息出错了!")
        print(context)
        return context
