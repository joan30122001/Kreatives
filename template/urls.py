from django.urls import path
from . import views 

app_name = "template"

urlpatterns = [
    path('template/',views.template, name='template'),
    path('creer_requete/',views.creer_requete, name='creer_requete'),
    path('operation_requete/',views.operation_requete, name='operation_requete'),
    path('preview_requete/',views.preview_requete, name='preview_requete'),
]
