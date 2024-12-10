from django.http import HttpResponse
from django.shortcuts import render
from .models import News_post


def home(request):
    news = News_post.objects.all()
    context = {
        'caption': 'CatDjango',
        'news': news
    }
    return render(request, 'myapp/news.html',context)

# def test_view(request):
#     return HttpResponse("<h1>Страница Test</h1><p>Это тестовая страница в приложении MyApp.</p>")




# from django.http import HttpResponse
#
# def data_view(request):
#     return HttpResponse('<h1>Страница с данными</h1><p>Здесь вы можете увидеть данные.</p>')
#
# def test_view(request):
#     return HttpResponse('<h1>Тестовая страница</h1><p>Добро пожаловать на тестовую страницу!</p>')
