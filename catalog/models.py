from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Наименование товара')
    description = models.CharField(max_length=250, verbose_name='Описание товара')
    image = models.ImageField(upload_to='catalog/images', verbose_name='Изображение(превью)', blank=True, null=True)
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    data_creation = models.DateTimeField(verbose_name='Дата создания(записи в БД)')
    data_last_change = models.DateTimeField(verbose_name='Дата последнего изменения(записи в БД)')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['category_name', 'price', 'data_creation', 'data_last_change']

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Наименование категории')
    description = models.CharField(max_length=250, verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

