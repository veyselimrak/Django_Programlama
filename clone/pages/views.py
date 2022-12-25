from django.shortcuts import render
from django.views.generic import TemplateView
from hotel.models import Hotel
# def index(request):
#     return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = Hotel.objects.all().filter(status=True)
        return context
        
# def about(request):
#     return render(request, 'about.html')

class AboutView(TemplateView):
    template_name = "about.html"

def blog(request):
    return render(request, 'blog.html')
def blog(request):
    return render(request, 'blog_detail.html')

# Create your views here.
