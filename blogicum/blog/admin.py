from django.contrib import admin

from .models import Post, Category, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('text', )
    list_display = (
        'id', 'title', 'author', 'text', 'category', 'location',
        'pub_date', 'is_published', 'created_at'
    )
    list_display_links = ('title',)
    list_editable = ('category', 'is_published', 'location')
    list_filter = ('created_at',)
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    list_display_links = ('title',)
    empty_value_display = '-пусто-'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_published')
    list_display_links = ('name',)
    empty_value_display = '-пусто-'
