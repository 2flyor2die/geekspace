"""geekspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path,re_path
from blog.views import IndexView,PostView,TagView,ArchiveView,CategoryView,SearchView

app_name = "blog"

urlpatterns = [

    re_path('^index/',IndexView.as_view(),name='index'),
    re_path('^post/(?P<pk>[0-9]+)/$',PostView.as_view(), name='detail'),

    #文章归档目录页
    re_path('^tag/(?P<pk>[0-9]+)/$',TagView.as_view(), name='tag'),

    #导航分类页
    re_path('^category/(?P<pk>[0-9]+)/$',CategoryView.as_view(), name='category'),

    #文章归档目录页
    re_path('^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchiveView.as_view(), name='archive'),

    #搜索页
    re_path('^search/$',SearchView.as_view(),name='search'),
]