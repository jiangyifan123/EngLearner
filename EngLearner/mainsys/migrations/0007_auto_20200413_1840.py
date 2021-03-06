# Generated by Django 2.2 on 2020-04-13 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsys', '0006_write_saving'),
    ]

    operations = [
        migrations.AlterField(
            model_name='write_saving',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='write_saving',
            name='writes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainsys.writes'),
        ),
    ]
