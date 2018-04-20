# coding:utf-8
from .models import Post, Category,Tag
from response import render_response, ErrorCode
from django.db.models.aggregates import Count
from utils import datetime_to_string
import markdown


def article_list(request):
    post_list = Post.objects.values('id', 'title', 'excerpt', 'views', 'modified_time', 'tags__name',
                                          'category__name', 'author__username').order_by('-modified_time')[:10]
    rows = []
    for post in post_list:
        row = {}
        row['id'] = post.get('id')
        row['category'] = post.get('category__name')
        row['title'] = post.get('title')
        row['excerpt'] = post.get('excerpt')
        row['views'] = post.get('views')
        row['author'] = post.get('author__username')
        row['modified_time'] = datetime_to_string(post.get('modified_time'))
        row['tags'] = post.get('tags__name',[])
        rows.append(row)
    return render_response(request, ErrorCode.OK, rows)


def detail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except:
        return render_response(request, ErrorCode.NOT_FOUND)
    post.increase_views()
    comment_list = post.comment_set.values('id','name','text','created_time')
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        # 'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    rows = []
    for comment in comment_list:
        row = {}
        row['id'] = comment.get('id')
        row['name'] = comment.get('name')
        row['text'] = comment.get('text')
        row['created_time'] = datetime_to_string(comment.get('created_time'))
        rows.append(row)
    article = {
        "id":post.id,
        "title":post.title,
        "content":post.body,
        "modified_time":post.modified_time,
        "author":post.author.username
    }
    context = {"post": article, "comment": rows}
    return render_response(request, ErrorCode.OK, context)


def archive(request, year, month):
    # post_list = Post.objects.raw('SELECT * FROM blog_post GROUP BY DATE_FORMAT(created_time, '%Y-%m')')
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    rows = []
    for post in post_list:
        row = {}
        row['id'] = post.get('id')
        row['id'] = post.get('id')
        row['id'] = post.get('id')
        row['id'] = post.get('id')
        row['id'] = post.get('id')
    return render_response(request, ErrorCode.OK, post_list)


def category(request):
    tags = Tag.objects.values('id','name','category','category__name').annotate(posts_num=Count('post'))
    rows = []
    for tag in tags:
        row = {}
        row['id'] = tag.get('id')
        row['name'] = tag.get('name')
        row['category_id'] = tag.get('category')
        row['category_name'] = tag.get('category__name')
        row['posts_num'] = tag.get('posts_num')
        rows.append(row)
    return render_response(request, ErrorCode.OK, rows)
