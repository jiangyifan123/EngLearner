# Generated by Django 2.2 on 2020-04-04 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commends',
            name='recommend',
        ),
        migrations.AddField(
            model_name='commends',
            name='recommend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Forum.Commends'),
        ),
    ]
