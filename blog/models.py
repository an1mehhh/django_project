from django.db import models
from django.template.defaultfilters import slugify

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='content')
    image = models.ImageField(verbose_name='image', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='date time')
    is_published = models.BooleanField(default=True, verbose_name='published')
    views_count = models.IntegerField(default=0, verbose_name='number of views')

    def __str__(self):
        return f"{self.title} {self.title} {self.date_of_creation}"

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'post`s'
        ordering = ('-date_of_creation', )
