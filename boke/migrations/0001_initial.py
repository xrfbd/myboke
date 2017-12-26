# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', models.CharField(max_length=3000, verbose_name='\u6b63\u6587')),
                ('date', models.DateTimeField(null=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('like', models.IntegerField(null=True, verbose_name='\u70b9\u8d5e')),
                ('reading', models.IntegerField(null=True, verbose_name='\u9605\u8bfb\u91cf')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=10, null=True, verbose_name='\u6807\u7b7e')),
                ('articles', models.ManyToManyField(to='boke.Article')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=12, verbose_name='\u6807\u7b7e')),
                ('password', models.CharField(max_length=12, verbose_name='\u6807\u7b7e')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='labels',
            field=models.ManyToManyField(to='boke.Label'),
        ),
    ]
