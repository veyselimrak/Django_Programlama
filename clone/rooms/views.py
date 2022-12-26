from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from rooms.models import Room



class RoomListView(ListView):
    model = Room
    template_name = 'rooms.html'
    context_object_name = 'rooms'
    
class Room_DetailView(DetailView):
    model = Room
    template_name = 'room_detail.html'
    context_object_name = 'room_detail'

