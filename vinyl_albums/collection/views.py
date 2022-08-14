from django.shortcuts import render
from .models import Artist


# Create your views here.
def home(request):
    return render(request, "collection/home.html", {})

def artists(request):
    artists = Artist.objects.all().order_by("name")
    return render(request, "collection/artists.html", {'artists': artists})

def equipment(request):
    return render(request, "collection/equipment.html", {})

def tsac(request):
    return render(request, "collection/the-sea-and-cake.html", {})