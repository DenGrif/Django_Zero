from django.http import HttpResponse
from django.shortcuts import render
from .models import News_post
from .forms import News_postForm


def home(request):
    news = News_post.objects.all()
    context = {
        'caption': 'CatDjango',
        'news': news
    }
    return render(request, 'myapp/news.html', context)

def create_news(request):
    form = News_postForm()
    return render(request, 'myapp/add_new_post.html', {'form':form})

