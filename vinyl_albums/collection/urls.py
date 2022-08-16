from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('artists', views.artists, name="artists"),
    path('equipment', views.equipment, name="equipment"),
    path('the-sea-and-cake', views.tsac, name="tsac"),
    path('as-cities-burn', views.acb, name="acb"),
    path('ben-kweller', views.benkweller, name="ben-kweller"),
    path('dashboard-confessional', views.dashboard, name="dashboard"),
    path('david-bowie', views.bowie, name="bowie"),
    path('further-seems-forever', views.fsf, name="fsf"),
    path('green-day', views.greenday, name="greenday"),
    path('guardians-of-the-galaxy', views.guardians, name="guardians"),
    path('jeremy-enigk', views.jeremyenigk, name="jeremyenigk"),
    path('julien-baker', views.julienbaker, name="julienbaker"),
    path('michael-buble', views.michaelbuble, name="michaelbuble"),
    path('radiohead', views.radiohead, name="radiohead"),
    path('sam-prekop', views.samprekop, name="samprekop"),
    path('sunny-day-real-estate', views.sunnyday, name="sunnyday"),
    path('the-anniversary', views.theanniversary, name="theanniversary"),
    path('tortoise', views.tortoise, name="tortoise"),
    path('vince-guaraldi', views.vinceguaraldi, name="vinceguaraldi"),
    path('weezer', views.weezer, name="weezer"),
]
