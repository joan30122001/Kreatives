from django.shortcuts import render, redirect
from .models import Template
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from  . import models
import pdfkit
from django.template.loader import get_template
from django.http.response import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import io
import datetime
from twilio.rest import Client


def template(request):
    return render(request, 'template.html')



def creer_requete(request):

    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        return render(request, 'email_sent.html', {'email':email})

    currentdate = datetime.date.today()
    return render(request, 'creer-requete.html', {'current_date':currentdate})



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
    account_sid = 'AC25fffecc0550d63d0eb20cd5793236b3'
    auth_token = '4d01a37db834e77914780908a65492dc'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Votre a bien été enregistré et envoyé",
        from_='+19378264862',
        to='+237697161353'
    )

    print(message.sid)

    return JsonResponse({"operation_result": f"{template.first_name} - {template.last_name} - {template.ue} - {template.level} - {template.mat} - {template.phone} - {template.date} - {template.respo} - {template.objet} - {template.description}"})



def preview_requete(request):
    templates = Template.objects.all()[:1]
    for template in templates:
        first_name = template.first_name,
        last_name = template.last_name,
        ue = template.ue,
        level = template.level,
        mat = template.mat,
        phone = template.phone,
        date = template.date,
        respo = template.respo,
        objet = template.objet,
        description = template.description

    return render(request, 'preview.html', {
        'first_name':first_name, 
        'last_name':last_name, 
        'ue':ue, 
        'mat':mat, 
        'mat':mat, 
        'level':level, 
        'phone':phone,
        'date':date, 
        'respo':respo, 
        'objet':objet,
        'description':description
    })



def generer_requete(request, id):
    template = Template.objects.get(pk = id)
    first_name = template.first_name,
    last_name = template.last_name,
    ue = template.ue,
    level = template.level,
    mat = template.mat,
    phone = template.phone,
    date = template.date,
    respo = template.respo,
    objet = template.objet,
    description = template.description

    templates = get_template('generator.html')
    context = {
        'first_name':first_name, 
        'last_name':last_name, 
        'ue':ue, 
        'level':level, 
        'mat':mat, 
        'phone':phone, 
        'date':date, 
        'respo':respo, 
        'objet':objet,
        'description':description
    }
    html = templates.render(context)
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)

    reponse = HttpResponse(pdf, content_type='application/pdf')
    reponse['Content-Disposition'] = 'attachment'
    return reponse


def download(request):
    template = Template.objects.all()
    return render(request, 'download.html', {'template':template})