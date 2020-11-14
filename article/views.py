from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import ArticleInfo, ArticleTag, Comment, Bottle
from .forms import ArticleInfoForm, CommentForm, BottleForm
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
    global nb, article_info
    new_bottle = Bottle.objects.filter(~Q(postuser_id=id), zhuangtai=0)
    count = Bottle.objects.filter(~Q(postuser_id=id), zhuangtai=0).count()
    newuser = User.objects.get(id=id)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article_info
            new_comment.commentator = newuser
            new_comment.save()
            nb.com = new_comment
            nb.zhuangtai = 2
            nb.save()

        success = {"success": "success"}
        #return render(request, "article/article_get.html", success)
        return HttpResponseRedirect('/article/article-my-comment')

    else:
        if count != 0:
            rand = random.randrange(0, count)
            nb = new_bottle[rand]
            article_info = ArticleInfo.objects.get(id=nb.article_id)

        if count != 0:
            comment_form = CommentForm()
            nb.zhuangtai = 1
            nb.getuser = request.user.id
            nb.save()
            return render(request, "article/article_get.html",
                          {'article_info': article_info, "comment_form": comment_form})
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
        commented_bottle = Bottle.objects.filter(postuser_id=request.user.id, zhuangtai=2)
        comment = Comment.objects.all()
        return render(request, "article/article_my_commented.html", {"commented_bottle":commented_bottle, "comment":comment})

@login_required()
def article_my_get(request):
    if request.method == 'GET':
        commented_bottle = Bottle.objects.filter(getuser=request.user.id, zhuangtai=1)
        return render(request, "article/article_my_get.html", {"commented_bottle":commented_bottle})






