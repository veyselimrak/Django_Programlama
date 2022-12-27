from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('enroll_the_hotel/', views.enroll_the_hotel, name="enroll_the_hotel")


    # path(route, views, opt(kısayol ismi))

]