# Generated by Django 2.2 on 2020-04-11 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0006_auto_20200409_0049'),
        ('users', '0024_auto_20200411_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='words_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.IntegerField(default=0, verbose_name='进度')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
