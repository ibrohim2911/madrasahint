from django.db.models import fields
from django.forms.widgets import RadioSelect
from django.shortcuts import redirect, render
from .models import User

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class usersview(CreateView):
    model = User
    template_name='register.html'
    fields= ['name','surname', 'age', 'number', 'daraja', 'vaqt']
    success_url = reverse_lazy('done')
class ModelListView(ListView):
    model = User
    template_name = "done.html"
class UserListView(ListView):
        model = User
        template_name = "home.html"
    
# Create your views here.
