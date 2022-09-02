from turtle import title
from django.shortcuts import render
from . models import Post

def home(request):
    post = Post.objects.all()
    print(post)
    context = {'post' :post}
    return render(request, 'query.html', context)

def post_description(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render(request, 'postdesc.html', context)
