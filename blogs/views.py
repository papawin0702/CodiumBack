import re
from django.shortcuts import render,redirect
from .models import Post
from blogs.form import PostModelForm


# Create your views here.
def hello(request):
    tags=['วารี','เพลิง']
    rating=4
    return render(request,'index.html',
    {
        'name':'HutaoC1',
        'author':'PapawinFlash',
        'tags' :tags,
        'rating' : rating,
    })

def display(request):
    return render(request,'display.html')

def form(request):
    form = PostModelForm
    return render(request,'form.html', {'form': form})

def addBlog(request):
    form = PostModelForm(request.POST)
    if form.is_valid():
        form.save(commit=True)

    return redirect("blogs_display")

def display(request):
    data = Post.objects.all()
    return render(request,'display.html',
    {
        'Posts':data
    
    })

def edit(request, Post_id):
    '''show edit form'''
    post = Post.objects.get(id=Post_id)
    post_form = PostModelForm(instance=post)

    return render(request, "edit.html", {"form": post_form, 'Post_id': Post_id})


def save(request, Post_id):
    '''update data'''
    post = Post.objects.get(id=Post_id)
    form = PostModelForm(instance=post, data=request.POST)
    if form.is_valid():
        form.save(commit=True)
    return redirect("blogs_display")


def delete(request, Post_id):
    post = Post.objects.get(id=Post_id)
    post.delete()
    return redirect('blogs_display')
