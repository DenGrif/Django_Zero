from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django<br><a href='http://127.0.0.1:8000/new'>Дунем на вторую страничку</a></h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страничка моего проекта на Django</h1>")
