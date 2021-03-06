# Generated by Django 4.0.2 on 2022-02-17 23:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Divisi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divisi', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fakultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fakultas', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prodi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodi', models.CharField(max_length=50)),
                ('fakultas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pendaftaran.fakultas')),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=70)),
                ('nim', models.PositiveBigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('whatsapp', models.CharField(max_length=20)),
                ('alamat', models.TextField()),
                ('tgl_lahir', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('angkatan', models.IntegerField(choices=[(2019, '2019'), (2020, '2020'), (2021, '2021')], default=2019)),
                ('divisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pendaftaran.divisi')),
                ('fakultas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pendaftaran.fakultas')),
                ('prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pendaftaran.prodi')),
            ],
        ),
    ]
