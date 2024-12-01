from core.models import *

class ReceitaMedica(models.Model):
    remedio = models.CharField(max_length=50)
    dosagem = models.CharField(max_length=10)
    qtd_de_dias = models.CharField(max_length=10)
    qtd_por_dia = models.CharField(max_length=10)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.remedio
