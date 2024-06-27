from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50, verbose_name='Наименование категории')
    description = models.CharField(max_length=250, verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category']

    def __str__(self):
        return self.category


class Product(models.Model):
    title = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Наименование товара')
    description = models.TextField(max_length=250, verbose_name='Описание товара', blank=True, null=True)
    image = models.ImageField(upload_to='catalog/images', verbose_name='Изображение(превью)', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания(записи в БД)')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения(записи в БД)')
    manufactured_at = models.DateTimeField(verbose_name='Дата производства продукта', blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title', 'price', 'created_at', 'updated_at', 'manufactured_at']

    def __str__(self):
        return self.name



