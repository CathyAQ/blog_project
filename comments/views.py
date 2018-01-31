# coding:utf-8
from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm


def post_comment(request,post_pk):
    post = get_object_or_404(Post,pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) #生成 comment模型实例，但不保存到数据库
            comment.post = post
            comment.save()
            return redirect(post) #传入为实例时，调用get_absolute_url
        else:
            comment_list = post.comment_set.all()
            context = {'post':post,'form':form,'comment_list':comment_list}
            return render(request,'blog/detail.html',context)
    return redirect(post)



