# Generated by Django 2.2 on 2020-04-09 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_userprofile_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='quantity',
        ),
    ]
