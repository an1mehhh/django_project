from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', **NULLABLE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_last_updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего измерения')

    def __str__(self):
        return f"{self.name} {self.category} {self.price} {self.date_created}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('name', 'category', 'price', 'date_created')


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f"{self.category}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('category',)
