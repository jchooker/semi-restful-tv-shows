from django.shortcuts import render
from .models import *

# Create your views here.
def allShows(request):
    context = {
        'shows':Show.objects.all(),
    }
    return render(request, "all-shows.html", context)