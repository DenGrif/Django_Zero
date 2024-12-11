from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import News_post
from .forms import News_postForm

def home(request):
    """
    Главная страница с отображением списка новостей.
    """
    news = News_post.objects.all()
    context = {
        'caption': 'CatDjango',
        'news': news
    }
    return render(request, 'myapp/news.html', context)

@login_required
def create_news(request):
    """
    Страница для добавления новостей.
    Только аутентифицированные пользователи могут добавлять новости.
    """
    error = ""
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            # Создаем объект, но пока не сохраняем его в базу
            news = form.save(commit=False)
            # Указываем текущего пользователя как автора
            news.author = request.user
            news.save()  # Сохраняем объект с автором
            return redirect('news_home')  # Перенаправляем на главную страницу
        else:
            error = "Данные были заполнены некорректно"
    else:
        form = News_postForm()
    return render(request, 'myapp/add_new_post.html', {'form': form, 'error': error})



# from mmap import error
#
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .models import News_post
# from .forms import News_postForm
#
#
# def home(request):
#     news = News_post.objects.all()
#     context = {
#         'caption': 'CatDjango',
#         'news': news
#     }
#     return render(request, 'myapp/news.html', context)
#
# def create_news(request):
#     error = ""
#     if request.method == 'POST':
#         form = News_postForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('news_home')
#         else:
#             error = "Данные были заполнены некорректно"
#     form = News_postForm()
#     return render(request, 'myapp/add_new_post.html', {'form':form, 'errors': error})
#
