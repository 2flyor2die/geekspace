from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic.base import View
from blog.models import Post
from django.shortcuts import render,get_object_or_404,redirect

from .forms import CommentForm

def add_comment(request,post_pk):
    #     '''
    #     用户添加评论
    #     '''
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comments = post.comment_set.all()
            return render(request,'blog/detail.html',{
                "post": post,
                "form": form,
                "comments": comments
            })
    return redirect(post)