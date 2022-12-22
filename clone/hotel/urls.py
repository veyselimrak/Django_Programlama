from django.urls import path
from . import views


urlpatterns = [
    path('', views.hotel_list, name="hotel"),

    # path(route, views, opt(kısayol ismi))

]