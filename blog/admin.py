from django.contrib import admin

# Register your models here.

from .models import Category,Post,Tag,Link,Cooperator,Carousel


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','excerpt','created_time','category','content']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['title','href','status']

@admin.register(Cooperator)
class CooperatorAdmin(admin.ModelAdmin):
    list_display = ['name','href','status']

@admin.register(Carousel)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title','image','url','index','content']


