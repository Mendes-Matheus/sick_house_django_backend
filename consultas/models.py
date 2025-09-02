import uuid
from django.db import models
from django.utils import timezone
from pacientes.models import Paciente

class TipoConsulta(models.TextChoices):
    NEUROCIRURGIAO = 'NEUROCIRURGIAO', 'Neurocirurgião'
    ORTOPEDISTA = 'ORTOPEDISTA', 'Ortopedista'
    CLINICO_GERAL = 'CLINICO_GERAL', 'Clínico Geral'
    PEDIATRA = 'PEDIATRA', 'Pediatra'
    GINECOLOGISTA = 'GINECOLOGISTA', 'Ginecologista'
    OFTALMOLOGISTA = 'OFTALMOLOGISTA', 'Oftalmologista'
    OTORRINOLARINGOLOGISTA = 'OTORRINOLARINGOLOGISTA', 'Otorrinolaringologista'
    UROLOGISTA = 'UROLOGISTA', 'Urologista'
    CARDIOLOGISTA = 'CARDIOLOGISTA', 'Cardiologista'

class StatusConsulta(models.TextChoices):
    PENDENTE = 'PENDENTE', 'Pendente'
    AGENDADA = 'AGENDADA', 'Agendada'
    REAGENDADA = 'REAGENDADA', 'Reagendada'
    REALIZADA = 'REALIZADA', 'Realizada'
    URGENTE = 'URGENTE', 'Urgente'
    IMEDIATA = 'IMEDIATA', 'Imediata'
    CANCELADA = 'CANCELADA', 'Cancelada'
    NAO_COMPARECEU = 'NAO_COMPARECEU', 'Não Compareceu'

class Estabelecimento(models.TextChoices):
    POLICLINICA = 'POLICLINICA', 'Policlínica'
    SARAH = 'SARAH', 'Sarah'
    REDE_MUNICIPAL = 'REDE_MUNICIPAL', 'Rede Municipal'

class Consulta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    tipo_consulta = models.CharField(max_length=50, choices=TipoConsulta.choices)
    status = models.CharField(max_length=20, choices=StatusConsulta.choices)
    data_solicitacao = models.DateField(default=timezone.now)
    data_agendamento = models.DateField(null=True, blank=True)
    estabelecimento = models.CharField(max_length=50, choices=Estabelecimento.choices, null=True, blank=True)
    observacao = models.TextField(max_length=1000, null=True, blank=True)
    motivo = models.CharField(max_length=500, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'consultas'

    def __str__(self):
        return f"Consulta {self.id} - {self.paciente.nome}"