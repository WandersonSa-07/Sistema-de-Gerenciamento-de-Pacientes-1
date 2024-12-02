from core.models import *

class Consulta(models.Model):   
    horario = models.OneToOneField(HorarioDisponivel, on_delete=models.CASCADE)
    #data = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self) :
        return str(self.medico.especialidade.nome) + " - Dr." + str(self.medico.usuario.last_name) + " - " + str(self.horario.data_horario.strftime('%d/%m/%Y %H:%M'))
        

    