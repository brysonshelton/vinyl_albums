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

def acb(request):
    return render(request, "collection/as-cities-burn.html", {})

def benkweller(request):
    return render(request, "collection/ben-kweller.html", {})

def dashboard(request):
    return render(request, "collection/dashboard-confessional.html", {})

def bowie(request):
    return render(request, "collection/david-bowie.html", {})

def fsf(request):
    return render(request, "collection/further-seems-forever.html", {})

def greenday(request):
    return render(request, "collection/green-day.html", {})

def guardians(request):
    return render(request, "collection/guardians-of-the-galaxy.html", {})

def jeremyenigk(request):
    return render (request, "collection/jeremy-enigk.html", {})

def julienbaker(request):
    return render(request, "collection/julien-baker.html", {})

def michaelbuble(request):
    return render(request, "collection/michael-buble.html", {})

def radiohead(request):
    return render(request, "collection/radiohead.html", {})

def samprekop(request):
    return render(request, "collection/sam-prekop.html", {})

def sunnyday(request):
    return render(request, "collection/sunny-day-real-estate.html", {})

def theanniversary(request):
    return render(request, "collection/the-anniversary.html", {})

def tortoise(request):
    return render(request, "collection/tortoise.html", {})

def vinceguaraldi(request):
    return render(request, "collection/vince-guaraldi.html", {})

def weezer(request):
    return render(request, "collection/weezer.html", {})