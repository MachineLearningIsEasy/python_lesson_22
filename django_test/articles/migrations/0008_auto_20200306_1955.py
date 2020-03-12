# Generated by Django 3.0.3 on 2020-03-06 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20200306_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 19, 55, 10, 304561)),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_img',
            field=models.ImageField(blank=True, null=True, upload_to='articles'),
        ),
    ]
