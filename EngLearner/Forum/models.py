from django.db import models

# Create your models here.
class Pages(models.Model):
    Date = models.DateField(auto_now_add = True, verbose_name = "创建日期")
    title = models.CharField(max_length = 30, default = '', verbose_name = "标题")
    content = models.CharField(max_length = 2000, default = '', verbose_name = "内容")
    username = models.CharField(max_length = 20, default = '0', verbose_name = "用户名")
    views = models.IntegerField(default = 0, verbose_name = "观看数")
    comment_num = models.IntegerField(default = 0, verbose_name = "评论数")
    last_view = models.DateField(auto_now = True, verbose_name = "创建日期")

class Commends(models.Model):
    Date = models.DateField(auto_now = True, verbose_name = "评论日期")
    username = models.CharField(max_length = 20, default = '0', verbose_name = "用户名")
    content = models.CharField(max_length = 30, default = '0', verbose_name = "评论内容")
    page = models.ForeignKey('Pages', on_delete=models.CASCADE, null = True)
    like_up = models.IntegerField(default = 0, verbose_name= "点赞数")
    like_down = models.IntegerField(default = 0, verbose_name= "踩数")

class likes(models.Model):
    user = models.ForeignKey('users.UserProfile', on_delete= models.CASCADE)
    operation = models.BooleanField(null = True, verbose_name= "点赞 or 踩")
    page = models.ForeignKey('Pages', on_delete = models.CASCADE, null = True)  
    commend = models.ForeignKey('Commends', on_delete = models.CASCADE, null = True)