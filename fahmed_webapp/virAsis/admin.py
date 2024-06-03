from django.contrib import admin
from django.contrib import admin
from .models import ElecDom

@admin.register(ElecDom)
class ApplianceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'temperature', 'humidity')

