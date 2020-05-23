from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone as timezone
# Create your models here.

class UserProfile(AbstractUser):
	mobile = models.CharField(max_length = 11, verbose_name = "电话")
	email = models.CharField(max_length = 100, null = True, blank = True, verbose_name = '邮箱')
	auth = models.CharField(max_length=10, verbose_name = "权限", default = "common")
	like = models.ManyToManyField('Forum.Pages')

	class Meta:
		verbose_name = "用户"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.username

class Parameter(models.Model):
	points = models.CharField(max_length = 20, default = '0', verbose_name = "积分")
	coins = models.CharField(max_length = 20, default = '0', verbose_name = "虚拟币")
	checknum = models.CharField(max_length = 20, default = '0', verbose_name = '打卡天数')
	scholarship = models.CharField(max_length = 20, default = '0', verbose_name = '奖学金')
	user = models.ForeignKey('UserProfile', null = True, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "用户数据"
		verbose_name_plural = verbose_name
	
	def __str__(self):
		return "<Parameter> points: %s, coins: %s, checknum: %s, scholarship: %s" % (self.points, self.coins, self.checknum, self.scholarship)

class shoppingCart(models.Model):
	Date = models.DateField(default= timezone.now, verbose_name = "添加产品进购物车时间")
	product = models.ManyToManyField('myadmin.product')
	user = models.OneToOneField('UserProfile', null = True, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "购物车"
		verbose_name_plural = verbose_name


class boughtProduct(models.Model):
	Date = models.DateField(default= timezone.now, verbose_name = "买商品的时间")
	product = models.ForeignKey('myadmin.product', null=True, on_delete=models.CASCADE)
	user = models.ForeignKey('UserProfile', null = True, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "已买的产品"
		verbose_name_plural = verbose_name

class taskList(models.Model):
	taskDate = models.DateField(default= timezone.now, verbose_name = "任务完成时间")
	task = models.ForeignKey('myadmin.Task', null = True, on_delete=models.CASCADE)
	user = models.ForeignKey('UserProfile', null = True, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "已完成任务表"
		verbose_name_plural = verbose_name

class tradeRecord(models.Model):
	Date = models.DateField(auto_now = True, verbose_name = "购买日期")
	recordId = models.CharField(max_length = 20, default = '0', verbose_name = "订单号")
	user = models.ForeignKey('UserProfile', null = True, on_delete=models.CASCADE)
	Total = models.CharField(max_length = 10, default = '0', verbose_name = "价格")
	desc = models.CharField(max_length = 20, default = '0', verbose_name = "描述")
	status = models.CharField(max_length = 10, default = '正在支付', verbose_name = "状态")

	class Meta:
		verbose_name = "交易记录"
		verbose_name_plural = verbose_name

class word_forget(models.Model):
	Date = models.DateField(auto_now = True, verbose_name = "购买日期")
	word = models.ForeignKey('mainsys.words', null = True, on_delete = models.CASCADE, verbose_name = "错误的单词")
	user = models.ForeignKey('UserProfile', null = True, on_delete = models.CASCADE, verbose_name = "用户")
	count = models.IntegerField(default = 1, verbose_name = "错误单词次数")

class words_log(models.Model):
	user = models.ForeignKey('UserProfile', null = True, on_delete = models.CASCADE)
	product = models.ForeignKey('myadmin.product', null = True, on_delete = models.CASCADE)
	pos = models.IntegerField(default = 0, verbose_name = "进度")