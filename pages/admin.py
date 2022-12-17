from django.contrib import admin
from .models import Project, Category, Image


class ProjectInline(admin.TabularInline):
    model = Project


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('projects',)
    inlines = (ProjectInline, )
    empty_value_display = 'Отсутствует'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'file',
        'category',
        'github_link',
        'website_link',
    )
    inlines = (ImageInline, )
    empty_value_display = 'Отсутствует'