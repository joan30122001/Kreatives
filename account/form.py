from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Student,Responsible


FILIERE_CHOICES =(
    ("1", "INFO"),
    ("MATHS", "MATHS"),
    ("3", "PHY"),
    ("4", "CHM"),
    ("5", "BIOS"),
    ("6", "GEOS"),
)

NIVEAU_CHOICES =(
    ("1", "L1"),
    ("2", "L2"),
    ("3", "L3"),
    ("4", "M1"),
    ("5", "M2"),
)


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    matricule = forms.CharField(required=True)
    filiere = forms.ChoiceField(choices = FILIERE_CHOICES)
    niveau = forms.ChoiceField(choices = NIVEAU_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.phone_number=self.cleaned_data.get('phone_number')
        student.matricule=self.cleaned_data.get('matricule')
        student.filiere=self.cleaned_data.get('filiere')
        student.niveau=self.cleaned_data.get('niveau')
        student.save()
        return user

class ResponsibleSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    matricule = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_responsible = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        responsible = Responsible.objects.create(user=user)
        responsible.phone_number=self.cleaned_data.get('phone_number')
        responsible.matricule=self.cleaned_data.get('matricule')
        responsible.save()
        return user