from django.shortcuts import render


def template(request):
    return render(request, 'template.html')


def creer_requete(request):
    return render(request, 'creer-requete.html')