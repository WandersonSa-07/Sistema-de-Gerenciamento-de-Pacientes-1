from core.models import *

class Consulta(models.Model):  
    HORARIO = (
          ("1", "07:00 - 07:30"),
          ("2", "07:30 - 08:00"),
          ("3", "08:00 - 08:30")
     )
    
    horario = models.CharField(max_length=20, choices=HORARIO)
    data = models.DateField()
    sintomas_apresentados = models.TextField(max_length=500)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.horario

    