# Generated by Django 2.2 on 2020-04-05 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0011_auto_20200405_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='commends',
            name='thumbs_down',
            field=models.IntegerField(default=0, verbose_name='踩数'),
        ),
        migrations.AddField(
            model_name='commends',
            name='thumbs_up',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
    ]
