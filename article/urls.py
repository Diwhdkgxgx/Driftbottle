from django.urls import path, re_path
from article import views


app_name = "article"

urlpatterns = [
    path('article-post/', views.article_post, name="article_post"),
    #path('article-get/<int:id>', views.article_get, name="article_get"),
    re_path('article-get/(?P<id>\d+)/$', views.article_get, name="article_get"),
    path('article-my-post/', views.article_my_post, name="article_my_post"),
    path('article-my-comment/', views.article_my_comment, name="article_my_comment"),
    path('article-my-get/', views.article_my_get, name="article_my_get"),
    path('article-putback-done/', views.article_putback_done, name="article_putback_done"),

    ]