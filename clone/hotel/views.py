from django.shortcuts import render
from . models import Hotel

def hotel_list(request):
    hotel =  Hotel.objects.all()
    context = {
        'hotel' : hotel
    }
    return render(request, 'hotel.html', context)
# Create your views here.
