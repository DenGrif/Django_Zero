from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    data = {
        'caption': 'CatDjango'
    }
    return render(request, 'myapp/news.html', data)

# def test_view(request):
#     return HttpResponse("<h1>Страница Test</h1><p>Это тестовая страница в приложении MyApp.</p>")




# from django.http import HttpResponse
#
# def data_view(request):
#     return HttpResponse('<h1>Страница с данными</h1><p>Здесь вы можете увидеть данные.</p>')
#
# def test_view(request):
#     return HttpResponse('<h1>Тестовая страница</h1><p>Добро пожаловать на тестовую страницу!</p>')
