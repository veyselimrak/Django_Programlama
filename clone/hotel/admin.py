from django.contrib import admin
from . models import Hotel, Category, Tag

@admin.register(Hotel)

class  HotelAdmin(admin.ModelAdmin):
    list_display = ('title','status')
    list_filter = ('status',)
    search_fields = ('title', 'description')

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

@admin.register(Tag)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
