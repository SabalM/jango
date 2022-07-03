from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView,DeleteView #TemplateView,,DetailView
from django.core.paginator import Paginator
from classbased.models import Laptop
from .forms import LaptopRegistration
# Create your views here.
class LaptopListView(ListView):
    model=Laptop
    template_name='classbased/laptop-list.html'
    context_object_name='laptops'
    def get_context_data(self,*args,**kwargs):
        laptops=self.get_queryset()
        paginator=Paginator(laptops,5) 
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'laptops': page_obj}
        return context

class LaptopCreateView(CreateView):
    form_class = LaptopRegistration
    template_name = 'classbased/laptop-create.html'
    success_url = reverse_lazy('laptop-list')

class LaptopUpdateView(UpdateView):
    model=Laptop
    template_name='classbased/laptop-update.html'
    context_object_name='laptop'
    fields= ['manufacturer','name','ram','gpu','cpu','price']
    success_url=reverse_lazy('laptop-list')

class LaptopDeleteView(DeleteView):
    model=Laptop
    template_name='classbased/laptop-delete.html'
    success_url=reverse_lazy('laptop-list')