from django.urls import path
from rooms.views import RoomListView, Room_DetailView
from . import views

urlpatterns = [
    path('', RoomListView.as_view(), name="rooms"),
    path('rooms/<int:pk>', Room_DetailView.as_view(), name="room_detail"),
]