from django.contrib import admin
from . models import Room

@admin.register(Room)

class  RoomAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)