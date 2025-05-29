from django.contrib import admin
from .models import Event, Category, GuestGroup

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(GuestGroup)
class GuestGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display  = ('name', 'date', 'location', 'capacity', 'type')
    list_filter   = ('type',)
    search_fields = ('name', 'description', 'location')
