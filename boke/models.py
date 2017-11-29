# coding=utf-8
#from __future__ import unicode_literals

#from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

class Article(models.Model):
    title=models.CharField(u'标题',max_length=50)
    content=models.CharField(u'正文',max_length=3000)
    date = models.DateField(u'创建日期', null=True,auto_now_add=True)
    like = models.IntegerField(u'点赞', max_length=3000,null=True)
    reading = models.IntegerField(u'阅读量', max_length=3000,null=True)
    labels=models.ManyToManyField('Label')
    def __unicode__(self):
        return self.title

class Label(models.Model):
    label=models.CharField(u'标签',max_length=10,null=True)
    articles=models.ManyToManyField(Article)
