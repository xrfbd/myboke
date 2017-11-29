# coding=utf-8

from django.shortcuts import render_to_response, redirect
from django.shortcuts import render
from django.http import HttpResponse
from models import Article,Label
from forms import NewArticleForm
from django import forms
#x新建帖子
def edit_article(request):
    if request.method == 'POST':
        art=NewArticleForm(request.POST)
        if art.is_valid():
            #print art.cleaned_data['label']
            print 'valisucceed'
            art.save()
            return HttpResponse('succeed')
        else:
            print 'validatefail'
            raise forms.ValidationError()
            #return HttpResponse('valid fail')
    else:
        labels=Label.objects.all()
        for label in labels:
            print '%s:%s'%(label.id,label.label)
        #labels=['1','python','mysql']
        return render_to_response('new_article.html',{'labels':labels})

#帖子列表
def article_list(request):
    arts=Article.objects.all()
    for art in arts:
        print art.labels.all()
    #return HttpResponse('ok')
    return render_to_response('articlelist.html',{'arts':arts})