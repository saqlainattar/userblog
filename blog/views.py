from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post
from . import forms

@login_required
def post_list(request):
    # return HttpResponse('welcome')
    posts = Post.objects.all().order_by('-created_on')
    return render(request,'blog/post_list.html',{'posts': posts})

@login_required
def detail_view(request,slug):
    # return HttpResponse('Hello')
    # return render(request, 'blog/base.html')
    # return render(request, 'blog/post_detail.html')

    post = Post.objects.get(slug=slug)
    return render(request,'blog/post_detail.html',{'post':post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST,request.FILES)
        if form.is_valid():
            # save post in db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('post:list')
    else:
        form = forms.CreatePost()
    return render(request,'blog/post_create.html',{'form':form})



