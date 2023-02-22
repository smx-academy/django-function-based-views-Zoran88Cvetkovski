from django.urls import path
from .views import korisnikime,pravoagolnik,proverka

urlpatterns = [
    path("ime-korisnik/", korisnikime),
    path ("pravo/",pravoagolnik),
    path("paren-neparen",proverka)


]