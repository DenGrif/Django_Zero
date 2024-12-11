from django import forms
from .models import News_post

class News_postForm(forms.ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date']  # Указаны только существующие поля
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите краткое описание'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст новости'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
