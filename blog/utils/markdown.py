#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2016-03-21 20:33:18
# ---------------------------------------


from markdown import markdown


def text_to_markdown(text, code_style='google_prettify'):
    """ 将markdown文本转换成html

    :param text:
    :param code_style: 'pretty_print' use google prettyprint code style
    :return:

    """

    kwargs = {
        'extensions': [
           'markdown.extensions.extra',
           'markdown.extensions.codehilite',
           'markdown.extensions.toc',
           'markdown.extensions.tables',
           'markdown.extensions.abbr']
    }
    # 设置代码风格为google-prettify
    if code_style == 'google_prettify':
        config = {
            'markdown.extensions.codehilite': {
                'use_pygments': False,
                'css_class': 'prettyprint linenums'
            },

            'markdown.extensions.tables': {}

        }
        kwargs.update({'extension_configs': config})

    return markdown(text, **kwargs)
