from django.db.models import CharField
from django.db.models import TextField

from django.db import models

class Binatang(models.Model) :
    gambar = models.ImageField (upload_to="images")
    nama = models.CharField (max_length=255)
    latin = models.CharField (max_length=255)
    deskripsi = models.TextField()
    
    def __str__(self):
        return self.nama
    