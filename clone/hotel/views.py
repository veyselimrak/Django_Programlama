from django.shortcuts import render
from . models import Hotel

def hotel_list(request):
    hotel =  Hotel.objects.all()
    context = {
        'hotel' : hotel
    }
    return render(request, 'hotel.html', context)
    
def hoteldetay(request, category_slug, hotel_id):

    hoteldetay = Hotel.objects.get(category_id__slug = category_slug, id = hotel_id)
    context = {
        'hoteldetay': hoteldetay
    }
    return render(request, 'hoteldetay.html', context)
# Create your views here.