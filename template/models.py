from django.db import models



class Template(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    ue = models.CharField(max_length = 255)
    level = models.CharField(max_length = 255)
    mat = models.CharField(max_length = 7)
    phone = models.CharField(max_length = 255)
    date = models.CharField(max_length = 255)
    respo = models.CharField(max_length = 255)
    objet = models.CharField(max_length = 255)
    description = models.TextField()