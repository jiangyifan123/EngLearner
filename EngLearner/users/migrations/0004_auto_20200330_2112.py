# Generated by Django 2.2 on 2020-03-30 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_tasklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='task',
            field=models.ManyToManyField(to='users.Task'),
        ),
    ]