from django.shortcuts import render
from .models import Template
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from  . import models


def template(request):
    return render(request, 'template.html')



def creer_requete(request):
    return render(request, 'creer-requete.html')



@csrf_exempt
def operation_requete(request):
    a = request.POST.get("first_name")
    b = request.POST.get("last_name")
    c = request.POST.get("ue")
    d = request.POST.get("level")
    e = request.POST.get("mat")
    f = request.POST.get("phone")
    g = request.POST.get("date")
    h = request.POST.get("respo")
    i = request.POST.get("objet")
    j = request.POST.get("description")

    template = models.Template.objects.create(
        first_name = a, 
        last_name = b,
        ue = c,
        level = d,
        mat = e,
        phone = f,
        date = g,
        respo = h,
        objet = i,
        description = j
    )

    return JsonResponse({"operation_result": f"{template.first_name} - {template.last_name} - {template.ue} - {template.level} - {template.mat} - {template.phone} - {template.date} - {template.respo} - {template.objet} - {template.description}"})