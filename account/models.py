from django.db import models
from django.contrib.auth.models import AbstractUser

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

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_responsible = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    matricule = models.CharField(max_length=7)
    filiere = models.CharField(choices = FILIERE_CHOICES, max_length = 12)
    niveau = models.CharField(choices = NIVEAU_CHOICES, max_length = 12)


class Responsible(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    matricule = models.CharField(max_length=7)
