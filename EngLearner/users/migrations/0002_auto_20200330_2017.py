# Generated by Django 2.2 on 2020-03-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='task',
        ),
        migrations.AddField(
            model_name='tasklist',
            name='task',
            field=models.ManyToManyField(null=True, to='users.Task'),
        ),
    ]
