# Generated by Django 2.2.5 on 2020-11-12 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=500)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=500, verbose_name='标签')),
                ('zhuangtai', models.CharField(default='已投放', max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentator', models.CharField(max_length=90)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticleInfo', verbose_name='所属瓶子')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.DeleteModel(
            name='BottleArticles',
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='articletag',
            field=models.ManyToManyField(blank=True, to='article.ArticleTag', verbose_name='标签分类'),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterIndexTogether(
            name='articleinfo',
            index_together={('id', 'slug')},
        ),
    ]
