# coding=utf-8
from django import forms
from django.forms import widgets
from models import Article,Label

class NewArticleForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=3000)
    label= forms.IntegerField(required=False)
#    lebel2 = forms.ChoiceField(label='标签2：',required=False)
    def save(self):
        newarticle=Article(title=self.cleaned_data['title'],
                           content=self.cleaned_data['content'])
        newarticle.save()
        print self.cleaned_data['label']
        labs=self.cleaned_data['label']
        if labs:
            newarticle.labels.add(labs)
        else:
            newarticle.labels.add('1')
        return newarticle
