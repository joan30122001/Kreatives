from django.urls import path
from .import  views

urlpatterns=[
    path('contact/',views.contact, name='contact'),
    path('register/',views.register, name='register'),
    path('student_register/',views.student_register.as_view(), name='student_register'),
    path('responsible_register/',views.responsible_register.as_view(), name='responsible_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
]