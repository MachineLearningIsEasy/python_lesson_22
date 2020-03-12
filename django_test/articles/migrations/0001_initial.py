# Generated by Django 2.2.5 on 2020-02-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=100)),
                ('article_text', models.CharField(max_length=1000)),
                ('article_date', models.DateTimeField(verbose_name='date published')),
                ('article_tag', models.ManyToManyField(to='articles.Tag')),
            ],
        ),
    ]
