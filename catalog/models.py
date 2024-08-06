from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Наименование категории'
    )
    description = models.CharField(
        max_length=250,
        verbose_name='Описание категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='Категория'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование товара'
    )
    description = models.TextField(
        max_length=250,
        verbose_name='Описание товара',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='catalog/images',
        verbose_name='Изображение(превью)',
        blank=True, null=True)
    price = models.PositiveIntegerField(
        verbose_name='Цена за покупку'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания(записи в БД)'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего изменения(записи в БД)'
    )
    manufactured_at = models.DateTimeField(
        verbose_name='Дата производства продукта',
        blank=True,
        null=True
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
        help_text="Опубликовать",
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['category', 'price', 'created_at', 'updated_at', 'manufactured_at']

    def __str__(self):
        return self.name


class Version(models.Model):
    product_ver = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Наименование товара",
        help_text="Выберите название товара",
    )
    version_number = models.CharField(
        max_length=100,
        verbose_name="Номер версии",
        help_text="Введите номер версии",
        null=True,
        blank=True,
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
        null=True,
        blank=True,
    )
    is_version_active = models.BooleanField(
        default=False,
        verbose_name="Активность",
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_number", "version_name"]

    def __str__(self):
        return self.version_name

