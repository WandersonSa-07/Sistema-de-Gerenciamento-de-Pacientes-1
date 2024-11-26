from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, codigo, password, **extra_fields):
        if not codigo:
            raise ValueError('O código é obrigatório.')
        user = self.model(codigo=codigo, username=codigo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, codigo, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(codigo, password, **extra_fields)

class Usuario(AbstractUser):
    TIPO_CHOICES = (
        ('paciente', 'Paciente'),
        ('atendente', 'Atendente'),
        ('medico', 'Médico'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='paciente')
    codigo = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11, null=True, blank=True)

    USERNAME_FIELD = 'codigo'

    objects = UsuarioManager()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.codigo
        super().save(*args, **kwargs)

    def __str__(self):
        return self.codigo
