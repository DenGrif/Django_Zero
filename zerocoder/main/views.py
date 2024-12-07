from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')


# def home(request):
#     # Формируем ссылки на страницы myapp
#     data_url = reverse('data-view')  # Используем имя маршрута для /myapp/data
#     test_url = reverse('test-view')  # Используем имя маршрута для /myapp/test
#
#     # Возвращаем HTML с ссылками
#     return HttpResponse(f"""
#            <h1>Это мой первый проект на Django<br><a href='http://127.0.0.1:8000/new'>Щёлкнем на вторую страничку в main</a></h1>
#            <p><a href="{data_url}">Перейти на страницу Data в myapp</a></p>
#            <p><a href="{test_url}">Перейти на страницу Test в myapp</a></p>
#        """)
#     #return HttpResponse("<h1>Это мой первый проект на Django<br><a href='http://127.0.0.1:8000/new'>Дунем на вторую страничку</a></h1>")
