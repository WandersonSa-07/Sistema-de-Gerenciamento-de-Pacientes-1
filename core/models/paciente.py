from core.models import *

class Paciente(models.Model):
     usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
     profissao = models.CharField(max_length=100)
     data_nascimento = models.DateField()
    
     SEXO = (
          ("MAS", "Masculino"),
          ("FEM", "Feminino"),
          ("NAO_INFORMADO", "Não informar")
     )
     sexo = models.CharField(max_length=20, choices=SEXO)

     def __str__(self):
          return self.usuario.first_name + " " + self.usuario.last_name 
