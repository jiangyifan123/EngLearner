# Generated by Django 2.2 on 2020-04-10 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0006_auto_20200409_0049'),
        ('users', '0020_remove_boughtproduct_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='selected_words',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.product'),
        ),
    ]
