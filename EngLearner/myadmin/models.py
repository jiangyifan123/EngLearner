from django.db import models

# Create your models here.

class Task(models.Model):
	taskname = models.CharField(max_length = 30, null = True, blank = True, verbose_name = "任务名称")
	taskpoints = models.IntegerField(null = True, blank = True, verbose_name = "任务积分")

	class Meta:
		verbose_name = "任务"
		verbose_name_plural = verbose_name
	
	def __str__(self):
		return "<Task> taskname: %s, taskpoints: %d" % (self.taskname, self.taskpoints)
    
class product(models.Model):
	product_name = models.CharField(max_length = 30, null = True, blank = True, verbose_name = "产品名", unique = True)
	product_price = models.CharField(max_length = 20, null = True, blank = True, verbose_name = "产品价格")
	product_description = models.CharField(max_length = 200, null = True, blank = True, verbose_name = "产品说明")
	product_type = models.CharField(max_length = 20, null = True, blank = True, verbose_name = "语言考试类别")
	product_style = models.CharField(max_length = 20, null = True, blank = True, verbose_name = "类别", default = "单词")

	class Meta:
		verbose_name = "产品"
		verbose_name_plural = verbose_name

	def __str__(self):
		return "<product> name: %s, price: %s, desc: %s" % (self.product_name, self.product_price, self.product_description	)