from django.db import models

# Create your models here.

from django.db import models
from blog.models import Post
from datetime import datetime
# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    url = models.URLField(blank=True)
    comments = models.TextField(verbose_name="评论",max_length=200)
    add_time = models.DateTimeField(verbose_name="评论时间", default=datetime.now)
    post = models.ForeignKey(Post,verbose_name="文章",on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "文章评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name