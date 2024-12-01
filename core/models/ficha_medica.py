from core.models import *

class FichaMedica(models.Model):
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    alergias = models.CharField(max_length=100)
    medicamentos_em_uso = models.CharField(max_length=50)
    observacoes = models.CharField(max_length=500)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.remedio
