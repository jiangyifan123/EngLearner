# Generated by Django 2.2 on 2020-04-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0020_auto_20200407_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='comment_num',
            field=models.IntegerField(default=0, verbose_name='评论数'),
        ),
    ]
