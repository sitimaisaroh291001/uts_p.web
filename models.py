from django.db import models

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    publish = models.DateTimeField("tanggal publikasi")

    def __str__(self):
        return self.judul

# Create your models here.
