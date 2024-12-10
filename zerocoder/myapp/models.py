from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Импорт модели пользователя

class News_post(models.Model):
	title = models.CharField('Название новости', max_length=50)
	short_description = models.CharField('Краткое описание новости', max_length=200)
	text = models.TextField('Новость')
	pub_date = models.DateTimeField('Дата публикации')
	author = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='Автор',
		related_name='news_posts'
	)  # Поле для связи с пользователем

	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новость'
