from django import forms
from django.contrib.auth.models import User #引入django默认的User 模型
from .models import UserProfile, EmailVerifyRecord

class LoginForm(forms.Form):#对数据库不进行修改
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):#对数据库进行修改
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta: #声明本表单类所应用的数据模型，表单将会写进数据库的那些记录。表单类的属性和数据模型类中的属性一一对应。
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match")
        return cd['password2']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ("phone", "birth", "description", "sex", "jointime")


class EmailVerifyRecordForm(forms.ModelForm):
    class Meta:
        model = EmailVerifyRecord
        fields = ("code", "email", "send_time", "exprie_time",)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)