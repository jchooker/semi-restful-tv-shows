from django.shortcuts import render
from .models import *

# Create your views here.
def all_shows(request):
    context = {
        'shows':Show.objects.all(),
    }
    return render(request, "shows.html", context)

def show_form(request):
    pass

def add_info(request):
    pass

def show_info(request, id):
    context = {
        'show':Show.objects.get(id=id)
    }
    return render(request, "view-show.html", context)

def edit_show(request, id):
    context = {
        'show':Show.objects.get(id=id),
    }
    return render(request, "edit-show.html", context)

def update_show(request):
    pass

def delete_show(request):
    pass