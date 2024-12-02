from core.models import *

class HorarioDisponivel(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_horario = models.DateTimeField()

    def str(self):
        return f"{self.medico} - {self.data_horario}"