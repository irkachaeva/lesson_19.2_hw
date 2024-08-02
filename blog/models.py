from django.db import models
from django.utils.text import slugify


class Blog(models.Model):

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, unique=True, db_index=True, null=True, blank=True, verbose_name="slug")
    body = models.TextField(max_length=250, verbose_name='Cодержимое', blank=True, null=True)
    image = models.ImageField(upload_to='blog/images', verbose_name='Изображение(превью)', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания(записи в БД)')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"