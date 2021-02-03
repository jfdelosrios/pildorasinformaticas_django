from django.shortcuts import render

# Create your views here.

from .models import Post

def blog(request):

    posts=Post.objects.all()

    return render(request,'blog/blog.html', {'posts': posts})