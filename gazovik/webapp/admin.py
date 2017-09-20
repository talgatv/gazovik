from django.contrib import admin
from .models import *


@admin.register(Tovar)
class TovarAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tovar._meta.fields]
    # raw_id_fields = ('user',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]
