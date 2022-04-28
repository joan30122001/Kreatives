from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import StudentSignUpForm, ResponsibleSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.core.mail import send_mail
from .models import User

def index(request):
    return render(request, 'index.html')



def register(request):
    return render(request, 'register.html')



def contact(request):

    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        return render(request, 'email_sent.html', {'email':email})

    return render(request, 'contact.html')



class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class responsible_register(CreateView):
    model = User
    form_class = ResponsibleSignUpForm
    template_name = 'responsible_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')



def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html',
    context={'form':AuthenticationForm()})



def logout_view(request):
    logout(request)
    return redirect('/')



# def contact(request):
#     # CONTACT FORM
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         form_data = {
#             'name':name,
#             'email':email,
#             'phone':phone,
#             'message':message,
#         }
#         message = '''
#         From:\n\t\t{}\n
#         Message:\n\t\t{}\n
#         Email:\n\t\t{}\n
#         Phone:\n\t\t{}\n
#         '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
#         send_mail('You got a mail!', message, '', ['ngounouloic675@gmail.com']) # TODO: enter your email address
        
#     return render(request, 'contact.html', {})