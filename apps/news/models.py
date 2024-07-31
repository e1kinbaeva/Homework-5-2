from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок новости')
    content = models.TextField(
        verbose_name='Содержание новости')
    image = models.ImageField(
        upload_to='news',
        verbose_name='Изображение новости')
    author = models.CharField(
        max_length=250,
        verbose_name='Автор новости')
    publication_date = models.DateField(

        verbose_name='Дата публикации')
  
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    