from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class profileAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name',)
    search_fields = ['first_name', 'last_name',]
