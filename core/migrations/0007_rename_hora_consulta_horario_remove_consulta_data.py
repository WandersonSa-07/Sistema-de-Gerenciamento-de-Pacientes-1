# Generated by Django 5.1.3 on 2024-11-21 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_consulta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='hora',
            new_name='horario',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='data',
        ),
    ]