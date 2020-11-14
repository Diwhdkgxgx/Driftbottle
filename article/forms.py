

from .models import ArticleInfo, Comment, Bottle
from django import forms

class ArticleInfoForm(forms.ModelForm):
    class Meta:
        model = ArticleInfo
        fields = ("title", "body")

class BottleForm(forms.ModelForm):
    class Meta:
        model = Bottle
        fields = ("getuser",)


