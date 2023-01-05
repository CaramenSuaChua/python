from django.contrib import admin
from .models import Data
# Register your models here.

@admin.register(Data)
class DataWeb(admin.ModelAdmin):
    list_display = ['name','link','price','description'] 
    admin.register(Data)