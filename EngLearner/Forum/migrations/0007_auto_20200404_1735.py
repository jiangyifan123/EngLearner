# Generated by Django 2.2 on 2020-04-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0006_auto_20200404_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commends',
            name='username',
            field=models.CharField(default='0', max_length=20, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='username',
            field=models.CharField(default='0', max_length=20, verbose_name='用户名'),
        ),
    ]
