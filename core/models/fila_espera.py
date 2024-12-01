from core.models import *

class FilaEspera(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    ESTADO = (
          ("Waiting", "Em espera"),
          ("Being_Attended_to", "Em atendimento"),
          ("Attended", "Atendido"),
          ("Cancelled", "Cancelado")
     )
    estado = models.CharField(max_length=20, choices=ESTADO, default="Waiting")# quando salvar vai estar sempre definido como em espera

    horario_chamado = models.DateTimeField()


    created_at = models.DateTimeField(auto_now_add=True) #Quando criar a fila, adciona a data ao qual foi criado. Para sabermos quem chegou primeiro

    USERNAME_FIELD = 'codigo'
    
    class Meta():
        ordering = ["created_at"] #Ordena pela ordem de criação, ou seja, de chegada

    def __str__(self):
        return self.paciente.usuario.username + " - " + self.medico.usuario.username
    
    