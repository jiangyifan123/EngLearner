# Generated by Django 2.2 on 2020-04-06 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0017_auto_20200406_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='opertaion',
            field=models.BooleanField(null=True, verbose_name='点赞 or 踩'),
        ),
    ]