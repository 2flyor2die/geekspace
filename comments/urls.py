# -*- coding:utf-8 -*-
__date__ = '18-6-8 下午1:39'

from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    # 评论详情页
    url(r'^post/(?P<post_pk>\d+)/',views.add_comment,name = 'add_comment'),
]