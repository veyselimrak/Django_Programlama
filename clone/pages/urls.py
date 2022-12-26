

from django.urls import path
from . import views
from .views import AboutView, IndexView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('blog/', views.blog, name="blog"),
    path('contact/', ContactView.as_view(), name = "contact"),

    # path(route, views, opt(kısayol ismi))

]