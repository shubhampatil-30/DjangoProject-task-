from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import task 
from .forms import createform
from django.urls import reverse_lazy

# Create your views here.
class tasklist(ListView):
    model = task
    template_name = 'showlist.html'
    context_object_name = 'to'

class createtask(CreateView):
    model= task
    form_class = createform
    template_name = 'createtask.html'
    success_url = reverse_lazy('gg')

class updatetask(UpdateView):
    model= task
    form_class = createform
    template_name = 'updatetask.html'
    success_url = reverse_lazy('gg')

class viewtask(DetailView):
    model = task
    template_name = "viewtask.html"
    context_object_name = 'i'
class deletetask(DeleteView):
    model = task
    template_name = "deletetask.html"
    success_url = reverse_lazy('gg')
