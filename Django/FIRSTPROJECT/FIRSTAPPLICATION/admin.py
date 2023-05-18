from django.contrib import admin
from .models import Information

# Register your models here.

@admin.register(Information)
class AdminInformation(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Contact', 'Address']