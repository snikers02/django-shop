from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}#поля для автоматичного заповнення у нас заповнится slug


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated', 'category')#фільтри
    list_editable = ('price', 'available')#записуємо параметри які можна редагувати
    prepopulated_fields = {'slug': ('name',)}


