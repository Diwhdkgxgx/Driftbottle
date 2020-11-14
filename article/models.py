from django.db import models
from Secondwork.settings import *
from django.utils import timezone
from django.contrib.auth.models import User
from slugify import slugify
from django.urls import reverse
# Create your models here.
class ArticleTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField('标签', max_length=500, blank=True)
    zhuangtai = models.CharField(max_length=5, default="已投放")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag

class ArticleInfo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    slug = models.SlugField(max_length=500)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    artitag = models.ManyToManyField(ArticleTag, blank=True, verbose_name="标签分类")

    class Meta:
        ordering = ("title",)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(ArticleInfo, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])

class Comment(models.Model):
    article = models.ForeignKey(ArticleInfo, on_delete=models.CASCADE,verbose_name="所属瓶子")
    commentator = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="评论用户")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body

#Comment by {0} on {1}".format(self.commentator,
class Bottle(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.OneToOneField(ArticleInfo, on_delete=models.CASCADE, verbose_name="所属瓶子文字")
    zhuangtai = models.IntegerField(default=0, verbose_name="瓶子的状态")
    postuser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="发布用户",related_name='post_user')
    getuser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="获取用户",related_name='get_user',blank=True, null=True)
    com = models.ForeignKey(Comment,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id)


    class Meta:
        verbose_name = '瓶子状态'

