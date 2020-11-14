from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import ArticleInfo, ArticleTag, Comment, Bottle
from .forms import ArticleInfoForm, BottleForm
from account.models import User
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

#放瓶子
@login_required()
@csrf_exempt
def article_post(request):
    if request.method == 'POST':
        article_post_form = ArticleInfoForm(data=request.POST)
        bottle_form = BottleForm(request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.save()
                newbottle = Bottle()
                newbottle.postuser = request.user
                newbottle.article = new_article
                newbottle.save()
                return  HttpResponse("1")
            except:
                return HttpResponse("2")
        else:
            return HttpResponse("3")
    else:
        article_post_form = ArticleInfoForm()
        bottle_form = BottleForm()
        return render(request, "article/article_post.html", {"article_post_form":article_post_form, "bottle_form":bottle_form} )

import random
from django.db.models import Q


@login_required()
@csrf_exempt
def article_get(request, id):
    global nb, article_info, new_comment
    new_bottle = Bottle.objects.filter(~Q(postuser_id=id), zhuangtai=0)
    count = Bottle.objects.filter(~Q(postuser_id=id), zhuangtai=0).count()
    newuser = User.objects.get(id=id)

    if request.method == 'POST':

        new_comment.article = ArticleInfo.objects.get(id=nb.article_id)
        new_comment.commentator = newuser
        new_comment.body = request.POST.get("body")


        if len(new_comment.body) != 0:
            new_comment.save()
            nb.com = new_comment
            nb.zhuangtai = 2
            nb.save()
            return HttpResponseRedirect('/article/article-my-comment')
            #return render(request, "article/article_get.html", success)
        else:
            new_comment.delete()
            nb.zhuangtai = 0
            nb.save()
            new_comment.save()
            return HttpResponseRedirect('/article/article-putback-done')


    else:

        if count != 0:
            rand = random.randrange(0, count)
            nb = new_bottle[rand]
            article_info = ArticleInfo.objects.get(id=nb.article_id)
            new_comment = Comment.objects.create(article_id=nb.article_id, commentator_id=request.user.id)
        if count != 0:
            nb.zhuangtai = 1
            nb.getuser = request.user.id
            nb.save()
            return render(request, "article/article_get.html",
                          {'article_info': article_info, "new_comment": new_comment})
        else:
            error = {'error': '海里面已经没有其他人的瓶子了qwq'}
            return render(request, "article/article_get.html", error)

@login_required()
def article_my_post(request):
    if request.method == 'GET':
        #post_bottle = Bottle.objects.all()
        post_bottle = Bottle.objects.filter(postuser_id=request.user.id)
        return render(request, "article/article_my_post.html", {"post_bottle":post_bottle})

@login_required()
def article_my_comment(request):
    if request.method == 'GET':
        commented_bottle = Bottle.objects.filter(getuser=request.user.id, zhuangtai=2)
        comment = Comment.objects.all()
        commented_bottle2 = Bottle.objects.filter(postuser_id=request.user.id, zhuangtai=2)
        return render(request, "article/article_my_commented.html", {"commented_bottle":commented_bottle, "commented_bottle2":commented_bottle2 })

@login_required()
def article_my_get(request):
    if request.method == 'GET':
        commented_bottle = Bottle.objects.filter(getuser=request.user.id, zhuangtai=1)
        return render(request, "article/article_my_get.html", {"commented_bottle":commented_bottle})

@login_required()
def article_putback_done(request):
    if request.method == 'GET':
        return render(request, "article/article_putback_done.html")



