import graphene
from graphene_django import DjangoObjectType
from .models import *

# Create your code in here
# --->> START - Query <<---
class FakultasType(DjangoObjectType):
    class Meta:
        model  = Fakultas
        fields = '__all__'


class ProdiType(DjangoObjectType):
    class Meta:
        model  = Prodi
        fields = '__all__'


class DivisiType(DjangoObjectType):
    class Meta:
        model  = Divisi
        fields = '__all__'


class MahasiswaType(DjangoObjectType):
    class Meta:
        model  = Mahasiswa
        fields = '__all__'


class Query(graphene.ObjectType):
    all_fakultas = graphene.List(FakultasType)
    all_prodi    = graphene.List(ProdiType)
    all_divisi   = graphene.List(DivisiType)
    all_mahasiswa= graphene.List(MahasiswaType)

    fakultas = graphene.Field(FakultasType, fakultas_id=graphene.Int())

    def resolve_all_fakultas(self, info):
        return Fakultas.objects.all()

    def resolve_all_prodi(self, info):
        return Prodi.objects.all()

    def resolve_all_divisi(self, info):
        return Divisi.objects.all()

    def resolve_all_mahasiswa(self, info):
        return Mahasiswa.objects.all()

    def resolve_fakultas(self, info, fakultas_id):
        return Fakultas.objects.get(id=fakultas_id)
# --->> FINISH - Query <<---

# --->> START - Mutation <<---
class MahasiswaInput(graphene.InputObjectType):
    nama    = graphene.String(required=True)
    nim     = graphene.Int()
    email   = graphene.String(required=True)
    whatsapp= graphene.String(required=True)
    alamat  = graphene.String(required=True)
    tgl_lahir=graphene.Date()
    angkatan= graphene.ID()
    fakultas= graphene.ID()
    prodi   = graphene.ID()
    divisi  = graphene.ID()


class CreateMahasiswa(graphene.Mutation):
    mahasiswa = graphene.Field(MahasiswaType)
    class Arguments:
        mahasiswa_data = MahasiswaInput()

    @staticmethod
    def mutate(root, info, mahasiswa_data=None):
        mahasiswa_instance = Mahasiswa(
            nama     = mahasiswa_data.nama,
            nim      = mahasiswa_data.nim,
            email    = mahasiswa_data.email,
            whatsapp = mahasiswa_data.whatsapp,
            alamat   = mahasiswa_data.alamat,
            tgl_lahir= mahasiswa_data.tgl_lahir,
            angkatan = mahasiswa_data.angkatan,
            fakultas_id = mahasiswa_data.fakultas,
            prodi_id    = mahasiswa_data.prodi,
            divisi_id   = mahasiswa_data.divisi
        )
        mahasiswa_instance.save()
        return CreateMahasiswa(mahasiswa=mahasiswa_instance)


class Mutation(graphene.ObjectType):
    create_mahasiswa = CreateMahasiswa.Field()
# --->> FINISH - Mutation <<---