from core.models import *

class Atendente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.codigo
   