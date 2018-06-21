from django.db import models
import django.utils.timezone as timezone
from django.urls import reverse
from datetime import datetime
# from ckeditor.fields import RichTextField

# Create your models here.

# 分类（用于导航）
class Category(models.Model):
    name = models.CharField(max_length=20,unique=True,verbose_name='文章分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name
        ordering = ['-id']





# 标签(用于标签云)
class Tag(models.Model):
    name = models.CharField(max_length=20,unique=True,verbose_name='文章标签')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name




#文章
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True,verbose_name='文章')
    excerpt = models.CharField(max_length=200, blank=True,verbose_name='文章摘要')
    content = models.TextField(verbose_name='文章正文')
    # content = RichTextField(verbose_name='文章正文')
    image = models.ImageField(upload_to="upload", max_length=100,verbose_name='文章小图')
    views = models.PositiveIntegerField(verbose_name='浏览量', default=0)
    likes = models.IntegerField(verbose_name='点赞数', default=0)
    topped = models.BooleanField(verbose_name='置顶', default=False)
    created_time = models.DateTimeField(verbose_name='发布时间', default=timezone.now)  # auto_now_add=True
    category = models.ForeignKey(Category, blank=False, null=False, verbose_name='文章分类',on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='文章标签')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


class Link(models.Model):
    STATUS_ITEMS = (
        (1,'正常'),
        (2,'删除'),
    )
    title = models.CharField(max_length=50,verbose_name="友链标题")
    href = models.URLField(verbose_name="友链地址")
    status = models.PositiveIntegerField(default=1,choices=STATUS_ITEMS,verbose_name="状态")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name


class Cooperator(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name="合作伙伴")
    href = models.URLField(verbose_name="合作伙伴链接")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '合作伙伴'
        verbose_name_plural = verbose_name


# class Banner(models.Model):
#     title = models.CharField(max_length=100,verbose_name="标题")
#     image = models.ImageField(upload_to="banner",verbose_name="轮播图")
#     url = models.URLField(max_length=200,verbose_name="访问地址")
#     index = models.IntegerField(default=100,verbose_name="顺序")
#     add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = '轮播图'
#         verbose_name_plural = verbose_name
