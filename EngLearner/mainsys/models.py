from django.db import models
import time
# Create your models here.
class words(models.Model):
    word = models.CharField(max_length = 40, default = '', verbose_name = "单词")
    symthm = models.CharField(max_length = 40, default = '', verbose_name = "音标")
    chinese = models.CharField(max_length = 100, default = '', verbose_name = "中文")
    analyzation = models.CharField(max_length = 200, default = '', verbose_name = "联想法")
    product = models.ManyToManyField('myadmin.product')

class writes(models.Model):
    title = models.CharField(max_length=200, default = "无标题", verbose_name="标题")
    time = models.IntegerField(default=0, verbose_name="限制时间")
    problem = models.CharField(max_length=2000, default="", verbose_name="问题")
    top = models.CharField(max_length=300, default="", verbose_name="规范")
    product = models.ForeignKey('myadmin.product', null = True, on_delete=models.CASCADE)

class write_saving(models.Model):
    content = models.CharField(max_length=1000, default = "", verbose_name = "内容")
    writes = models.ForeignKey('writes', on_delete = models.CASCADE, null = True)
    user = models.ForeignKey('users.UserProfile', on_delete = models.CASCADE, null = True)

class read_data(models.Model):
    Date = models.DateField(auto_now_add = True, verbose_name = "创建时间")
    mp3_url = models.CharField(max_length=300, default = "", verbose_name = "mp3内容", null = True)
    eng = models.CharField(max_length=3000, default="", verbose_name = "英文内容")
    chinese = models.CharField(max_length=5000, default="", verbose_name = "中文内容")
    title = models.CharField(max_length=300, default="", verbose_name = "标题")
    url = models.CharField(max_length=300, default = "", verbose_name = "地址")

class listen_data(models.Model):
    Date = models.DateField(auto_now_add = True, verbose_name = "创建时间")
    mp3_url = models.CharField(max_length=300, default = "", verbose_name = "mp3内容", null = True)
    eng = models.CharField(max_length=5500, default="", verbose_name = "英文内容")
    chinese = models.CharField(max_length=3000, default="", verbose_name = "中文内容")
    title = models.CharField(max_length=300, default="", verbose_name = "标题")
    url = models.CharField(max_length=300, default = "", verbose_name = "地址")
    data_time = models.CharField(max_length=1000, default = "", verbose_name = "地址")
