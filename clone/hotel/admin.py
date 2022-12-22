from django.contrib import admin
from . models import Hotel

@admin.register(Hotel)

class  HotelAdmin(admin.ModelAdmin):
    list_display = ('title','status')
    list_filter = ('status',)
    search_fields = ('title', 'description')