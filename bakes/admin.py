from django.contrib import admin
from .models import Bake
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Bake)
class BakeAdmin(SummernoteModelAdmin):
    """
    Specifies which fields to use Summernote for
    """
    summernote_fields = ('description', 'equipment', 'ingredients', 'method')

