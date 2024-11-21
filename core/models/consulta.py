from core.models import *

class Consulta(models.Model):
    horario = models.DateTimeField()
    sintomas_apresentados = models.TextField(max_length=500)
    medico = models.OneToOneField(Medico, on_delete=models.CASCADE)

    def __str__(self) :
        return self.horario

    