from django.shortcuts import render, get_object_or_404
from .models import Post, FeaturePost
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    return render(request, 'index.html')

def full_post(request, post_url):
    get_post = get_object_or_404(Post, url=post_url)
    return render(request, 'post.html', {'full_post': get_post})

