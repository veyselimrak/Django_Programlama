from django.urls import path
from . import views


urlpatterns = [
    path('', views.hotel_list, name="hotel"),
    path('<slug:category_slug>/<int:hotel_id>', views.hoteldetay, name="hoteldetay"),
    path('categories/<slug:category_slug>', views.category_list, name="hotel_by_category"),
    path('tags/<slug:tag_slug>', views.tag_list, name="hotel_by_tag"),
    # path(route, views, opt(kısayol ismi))
]