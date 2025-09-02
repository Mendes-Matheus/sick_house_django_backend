from rest_framework import serializers
from .models import Consulta
from pacientes.serializers import PacienteSerializer

class ConsultaSerializer(serializers.ModelSerializer):
    paciente_detail = PacienteSerializer(source='paciente', read_only=True)
    
    class Meta:
        model = Consulta
        fields = '__all__'