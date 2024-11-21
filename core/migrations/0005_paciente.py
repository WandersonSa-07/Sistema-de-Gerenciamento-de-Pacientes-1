# Generated by Django 5.1.3 on 2024-11-21 15:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_medico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profissao', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Feminino'), ('NAO_INFORMADO', 'Não informar')], max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]