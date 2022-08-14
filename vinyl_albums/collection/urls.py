from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('artists', views.artists, name="artists"),
    path('equipment', views.equipment, name="equipment"),
    path('the-sea-and-cake', views.tsac, name="tsac"),
]
