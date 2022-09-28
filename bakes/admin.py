"""
Imports external libraries for the program and
models to be used in this file
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Bake, Comment, BestFor


@admin.register(Bake)
class BakeAdmin(SummernoteModelAdmin):
    """
    Creates admin capabilities for bake management via admin panel
    Specifies which fields to use Summernote for
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    readonly_fields = ('slug',)
    list_filter = ('status', 'created_on', 'difficulty')
    search_fields = ('title', 'equipment', 'ingredients')
    summernote_fields = ('description', 'equipment', 'ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Creates admin capabilities for comment management via admin panel
    """
    list_display = ('name', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(BestFor)
class BestForAdmin(admin.ModelAdmin):
    """
    Creates admin capabilities for management of Best For bakes via admin panel
    """
    list_display = ('best_for', 'user', 'bake')
    list_filter = ('best_for',)
    search_fields = ('best_for',)
