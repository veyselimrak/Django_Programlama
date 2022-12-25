from django.urls import path
from . import views
from pages.views import AboutView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('blog/', views.blog, name="blog"),


    # path(route, views, opt(kısayol ismi))

]