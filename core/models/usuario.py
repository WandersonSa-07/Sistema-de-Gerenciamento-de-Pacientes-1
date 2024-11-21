from core.models import *
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, codigo, password, **extra_fields):
        if not codigo:
            raise ValueError('O codigo é obrigatório')
        user = self.model(codigo=codigo, username=codigo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, codigo, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(codigo, password, **extra_fields)

class Usuario(AbstractUser):
    codigo = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11, null=True, blank=True)

    USERNAME_FIELD = 'codigo'

    def __str__(self):
        return self.codigo
    
    objects = UsuarioManager()