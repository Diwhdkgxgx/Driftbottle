import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm, UserForm
from .models import UserProfile, User
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Create your views here.
def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            #user = authenticate(username='username', password='password')
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
            else:
                error = {'error': '密码输入错误，请重新输入！'}
                return render(request, 'account/login.html', error,)

        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})

def main(request):
    return render(request, 'account/main.html')

def random_str():
    _str = '1234567890abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(_str) for i in range(4))

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        #emailverifyrecord_from = EmailVerifyRecordForm(request.POST)
        if request.POST.get('email_code') == request.session['email_code']:
            if user_form.is_valid() and userprofile_form.is_valid():
                new_user = user_form.save(commit=False)  # 数据还不需要保存入数据库，只生成了一个数据对象
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                new_profile = userprofile_form.save(commit=False)
                new_profile.user = new_user
                new_profile.save()
                success = {'success': '注册成功，点击返回登陆'}
                return render(request, "account/register.html", success)
            else:
                error = {'error': '信息填写有误,点击重新填写'}
                return render(request, "account/register.html", error)
        else:
            error = {'error': '验证码错误'}
            return render(request, "account/register.html", error)

    if request.method == 'GET':
        try:
            email = request.GET['email']
        except:
            email = ''
        email_code = random_str()
        msg = '验证码：' + email_code
        send_mail('邮箱验证', msg, settings.EMAIL_FROM, [email])
        print(email_code)
        # 将验证码保存到session中在接下来的操作中进行验证
        request.session['email_code'] = email_code
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        # #return HttpResponse('ok')
        return render(request, "account/register.html", {"form": user_form, "profile": userprofile_form,})

@login_required()
def myself(request):
    user = User.objects.get(username=request.user)
    if hasattr(request.user, 'userprofile'):
        userprofile = UserProfile.objects.get(user=request.user)
    else:
        UserProfile.objects.create(user=request.user)

    userprofile = UserProfile.objects.get(user=request.user)
    return render(request, "account/myself.html", {"user":request.user, "userprofile":userprofile})


@login_required()
def myself_edit(request):
    if hasattr(request.user, 'userprofile'):
        userprofile = UserProfile.objects.get(user=request.user)
    else:
        UserProfile.objects.create(user=request.user)
    userprofile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)

        if user_form.is_valid() * userprofile_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            request.user.email = user_cd['email']
            userprofile.phone = userprofile_cd['phone']
            userprofile.birth = userprofile_cd['birth']
            userprofile.sex = userprofile_cd['sex']
            userprofile.description = userprofile_cd['description']
            request.user.save()
            userprofile.save()
        return HttpResponseRedirect('/account/my-information')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"phone":userprofile.phone,
                                                    "birth":userprofile.birth,
                                                    "sex":userprofile.sex,
                                                    "description":userprofile.description})
        return render(request, "account/myself_edit.html", {"user_form":user_form, "userprofile_form":userprofile_form})

@login_required()
def about(request, id):
    userprofile = UserProfile.objects.filter(user_id=id)
    user = User.objects.filter(id=id).first()
    #return redirect(reverse(kwargs=kwargs))
    return render(request, "account/about.html", {"usern":user, "userprofile": userprofile,})



























