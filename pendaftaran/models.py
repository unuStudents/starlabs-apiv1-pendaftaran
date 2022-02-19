import uuid
from django.db import models

# Create your models here.
class Fakultas(models.Model):
    fakultas= models.CharField(max_length=100)
    
    def __str__(self):
        return '{} - {}'.format(self.id, self.fakultas)


class Prodi(models.Model):
    prodi   = models.CharField(max_length=50)
    fakultas= models.ForeignKey(Fakultas, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.id, self.prodi)


class Divisi(models.Model):
    divisi = models.CharField(max_length=20)

    def __str__(self) -> str:
        return '{} - {}'.format(self.id, self.divisi)


class Mahasiswa(models.Model):
    CHOICE_ANGKATAN = [
        (2019, '2019'),
        (2020, '2020'),
        (2021, '2021')
    ]
        
    id          = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    nama        = models.CharField(max_length=70)
    nim         = models.PositiveBigIntegerField(unique=True, null=True)
    email       = models.EmailField(unique=True)
    whatsapp    = models.CharField(max_length=20)
    alamat      = models.TextField(null=True)
    tgl_lahir   = models.DateField(null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    angkatan    = models.IntegerField(choices=CHOICE_ANGKATAN, default=2019)
    fakultas    = models.ForeignKey(Fakultas, on_delete=models.CASCADE)
    prodi       = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    divisi      = models.ForeignKey(Divisi, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.nama, self.divisi)