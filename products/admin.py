from django.contrib import admin
from .models import Product, Category, Color

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display color names in the admin list


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
