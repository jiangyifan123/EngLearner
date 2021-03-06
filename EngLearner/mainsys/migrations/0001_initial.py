# Generated by Django 2.2 on 2020-04-07 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myadmin', '0003_product_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(default='', max_length=40, verbose_name='单词')),
                ('symthm', models.CharField(default='', max_length=40, verbose_name='音标')),
                ('chinese', models.CharField(default='', max_length=100, verbose_name='中文')),
                ('analyzation', models.CharField(default='', max_length=200, verbose_name='联想法')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.product')),
            ],
        ),
    ]
