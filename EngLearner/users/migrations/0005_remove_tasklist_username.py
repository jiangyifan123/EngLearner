# Generated by Django 2.2 on 2020-03-30 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200330_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='username',
        ),
    ]
