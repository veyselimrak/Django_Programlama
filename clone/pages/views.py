from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from hotel.models import Hotel, Room
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = Hotel.objects.all().filter(status=True)
        return context
        
class AboutView(TemplateView):
    template_name = "about.html"

def blog(request):
    return render(request, 'blog.html')
    
def blog(request):
    return render(request, 'blog_detail.html')

class ContactView(FormView, SuccessMessageMixin):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    success_message = "Mesajınız başarıyla alındı."

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


