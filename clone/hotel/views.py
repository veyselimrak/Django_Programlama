from django.shortcuts import render
from . models import Hotel, Category, Tag

def hotel_list(request):
    hotel =  Hotel.objects.all()
    context = {
        'hotel' : hotel,
    }
    return render(request, 'hotel.html', context)

def hotel_list2(request):
    index =  Hotel.objects.all()
    context = {
        'index' : index,
    }
    return render(request, 'index.html', context)
    
def hoteldetay(request, category_slug, hotel_id):

    hoteldetay = Hotel.objects.get(category_id__slug = category_slug, id = hotel_id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'hoteldetay': hoteldetay,
        'categories': categories,
        'tags':tags
    }
    return render(request, 'hoteldetay.html', context)
# Create your views here.

def category_list(request, category_slug):

    category_hotels = Hotel.objects.all().filter(category__slug = category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'category_hotels': category_hotels,
        'categories': categories,
        'tags':tags
    }
    return render(request, 'hoteldetay.html', context)

def tag_list(request, tag_slug):

    category_hotels = Hotel.objects.all().filter(tags__slug = tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'category_hotels': category_hotels,
        'categories': categories,
        'tags':tags

    }
    return render(request, 'hoteldetay.html', context)