from django.contrib import admin
from .models import Category, Post, FeaturePost

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'title',
        'category',
        'pub_date',
    )
    search_fields = (
        'title',
        'category',
        'content'

    )
    list_filter = (
        'category',
        'pub_date',
    )
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title',)


@admin.register(FeaturePost)
class FeaturePostAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'title',
        'category',
        'pub_date',
    )

