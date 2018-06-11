# -*- coding:utf-8 -*-
__date__ = '18-6-10 下午9:13'

from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post

class LatestEntriesFeed(Feed):
    title = "极客空间"
    link = "/geekspace/"
    description = "极客空间－个人技术博客！"

    def items(self):
        return Post.objects.order_by('-created_time')[:4]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt

    # item_link is only needed if NewsItem has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse('news-item', args=[item.pk])