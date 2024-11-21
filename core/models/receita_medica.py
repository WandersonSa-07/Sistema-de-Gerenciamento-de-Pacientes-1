from core.models import *

class ReceitaMedica(models.Model):
    remedio = models.CharField(max_length=50)
    dosagem = models.CharField(max_length=4)
    qtd_de_dias = models.CharField(max_length=3)
    qtd_por_dia = models.CharField(max_length=2)

    def __str__(self):
        return self.remedio
