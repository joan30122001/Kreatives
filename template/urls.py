from django.urls import path
from . import views 

app_name = "template"

urlpatterns = [
    path('template/',views.template, name='template'),
    path('creer_requete/',views.creer_requete, name='creer_requete'),
]
