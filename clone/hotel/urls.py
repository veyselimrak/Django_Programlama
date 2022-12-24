from django.urls import path
from . import views


urlpatterns = [
    path('', views.hotel_list, name="hotel"),
    path('<slug:category_slug>/<int:hotel_id>', views.hoteldetay, name="hoteldetay"),

    # path(route, views, opt(kısayol ismi))
]