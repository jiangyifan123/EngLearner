# Generated by Django 2.2 on 2020-03-30 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myadmin', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='产品名')),
                ('product_price', models.CharField(blank=True, max_length=20, null=True, verbose_name='产品价格')),
                ('product_description', models.CharField(blank=True, max_length=200, null=True, verbose_name='产品说明')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(blank=True, max_length=30, null=True, verbose_name='任务名称')),
                ('taskpoints', models.IntegerField(blank=True, null=True, verbose_name='任务积分')),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
            },
        ),
    ]