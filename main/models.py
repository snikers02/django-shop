from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'#параметр відображення у множенні


    def __str__(self):
        return self.name #метод для відображення назви категорії в адмінці(у нашому випадку по імені, бо повертаємо ім'я)\
    
    def get_absolute_url(self):
        return reverse("main:product_list_by_category", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)#'blank=True' - означає, що поле може бути пустим
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)#доступність товару
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:product_detail", args=[self.id, self.slug])



