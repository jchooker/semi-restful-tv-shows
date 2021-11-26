from django.db.models.expressions import Value
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages

# Create your views here.
def all_shows(request):
    context = {
        'shows':Show.objects.all(),
    }
    return render(request, "shows.html", context)

def show_form(request):
    context = {
        'shows':Show.objects.all()
    }
    return render(request, 'add-show.html', context)

def add_info(request):
    if request.method == "POST":
        errors = Show.objects.basic_manager(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return render(request, 'add-show.html')
        else:
            new_show=Show.objects.create(title=request.POST['show_title'], 
            network=request.POST['show_network'],
            release_date=request.POST['show_release_date'],
            desc=request.POST['show_desc']  
            )
            return redirect(f'/shows/{new_show.id}')
    else:
        return redirect('/')

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

def update_show(request, id):
    show_to_update = Show.objects.get(id=id)
    return redirect(f'/shows/{id}')

def delete_show(request, id):
    if request.method == "POST":
        show_to_delete = Show.objects.get(id=id)
        show_to_delete.delete()
        return redirect('/')
    else:
        return redirect('/')