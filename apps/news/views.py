# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from apps.news.models import Post


def index(request):
    posts = Post.objects.filter(published_at__lte=datetime.now()).order_by('-updated_at')
    paginator = Paginator(posts, 5)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    to_return = {'posts': posts}
    return render(request, 'news/index.html', to_return)


def post(request, category, slug, post_id):
    post = get_object_or_404(Post, category__slug=category, slug=slug, id=post_id)
    related = Post.objects.filter(category__slug=category).exclude(id=post.id).order_by('-published_at')[:3]
    to_return = {'post': post, 'related': related}
    return render(request, 'news/post.html', to_return)