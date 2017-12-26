# coding=utf-8

from django.shortcuts import render_to_response, redirect
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import Article,Label,User
from forms import NewArticleForm,LoginForm
from django import forms
from django.core.urlresolvers import reverse
import uuid

def index(request):
    return render_to_response('index.html',{'username':'yixiu'})

def logout(request):
    #清除cookie
    return HttpResponse(u'退出成功')

def login(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password)
            if user:
                #
                response=HttpResponseRedirect(reverse('index'))
                mysessionid=str(uuid.uuid4())
                response.set_cookie('mysessionid_cookie',mysessionid)
                #?????
                request.session[mysessionid] = user.username
                #
                return response
            else:
                return render_to_response('login.html',{'form':form,'error':form.errors})

        else:
            print 'validateerror'
            return render_to_response('login.html',{'form':form,'error':form.errors})
    else:
        #user=User.objects.create(username='xuran',password='111111')
        return render_to_response('login.html',{'form':form})
#x新建帖子
def edit_article(request):
    if request.method == 'POST':
        art=NewArticleForm(request.POST)
        if art.is_valid():
            print art.cleaned_data['label']
            print 'valisucceed'
            art.save()
            return HttpResponseRedirect(reverse('articlelist'))
        else:
            print 'validatefail'
            raise forms.ValidationError('validate error')
            #return HttpResponse('valid fail')

    else:
        labels=Label.objects.all()
        for label in labels:
            print '%s:%s'%(label.id,label.label)
        #labels=['1','python','mysql']
        return render_to_response('new_article.html',{'labels':labels})

#帖子列表
#问题：标签显示不出来
def article_list(request):
    arts=Article.objects.all()
    for art in arts:
        for i in art.labels.all():
            print 'label:',i.label
    #return HttpResponse('ok')
    return render_to_response('articlelist.html',{'arts':arts})