from django.contrib import admin
from .models import Lugares

class LugaresAdmin(admin.ModelAdmin):
    list_display = ('created','updated')

# Register your models here.

admin.site.register(Lugares, LugaresAdmin)