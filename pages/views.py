from django.shortcuts import render

from posts.models import Post


def index(request):
    public_posts = Post.objects.is_public()
    return render(request, "landing/index.html", {"posts": public_posts})


def home(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, "home/index.html", {"posts": posts, "owner": True})
