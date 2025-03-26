from typing import Any
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = '#'
    ...
    
    
class ServicesView(TemplateView):
    template_name = '#'
    ...
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = [
            {"title": "Слаботочные системы",},
            {"title": "Умный дом"},
            ...
        ]
        return context
    
    
class ContactView(FormView):
    template_name = '#'
    form_class = ContactForm
    success_url = '/thanks/'
    
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
    
    