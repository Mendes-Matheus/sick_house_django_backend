import uuid
from django.db import models
from django.utils import timezone

class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField(default=0)
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    rg = models.CharField(max_length=20, null=True, blank=True)
    cns = models.CharField(max_length=20, null=True, blank=True)
    nome_do_pai = models.CharField(max_length=200, null=True, blank=True)
    nome_da_mae = models.CharField(max_length=200, null=True, blank=True)
    celular1 = models.CharField(max_length=20, null=True, blank=True)
    celular2 = models.CharField(max_length=20, null=True, blank=True)
    sexo = models.CharField(max_length=15, choices=SEXO_CHOICES, null=True, blank=True)
    logradouro = models.CharField(max_length=200, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    data_cadastro = models.DateField(default=timezone.now)
    data_ultima_consulta = models.DateField(null=True, blank=True)
    observacao = models.TextField(max_length=1000, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'pacientes'

    def __str__(self):
        return self.nome